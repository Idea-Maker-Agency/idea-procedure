# Running a project on heroku

##Step 1: Create requirements file
We typically have our requirements in a directory `requirements/`  
I created a file `heroku.txt` with the following:
```
-r base.txt
gunicorn
django-heroku
whitenoise
```

## Step 2: Add top level requirements.txt
Heroku expects a `requirements.txt` at the top level so lets create it.  
In that file I put:  
`-r requirements/heroku.txt`

## Step 3: Create a settings file
Heroku needs its own settings because we are now using [whitenoise](https://github.com/evansd/whitenoise) and [django_heroku](https://github.com/heroku/django-heroku).

```
heroku_settings.py  -

(at top)
import django_heroku
MIDDLEWARE = MIDDLEWARE + ['whitenoise.middleware.WhiteNoiseMiddleware',]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

(at bottom)
django_heroku.settings(locals())
```
For more information you can read the docs for [django_heroku](https://github.com/heroku/django-heroku)

## Step 4: Create a Procfile
Heroku needs a procfile at top level.  

*Note*: the collectstatic command is optional.  
Heroku will automatically run collectstatic. However, in some cases the post processing will fail and block your 
deployment.
```
web: gunicorn --pythonpath project  project.wsgi
release: python manage.py migrate --noinput
release: python manage.py collectstatic --no-post-process --noinput
release: python manage.py loaddata any_fixtures.json
```

## Step 5: Heroku - Add postgres 
Go to Add Resources and select Postgres

(this will automatically populate in your config variables)  which will look like this:
`DATABASE_URL = postgres://wlkdflsdf:3838.... `

## Step 6: Heroku - Add configuration variables as needed
Click on Settings and then config vars
DJANGO_SETTINGS_MODULE - project.setting.heroku_settings
EMAIL_HOST_PASSWORD - some-password  
DISABLE_COLLECTSTATIC - 1 (optional)

## Step 7: Heroku - set buildpack
You need to tell Heroku you are running a python project.
Click on Settings and Buildpacks  
Choose python

## Done!
