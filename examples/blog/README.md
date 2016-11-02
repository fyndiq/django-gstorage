# An example blog

An example project using django-gstorage to save files
to Google cloud.

## Setting up Google cloud

* Create a bucket in Google cloud storage - https://console.cloud.google.com/storage/
* Add the service account as a user to the bucket with
  write permissions
* Create a .env in the current folder with the required settings. For example

```
GOOGLE_APPLICATION_CREDENTIALS=/Users/pcaulagi/src/django-gstorage/examples/blog/dev-f6e3f07b7da8.json
GCLOUD_PROJECT_NAME=pcaulagi
GCLOUD_DEFAULT_BUCKET_NAME=test-bucket
```

## Setting up project

```
$ virtualenv /tmp/blog
$ . /tmp/blog/bin/activate
$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py createsuperuser

$ python manage.py runserver
```

Go to [admin](http://localhost:8000/admin) and create some pages.
Check the images appear on Google cloud. Also see the blog locally
referencing files on Google - http://localhost:8000
