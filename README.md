# Ecommerce Website Project

A useful e-commerce application written in Django! It can be used as a base project for adding new applications or improving existing functionalities.


 ## Installation
 ---

Before jumping on the installation, you just have to download the repository and activate a virtual environment with the following commands:

```bash

cd ecommerce
pip install virtualenv
venv\Scripts\activate

```

In order to make this project work, you have to install the following requirements:

```bash

pip install django
pip install pillow

```

Or you can run the following command in order to directly install the required tools (Django & Pillow) within the requirements.txt file :

````bash

pip install -r requirements.txt

````

The pillow library allows to add the ImageField to this project.

Once the requirements are installed, you can run the server by using the following in-built Django command :

```bash

python manage.py runserver

```

Once the server is running, it is possible to look at the project on the browser at the following local URL: http://127.0.0.1:8000/

## Usage
---

Before making use of this project, make sure that you have some basic django knowledge as well as some JavaScript, CSS and HTML knowledge.


## License
----

[MIT License](https://github.com/anas-ecam2020/ecommerce/blob/main/LICENSE.txt)


## Main components
---

* [Models](https://github.com/anas-ecam2020/ecommerce/blob/main/store/models.py)

The creation of models allow to shape the sqlite database.

* [Urls](https://github.com/anas-ecam2020/ecommerce/blob/main/store/urls.py)

The urls allow to set the path for the each view contained in views.

* [Views](https://github.com/anas-ecam2020/ecommerce/blob/main/store/views.py)

Views contains all the functions that render the different html templates.

* [Static](https://github.com/anas-ecam2020/ecommerce/tree/main/store/static)

The store/static folder contains all the CSS, the images and the JavaScript needed for the front-end development of the project.

* [Tests](https://github.com/anas-ecam2020/ecommerce/tree/main/store/tests)

Unit Testing allows to check if some parts of the code such as the views, the urls and the models run properly.

## Author
---

Anas Rabai