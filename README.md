# shopping-project

Simple shopping website based on django & vue

## Technologies used in this project:

- Python 3.x

  - Django 3.2

    - Djangorestframework

- Javascript

  - Vue JS
  
  - Vue CLI
  
  - Vue router
  
  - Vue x

- HTML 5

- CSS 3

- Bootstrap 5.1

- JWT

- Axios



## 1. First clone or download this project:
```
$ git clone https://github.com/AminMehri/shopping-project.git
```

## 3. create a virtualenv in backend with The following command:
```
$ virtualenv venv 

$ sourse venv/bin/activate
```

## 4. when active virtual environment, install the project requirements:
```
$ pip install -r requirement.txt
```

## 5. Migrations:
```
$ python manage.py makemigrations

$ python manage.py migrate
```

## 6. RUN:
```
$ python manage.py runserver
```


## 7. in frontend
```
$ npm i (or npm install)

$ npm run serve
```

You may need to add your frontend localhost address to crosheaders in settings.py.

If your django localhost address different as http://127.0.0.1:8000 , you need to change the axios requests address in all vue components.

You did it. congratulations
