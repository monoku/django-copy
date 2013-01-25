# Django Copy

Django-Copy is a copy manager, developed to easyly input and assign copy data in the django templates.

# Usage

## Install the app in django

First you should install the latest version of Django-Copy, we recommend make it using PIP:

```shell
pip install -e git+https://github.com/monoku/django-copy.git#egg=django-copy
```

## Add the app to your settings and sync

```python
INSTALLED_APPS = (
    ...
    'kopy',
    ...
)
```

 and then...

```shell
./manage.py syncdb
./manage.py migrate
```

We encourage you to use [South](http://south.aeracode.org/).


## Import the app into your template

```django
{% load copy %}
```

## Use it

```
{% copy 'key-name' [ default='html text' ] %}
```

The default param is optional, here is an example of the usage:

```django
{% copy 'key-name' default='the default value that will be assigned in the database if empty' %}
```


# License

Copyright [2011] [monoku and developers in AUTHORS FILE]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.