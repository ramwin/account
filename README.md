# django-account
provide many customer user related view

# Warning
You should clone this project in your project so that you can change the source code whatever your want.

# Usage
1. clone project
```
git clone git@github.com:ramwin/django-account.git /tmp/django-account
cd <your project directory>
mv /tmp/django-account/account ./  # mv the account app to your project
```

2. change settings
```
// <project directory>/<project name>/settings.py
INSTALLED_APPS = [
    ...
    "account",
]

AUTH_USER_MODEL = "account.User"
```
