#!/usr/bin/env python3
"""
Simple test harness for the basic-apache-server demo.

What it does:
- Builds the Docker image (requires Docker installed and accessible via sudo)
- Runs a temporary container mapped to localhost:8080
- Fetches a few pages and checks for expected content and intentionally vulnerable patterns
- Stops and removes the container

Run: sudo python3 tests/test_site.py
(Uses sudo because docker commands in this environment required sudo)
"""

import subprocess
import time
import urllib.request
import sys

HOST = 'http://127.0.0.1:8080'
CONTAINER_NAME = 'basic-apache-server-test'
IMAGE_NAME = 'basic-apache-server'


def run(cmd, check=True):
    print(f">>> {cmd}")
    res = subprocess.run(cmd, shell=True, check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = res.stdout.decode(errors='replace')
    print(out)
    if check and res.returncode != 0:
        raise SystemExit(f"Command failed (exit {res.returncode}): {cmd}\nOutput:\n{out}")
    return out


def fetch(path, timeout=5):
    url = HOST + path
    for _ in range(timeout*2):
        try:
            with urllib.request.urlopen(url, timeout=2) as r:
                return r.read().decode(errors='replace')
        except Exception as e:
            time.sleep(0.5)
    raise RuntimeError(f"Timed out fetching {url}")


def main():
    try:
        # Build image
        run(f"sudo docker build -t {IMAGE_NAME} .")

        # Run container
        cid = run(f"sudo docker run -d --name {CONTAINER_NAME} -p 8080:80 {IMAGE_NAME}")

        # Wait and fetch pages
        print('Waiting for server...')
        index = fetch('/')
        print('Fetched index page (first 300 chars):')
        print(index[:300])

        vulnerable_html = fetch('/vulnerable.html')
        submit_html = fetch('/submit.html')
        contact_html = fetch('/contact.html')

        # Checks
        errors = []
        if 'Welcome to the Basic Apache Server Demo' not in index:
            errors.append('index page does not contain expected welcome text')

        # Check that the intentionally-vulnerable client-side JS exists
        for name, content in (('vulnerable.html', vulnerable_html), ('submit.html', submit_html)):
            if 'innerHTML' not in content and 'URLSearchParams' not in content:
                errors.append(f"{name} does not contain expected vulnerable JS patterns (innerHTML/URLSearchParams)")

        # Check the contact form uses GET (intentional)
        if 'method="get"' not in contact_html.lower() and 'method=get' not in contact_html.lower():
            errors.append('contact form does not use GET (expected for demo)')

        if errors:
            print('\nTEST FAILS:')
            for e in errors:
                print('- ' + e)
            raise SystemExit(2)

        print('\nAll checks passed (site served and vulnerable patterns present as expected).')

    finally:
        print('\nTearing down container (if running)')
        run(f"sudo docker stop {CONTAINER_NAME}", check=False)
        run(f"sudo docker rm {CONTAINER_NAME}", check=False)


if __name__ == '__main__':
    main()
