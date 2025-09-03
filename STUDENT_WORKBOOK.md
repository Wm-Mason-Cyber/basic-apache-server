# Student Workbook — Basic Apache Server

Use this printable workbook in class. It mirrors `docs/student-workbook.md`.

## Objectives
- Understand how static files are served by Apache
- Explore a simple reflected input vulnerability (client-side)
- Learn a safe way to display user input (use textContent/escape output)

## Setup (teacher should ensure Docker is running)

```bash
docker build -t basic-apache-server .
docker run --rm -p 8080:80 basic-apache-server
```

Open http://localhost:8080 in your browser.

## Explore the site
- Open `/index.html` and `/about.html` to understand the layout.
- Open `/contact.html`, submit a message like "hello" and observe the `submit.html` page.

## Demonstrate the vulnerability
- In `/contact.html` send a message containing this payload (ONLY on your local instance):

```
<img src=x onerror="document.title='XSS-TRIGGERED'">
```

- Observe whether the page title changes to `XSS-TRIGGERED` on the `submit.html` page.

## Patch the code (client-side safe fix)
- Open `site/submit.html` in a text editor. Find the place where the page sets `innerHTML` with user-supplied content and change it to use `textContent` or create DOM nodes with `document.createElement` + `textContent`.

## Verify the fix
- Reload `submit.html` with the same payload and confirm the page title does not change.

## Discussion questions
- Why is it dangerous to insert unsanitized user input into a page?
- What are server-side fixes for XSS?
- When would you still need additional escaping even if using `textContent`?

---

---

Automated tests use a Python virtual environment. To set up:

```bash
python3 -m venv venv
source venv/bin/activate
pip install selenium
```

The `.gitignore` excludes `venv/` and Python cache files.

Safety reminder: Only test exploits on local or classroom networks you control.
