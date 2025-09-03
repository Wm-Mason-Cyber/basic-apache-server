Website structure

Top-level:
- `site/` — files that Apache will serve. The root of the website corresponds to the `site/` folder.

Important pages:
- `index.html` — home
- `about.html` — description and audience
- `contact.html` — example form (GET method used intentionally)
- `submit.html` — reveals form values using unsanitized insertion (client-side)
- `vulnerable.html` — simple search demo that reflects `q` into the page

Assets:
- `site/assets/style.css` — basic styling

Use this file to explain what each page does and how it maps to the filesystem. In Apache, the site root maps to `/usr/local/apache2/htdocs/` inside the container.
