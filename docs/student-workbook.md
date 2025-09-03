Student workbook — Basic Apache Server

This workbook is designed to be printed or distributed to students. It guides them through exploring the demo site, discovering a reflected XSS vulnerability, and applying a safe fix.

1) Objectives
- Understand how static files are served by Apache
- Explore a simple reflected input vulnerability (client-side)
- Learn a safe way to display user input (use textContent/escape output)

2) Setup (teacher should ensure Docker is running)
- Build and run the demo:

```bash
docker build -t basic-apache-server .
docker run --rm -p 8080:80 basic-apache-server
```

Open http://localhost:8080 in your browser.

3) Explore the site
- Open `/index.html` and `/about.html` to understand the layout.
- Open `/contact.html`, submit a message like "hello" and observe the `submit.html` page.

4) Demonstrate the vulnerability
- In `/contact.html` send a message containing this payload (ONLY on your local instance):

```
<script>alert('xss')</script>
```

- Observe whether an alert executes on the `submit.html` page.

5) Patch the code (client-side safe fix)
- Open `site/submit.html` in a text editor. Find the place where the page sets `innerHTML` with user-supplied content and change it to use `textContent` or create DOM nodes with `document.createElement` + `textContent`.

6) Verify the fix
- Reload `submit.html` with the same payload and confirm the alert no longer executes.

7) Discussion questions
- Why is it dangerous to insert unsanitized user input into a page?
- What are server-side fixes for XSS?
- When would you still need additional escaping even if using `textContent`?

8) Extra challenges
- Change the form method to `POST` and discuss why POST is preferred for sensitive data.
- Implement a small server (Flask or Express) that escapes output server-side and compare.

---

Safety reminder: Only test exploits on local or classroom networks you control.
