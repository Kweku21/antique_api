# Antique Product API Backend

### Instructions on how to execute the application
Note: Make sure you have docker installed

1. Start the Django application with Docker: `docker-compose up --build`

2. Start Database migration: `docker-compose run web python manage.py makemigrations`

3. Migrate Database Models: `docker-compose run web python manage.py migrate`

4. Application will be running on : `http://localhost:8000/ `

### Product Files

Product images have been upload and stored in media/products_pics

### Application Database

1. SQLite is the database engine for this application.
2. Data have already been populated in the database

### Front-end for this application

The front-end application for this application is [Antique Frontend](https://github.com/Kweku21/antique-ui)