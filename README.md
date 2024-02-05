# django_blog

## Prerequisites

- Python >= 3.10.5
- Django >= 5.0.1

## Installation

### Django installation

```bash
$ pip install django
```

## Run Web application

### Start Django server
``` bash
$ python manage.py migrate
$ python manage.py createsuperuser
ユーザー名 (leave blank to use 'kurosaki'): admin
メールアドレス: kurosaki4pers@gmail.com
Password:
Password (again):
Superuser created successfully.
$ python manage.py runserver
```

## License

&copy; 2024 [Ken Kurosaki](https://github.com/quinpallet).
This project is [MIT](https://github.com/quinpallet/django_study/blob/master/LICENSE) licensed.