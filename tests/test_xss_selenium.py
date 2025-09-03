#!/usr/bin/env python3
"""
Selenium-based XSS test for the Basic Apache Server demo.

Requires:
- Docker (for the site)
- Python 3
- selenium (`pip install selenium`)
- Chrome or Chromium and chromedriver (installable via apt)

Run:
  sudo python3 tests/test_xss_selenium.py

This test will:
- Build and run the Docker container
- Open /submit.html and /vulnerable.html with an XSS payload
- Check if the payload is executed (alert or script in DOM)
- Confirm /safe.html does NOT execute the payload
"""
import subprocess
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException

HOST = 'http://127.0.0.1:8080'
CONTAINER_NAME = 'basic-apache-server-test'
IMAGE_NAME = 'basic-apache-server'

XSS_PAYLOAD = "<img src=x onerror=\"document.title='XSS-TRIGGERED'\">"


def run(cmd, check=True):
    print(f">>> {cmd}")
    res = subprocess.run(cmd, shell=True, check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = res.stdout.decode(errors='replace')
    print(out)
    if check and res.returncode != 0:
        raise SystemExit(f"Command failed (exit {res.returncode}): {cmd}\nOutput:\n{out}")
    return out


def start_container():
    run(f"sudo docker build -t {IMAGE_NAME} .")
    run(f"sudo docker run -d --name {CONTAINER_NAME} -p 8080:80 {IMAGE_NAME}")
    print('Waiting for server...')
    time.sleep(2)


def stop_container():
    run(f"sudo docker stop {CONTAINER_NAME}", check=False)
    run(f"sudo docker rm {CONTAINER_NAME}", check=False)


def test_xss(url, should_trigger):
    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-gpu')
    opts.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=opts)
    driver.set_page_load_timeout(10)
    try:
        driver.get(url)
        time.sleep(1.5)
        # Check if the payload changed the title
        title = driver.title
        if should_trigger:
            if 'XSS-TRIGGERED' in title:
                print(f'[PASS] XSS triggered as expected on {url}')
                return True
            else:
                print(f'[FAIL] XSS did NOT trigger on {url}')
                return False
        else:
            if 'XSS-TRIGGERED' in title:
                print(f'[FAIL] XSS triggered on SAFE page {url}')
                return False
            else:
                print(f'[PASS] XSS did NOT trigger on safe page {url}')
                return True
    finally:
        driver.quit()


def main():
    try:
        start_container()
        errors = []
        # /submit.html
        submit_url = f"{HOST}/submit.html?name=Attacker&email=evil%40x.com&message={XSS_PAYLOAD}"
        if not test_xss(submit_url, should_trigger=True):
            errors.append('submit.html did not trigger XSS as expected')
        # /vulnerable.html
        vuln_url = f"{HOST}/vulnerable.html?q={XSS_PAYLOAD}"
        if not test_xss(vuln_url, should_trigger=True):
            errors.append('vulnerable.html did not trigger XSS as expected')
        # /safe.html
        safe_url = f"{HOST}/safe.html?q={XSS_PAYLOAD}"
        if not test_xss(safe_url, should_trigger=False):
            errors.append('safe.html triggered XSS (should be safe)')
        if errors:
            print('\nTEST FAILS:')
            for e in errors:
                print('- ' + e)
            raise SystemExit(2)
        print('\nAll XSS tests passed (site vulnerabilities behave as described in the workbook).')
    finally:
        stop_container()

if __name__ == '__main__':
    main()
