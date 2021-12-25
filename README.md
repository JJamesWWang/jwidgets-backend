# JWidgets

## Build

1. Install Python 3.9
2. Set up virtual environment: `virtualenv -p /usr/bin/python3.9 venv
3. Activate venv: `source venv/bin/activate`
4. Install reqs: `pip install -r requirements.txt`
5. Install postgres: `sudo apt install postgresql`
6. Start postgres: `sudo service postgresql start`
7. Create database:
    * `sudo -i -u postgres`
    * `psql postgres`
    * `CREATE DATABASE jwidgets;`
    * `CREATE USER username WITH PASSWORD 'password'`
    * `GRANT ALL PRIVILEGES ON DATABASE jwidgets TO username`
    * `\q`
    * `exit`
8. Apply migrations `python manage.py migrate`
9. Start server: `python manage.py runserver`
