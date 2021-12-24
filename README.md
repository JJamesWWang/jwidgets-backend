# JWidgets

## Build

1. Install Python 3.10
2. Set up virtual environment: `virtualenv -p /usr/bin/python3.10 venv
3. Activate venv: `source venv/bin/activate`
4. Upgrade pip: `curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10`
5. Install reqs: `pip install -r requirements.txt`
6. Install postgres: `sudo apt install postgresql`
7. Start postgres: `sudo service postgresql start`
8. Create database:
    * `sudo -i -u postgres`
    * `psql postgres`
    * `CREATE DATABASE jwidgets;`
    * `CREATE USER username WITH PASSWORD 'password'`
    * `GRANT ALL PRIVILEGES ON DATABASE jwidgets TO username`
    * `\q`
    * `exit`
9. Apply migrations `python manage.py migrate`
10. Start server: `python manage.py runserver`
