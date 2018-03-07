# SyDjango Mar 2018 -- PDF Fun

This is a repo I created for a presentation I gave at SyDjango Mar 2018 about
my experience with fillable PDF forms.


# Requirements

Please install pdftk: https://www.pdflabs.com/tools/pdftk-server/

If you are on a Mac, this is probably just `brew install pdftk`

# Installation

Make sure you have Pipenv installed, then run the following commands:

```
$ pipenv install
$ pipenv run python manage.py migrate
$ pipenv run python manage.py runserver
```

You should be able to access the server on http://localhost:8000/

