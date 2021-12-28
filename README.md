# JWidgets

## Build

To build, run `docker-compose up`.
Use the docker extension by Microsoft to enter the `jwidgets` container and run `python
manage.py migrate`.

### Set Up Local Python Venv For Development
1. Install Python 3.9
2. Set up virtual environment: `virtualenv -p /usr/bin/python3.9 venv
3. Activate venv: `source venv/bin/activate`
4. Install reqs: `pip install -r requirements.txt`
5. Set the venv as the one to use in VSCode.
