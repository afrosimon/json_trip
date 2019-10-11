# JSON Trip

Simple flask app for me to create json files based on destinations I have visited in past trips.

## Developer setup

Use virtualenvwrapper to create a Python 3 environment:

```
$ cd path/to/json_trip
$ mkvirtualenv -p python3.6 json_trip
(json_trip)$ setvirtualenvproject
```

Install python dependencies:

```
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

Use these flask commands to prepare the database:

```
$ flask db init
$ flask db upgrade
```

As for the configuration, copy the .flaskenv-sample file and edit its content. And start the application:

```
$ flask run
```
