Overview

This project is a small, intentionally-simple website served by Apache. It's designed for classroom exploration and includes a few intentionally insecure patterns so students can safely learn how to find and fix common issues.

Goals:
- Demonstrate how static files are served by Apache
- Provide easy-to-understand examples of reflected input handling (a client-side XSS demonstration)
- Supply clear documentation and exercises for students of varying experience levels

Files of interest:
- `site/index.html` — home page
- `site/contact.html` — a simple contact form
- `site/submit.html` — displays submitted form values in an unsafe way (reflected input)
- `site/vulnerable.html` — search box that reflects the query unsafely

See the other docs for setup, structure, and vulnerability explanations.
