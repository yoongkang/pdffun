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

# Comments

In this repository, I sent the image as a base64 encoded string. Don't do this.

A better idea would be to send it as a `Blob`. Do that instead.

I'm going to make changes to this repository soon to use `Blob`.
