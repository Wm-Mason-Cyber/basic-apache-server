Setup and running (local / Docker)

Prerequisites:
- Docker installed locally

Build and run:

```bash
# from the repo root
docker build -t basic-apache-server .

# run and map container port 80 to your host port 8080
docker run --rm -p 8080:80 basic-apache-server
```

Then open http://localhost:8080 in a browser.

Teaching notes:
- This demo is self-contained and uses only static files. No external network requests are required.
- Because the "vulnerabilities" are client-side and local, students can test attacks safely without impacting external systems.
- If you prefer, you can mount the `site/` folder into a running `httpd` container to edit files live:

```bash
docker run --rm -p 8080:80 -v "$(pwd)/site:/usr/local/apache2/htdocs/" httpd:2.4
```

That command lets you edit files locally and reload the page in the browser to see changes.
