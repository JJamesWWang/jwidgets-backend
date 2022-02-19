# JWidgets

### Build
1. Install Python 3.10.2
2. Set up virtual environment: `virtualenv -p /usr/bin/python3.10 venv
3. Activate venv: `source venv/bin/activate`
4. Install reqs: `pip install -r requirements.txt`
5. Migrate db: `python manage.py makemigrations && python manage.py migrate`
6. Start server: `python manage.py runserver`

When run locally, it uses SQLite3, but deployment on Heroku via Docker uses Postgres.
