Test harness for the Basic Apache Server demo

This folder contains a simple Python script to build the demo Docker image, run a temporary container, fetch a few pages, verify expected content and vulnerable patterns, and then clean up.

Requirements:
- Docker installed and usable (this environment used `sudo` for docker commands)
- Python 3

Run the tests:

```bash
# from repo root
sudo python3 tests/test_site.py
```

What it checks:
- The image builds successfully
- The container serves `/`, `/vulnerable.html`, `/submit.html`, and `/contact.html`
- `/submit.html` and `/vulnerable.html` contain the intentionally vulnerable client-side patterns (`innerHTML`, `URLSearchParams`)
- The contact form uses `GET` (for demonstration)

This harness is intentionally simple and classroom-friendly. You can extend it to assert more behaviors or integrate with CI later.

---

## XSS vulnerability test (headless browser)

A more realistic test is provided in `test_xss_selenium.py` using Selenium and headless Chrome. This test will:
- Build and run the Docker container
- Open `/submit.html` and `/vulnerable.html` with an XSS payload
- Check if the payload is executed (by changing the page title)
- Confirm `/safe.html` does NOT execute the payload

### Requirements
- Docker
- Python 3
- Selenium (`pip install selenium`)
- Chrome or Chromium and chromedriver (installable via apt)

### Run the test:

```bash
python3 -m venv venv
source venv/bin/activate
pip install selenium
sudo apt-get install -y chromium-driver chromium
sudo python3 tests/test_xss_selenium.py
```


If you see `[PASS] XSS triggered as expected` for the vulnerable pages and `[PASS] XSS did NOT trigger on safe page` for the safe page, the vulnerabilities are working as described in the workbook.

**XSS payload used for testing:**

```
<img src=x onerror="document.title='XSS-TRIGGERED'">
```

The `.gitignore` excludes `venv/` and Python cache files.
