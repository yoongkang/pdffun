# SyDjango Mar 2018 -- PDF Fun

This is a repo I created for a presentation I gave at SyDjango Mar 2018 about
my experience with fillable PDF forms.

Also have a blog post on this topic: https://yoongkang.com/blog/pdf-forms-with-python/

# Requirements

Please install pdftk: https://www.pdflabs.com/tools/pdftk-server/

# Installation

Make sure you have Pipenv installed, then run the following commands:

```
$ pipenv install
$ pipenv run python manage.py migrate
$ pipenv run python manage.py runserver
```

You should be able to access the server on http://localhost:8000/

