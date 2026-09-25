# CareConnect

CareConnect is a small healthcare support concept for a community NGO. People can send a support request, register their interest in volunteering, and see a simple count of submissions on the dashboard.

## Tech stack

- Python and Flask for the web app
- SQLite for the form submissions
- HTML, CSS, and plain JavaScript for the pages

## FAQ idea

The FAQ helper uses a few keyword checks to answer common questions about support and volunteering. It is a small automation example, not a connected AI model. It can work without an external service and points people to the right form when it does not know an answer.

## Run locally

1. Install Python 3.10 or later.
2. Install dependencies with `pip install -r requirements.txt`.
3. Start the app with `python app.py`.
4. Open `http://127.0.0.1:5000` in a browser.

The SQLite database is created automatically next to `app.py`. The dashboard is available at `/dashboard`.

## Hosting

This Flask app can be deployed as a Render Web Service. Connect the GitHub repository, use `pip install -r requirements.txt` as the build command, and `gunicorn app:app` as the start command. The sample uses a local SQLite file, so check the hosting service's storage settings if you need submissions to remain after a redeploy.

Live app: _Add the hosted URL after deployment._

## Use case and scope

An NGO team could use the forms to collect requests and volunteer interest, then use the dashboard for a quick overview. This is a student prototype: it does not provide medical advice, verify submissions, or protect a real patient record system. Avoid entering sensitive health details.
