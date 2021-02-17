# django-react-template-app
workbench for https://youtube.com/playlist?list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j

# Notes 

## Initial Setup 

### VSCode Setup
- Install VSCode
- Install VSCode extensions 
    - JS Extension
    - Python Extension 
    - React Extension 
    - Prettier Extension


# Server Setup
## Virtual Environment

- `python3 -m venv venv`
- `source venv/bin/activate`

## Install Django and Django Rest Framework 

- `pip install django djangorestframework`

## Init Django Project and Create API app

- `django-admin startproject music_controller`
- `cd music_controller/ && django-admin startapp api`

## Register apps in `settings.py`

```python
INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'rest_framework',
    ...
]
```
## Initialize Model 

- see the `api/models.py` file

### Make Migrations and Migrate

- `python manage.py makemigrations`
- `python manage.py migrate`


## Create Serializer and urls.py`

- create `serializers.py` file 
- setup `urls.py` file

## Setup the view for the URL

- setup `views.py` file

# Client Setup 

- create app called `frontend` in django 
    - `cd music_controller/frontend/`

- `npm init -y`

- `npm install webpack webpack-cli --save-dev`

- `npm install @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev`

- `npm install react react-dom --save-dev`

- `npm install @material-ui/core`

- `npm install @babel/plugin-proposal-class-properties`

- `npm install react-router-dom --save` 

- `npm install @material-ui/icons`

## create files and populate

- `babel.config.json`
- `webpack.config.js` 


### configure `package.json`

- add the following scripts 
    ```
    "dev": "webpack --mode development --watch",
    "build": "webpack --mode production"
    ```

# Start Server

- `python manage.py runserver`

- `npm run dev`
