Intentional vulnerabilities (for classroom exploration)

This section describes the intentionally insecure patterns included in the demo, why they are risky, and how to fix them.

1) Reflected input displayed without sanitization (client-side XSS)
- Files: `site/submit.html`, `site/vulnerable.html`
- What: User-supplied values from query parameters are inserted into the DOM using `innerHTML`.
- Risk: If an attacker can supply HTML/JS (for example `<script>alert(1)</script>`), it will execute in the victim's browser.
- How students can test: Run the site locally and submit a message containing `<script>alert('xss')</script>` in the message or the search box.
- Fixes: Escape or sanitize user input. Use `textContent` instead of `innerHTML`, or apply a proper escape function on the server.

2) Visible form submission data (GET)
- File: `site/contact.html`
- What: The contact form uses `GET`, so the data appears in the URL.
- Risk: Sensitive data can end up in logs or browser history.
- Fixes: Use `POST` for sensitive data; avoid logging or storing unnecessary fields.

Teaching ideas and exercises:
- Have students demonstrate and then patch the XSS by changing `innerHTML` to safely-escaped text.
- Show the difference between GET and POST by switching the form method and observing the URL.
- Discuss server-side validation and output encoding as a general mitigation strategy.

Compare vulnerable vs safe demo:
- The repository contains `site/vulnerable.html` (intentionally unsafe) and `site/safe.html` (a safe implementation).
- Exercise: open both pages, submit the same payload (for example `<script>alert("xss")</script>`), and observe the different behaviors.
- After students patch `submit.html` (or `vulnerable.html`) to use `textContent` or server-side escaping, verify the attack no longer executes.

Safety note: Only test these attacks on local instances or classroom networks you control.
