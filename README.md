<!-- README rewritten for clarity and classroom use -->
# Basic Apache Server — Classroom demo 🧑‍🏫🐳

A tiny, safe (but intentionally instructive) website served by Apache. This repo is designed for classroom use to demonstrate how static websites are served and to teach common web vulnerabilities in a controlled environment.

## Quick links

- Live demo (when running locally): http://localhost:8080
- Student workbook: `STUDENT_WORKBOOK.md` (printable)
- Docs: `docs/` — setup, structure, vulnerabilities, lesson plan

---

## Quick start

Build and run the demo using Docker (from the repository root):

```bash
# build the Docker image
docker build -t basic-apache-server .

# run the site on localhost:8080
docker run --rm -p 8080:80 basic-apache-server
```

Open http://localhost:8080 in your browser.

See `docs/setup.md` for a live-mount example and additional teaching notes.

---

## What's included

- `site/` — the website files Apache serves. Key pages:
  - `/index.html` — Home and quick exercises
  - `/about.html` — About the demo
  - `/contact.html` — Contact form (uses GET intentionally)
  - `/submit.html` — Displays submitted values (intentionally unsafe)
  - `/vulnerable.html` — Demonstration of reflected input
  - `/safe.html` — Safe implementation students can compare against
  - `assets/` — CSS and static assets

- `docs/` — classroom documentation and lesson materials.
  - `docs/overview.md` — project goals and tour
  - `docs/setup.md` — Docker run/build instructions
  - `docs/vulnerabilities.md` — detailed descriptions and exercises
  - `docs/lesson-plan.md` — suggested class flow

- `tests/` — small automated harness that builds the image, runs a container, fetches pages, and checks for the expected demo patterns (see `tests/README.md`).

---

## Very short Docker overview

Docker packages applications into containers. We use the official `httpd:2.4` image and copy our `site/` into the container's document root. Students don't need to install Apache — they only need Docker to run this demo locally.

Read more:
- Official getting started: https://docs.docker.com/get-started/
- Docker overview for educators: https://www.docker.com/resources/what-container

Basic commands (copyable):

```bash
# build image from repository root
docker build -t basic-apache-server .

# run the site on localhost:8080
docker run --rm -p 8080:80 basic-apache-server

# stop a running container by name (if you started it detached)
docker stop <container-name>
```

---

## Safety notes 🔒

This project intentionally includes small, benign insecure patterns so students can safely explore and fix them. Do not deploy these vulnerable pages on public servers. Always test attacks on local machines or controlled classroom networks.

---

## Student workbook (printable) 📘

A printable student workbook is included at `STUDENT_WORKBOOK.md` and `docs/student-workbook.md`. It guides students through:

- exploring the site
- demonstrating a reflected XSS payload in a safe, local environment
- patching client-side code (safe example provided in `site/safe.html`)
- discussion questions and follow-ups

---

## License

See `LICENSE` for licensing details.

---

If you'd like, I can add a small CLI helper (`dev.sh`) to make build/run/stop easier for students, or create a branch with the exercise steps pre-applied. Tell me which you'd prefer.
