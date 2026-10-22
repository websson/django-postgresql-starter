# Django + PostgreSQL starter

[![Deploy to Uppcoder](deploy-to-uppcoder.svg)](https://portal.uppcoder.com/cust-portal/deploy?starter=django-postgresql-starter&utm_source=github&utm_medium=repo&utm_campaign=django-starter)

A small Django project on PostgreSQL, ready to deploy: a notes page and the
Django admin. Everything that changes between your laptop and a server comes
from environment variables, so no password sits in the code, and it already has
the two settings that usually cost an afternoon behind an HTTPS proxy.

## What is already set up

- **The database from the environment:** `POSTGRES_DB`, `POSTGRES_USER`,
  `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`. Without them it falls
  back to SQLite, so it always starts.
- **`SECURE_PROXY_SSL_HEADER`:** a proxy that ends HTTPS passes requests on over
  HTTP. Without this setting Django thinks the request was plain HTTP, and the
  admin login fails with "403 Origin checking failed".
- **`CSRF_TRUSTED_ORIGINS`** from the app's own address (`UPPCODER_SELF_URL`, or
  `CSRF_TRUSTED_ORIGINS` itself).
- **`DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`** from the
  environment, with development defaults. Set a real secret key before you
  share the app.
- **A `notes` app** with its migration, an admin page and a front page that
  says which database it is on.

## Deploy it on Uppcoder (free plan)

[Uppcoder](https://portal.uppcoder.com/developers?utm_source=github&utm_medium=repo&utm_campaign=django-starter)
runs it on its own HTTPS address with a real PostgreSQL database and VS Code in
the browser beside it.

Press the button above: it opens Uppcoder's deploy page with this starter and PostgreSQL filled in. New to Uppcoder? Sign up there, confirm your email, and start the free plan (Spark) in one click on the same page. Once it is deployed, run the two commands in step 5. Or set it up by hand:

1. Sign up at portal.uppcoder.com, confirm your email, then Billing, Spark, Start free.
2. Stacks, Create, Blank stack. Pick **Django**, then add **PostgreSQL**: it is
   connected to the app automatically. On the Django card, fill in an admin
   username, password and email.
3. On the Django card, under Git repository, paste
   `https://github.com/websson/django-postgresql-starter` (branch `main`).
4. Deploy. Uppcoder clones the repository, sets the `POSTGRES_*` variables and
   installs the PostgreSQL driver.
5. Open the web terminal on the stack page and create the tables and the admin
   user (it takes the username, password and email you typed on the card):

   ```bash
   pixi run -e web-django python manage.py migrate
   pixi run -e web-django python manage.py createsuperuser --noinput
   ```

   (`pixi run -e web-django` runs them in the app's own Python environment; a
   plain `python` in the terminal is a different one, without Django.)

6. Open the app's address: the front page says `postgresql`. Sign in at `/admin/`.

The full walk-through, with pictures:
[Deploy a Django app with PostgreSQL, free](https://portal.uppcoder.com/guides/deploy-django-postgresql?utm_source=github&utm_medium=repo&utm_campaign=django-starter).

To start from your own copy, fork this repository first and paste your fork's
address instead.

## Run it on your own machine

With Docker:

```bash
docker compose up
```

Then open http://localhost:8000. Compose starts PostgreSQL 16 beside the app
and runs the migrations. For the admin:
`docker compose exec app python manage.py createsuperuser`.

Without Docker it runs on SQLite:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

MIT licensed. Made by [WEBSSON](https://github.com/websson).
