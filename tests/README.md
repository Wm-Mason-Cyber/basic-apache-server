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
