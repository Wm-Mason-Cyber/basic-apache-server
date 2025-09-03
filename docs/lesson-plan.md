Lesson plan (suggested)

Duration: 45–90 minutes depending on depth.

1) 10 minutes — Introduction
- Explain the Apache container and where files are served from.
- Show `index.html` and `about.html`.

2) 15–30 minutes — Hands-on vulnerability discovery
- Students open `contact.html` and `submit.html` and try submitting scripts in the message field.
- Observe the result and explain reflected XSS.

3) 10–20 minutes — Fixes and discussion
- Students implement a fix (e.g., change `innerHTML` -> `textContent` in `submit.html`) and observe the difference.
- Discuss server-side vs. client-side mitigations, logging concerns, and secure defaults.

4) Wrap-up
- Run through the `docs/vulnerabilities.md` and discuss further reading and next steps.

Optional extension: Add a simple backend (e.g., a minimal Python/Flask app) to show server-side handling and how to properly encode outputs.
