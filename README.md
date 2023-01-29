# Job Connect API
Job Connect API is the backend service used by the [Job Connect App](https://github.com/ssmi8/job_connect)

## Table of Contents

- [Development Goals](#development-goals)
- [Agile Planning](#agile-planning)
    - [Epics](#epics)
    - [User Stories](#user-stories)
- [API End Points](#api-endpoints)
- [Security](#security)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
    - [Version Conrol](#version-control)
    - [Heroku Deployment](#heroku-deployment)

## Development Goals

The goal of this API is to provide a backend sevice to all the Job Connect front end application to perform, create, read, update and delete operations vias the user interface.


## Agile Planning

This project was developed using agile methodologies by delivering small features in incremental sprints.  There were 3 sprints in total.

All stories were laid out at the beginning of the project, as these were the key elements to implement.  Throughout the process some user stories were added as the project developed.

The Kanban board was created using github projects and can be located [here](https://github.com/users/ssmi8/projects/3).

## Epics
### Set Up

This Epic covers all the initial setup of the Django application and Django REST Framework in order to begin coding the features.

### Posts

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of user posts. This includes like activity.

### Comments

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of user comments in relation to posts.

### Profiles

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of user created profiles. This includes following functionality.

### Skills

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of user skill posts.

### Jobs

This Epic covers all API endpoint creation and database connections relating to the CRUD functionality of user job posts.


## User Stories

### Setup

- As a developer, I need to create the base project set up so that I can build out the features.
- As a developer, I need to create the cloudinary bucket and create the connection to the project so static image can be uploaded.
- As a user I can create a new account so that I can access all the features for signed up users.

### Posts

- As a user, I want to be able to be able to view, edit or delete a post
- As a user, I want to be able to get a list of profiles

### Profiles

- As a developer, I want to create a new blank profile with default image, when a user is created.
- As a user, I want to be able to get a list of profiles.

## API Endpoints

User Story:

- As a developer, I need to create the base project set up so that I can build out the features.

Implementation:

The base project was created and a virtual environment created with all neccessary packages installed and frozen into the requirements.

The settings were also edited to hide any secret variables and set dev and production environments apart.

User Story:

- As a developer, I need to create a cloudinary account and create the connection to the project so that static images can be uploaded by users.

Implementation:

A cloudinary account was used  and a service account created to allow image uploads via the service account.

User Story:

- As a user I can create a new account so that I can access all the features for signed up users

Implementation:

Django rest framework and dj_rest_auth were installed and added to the url patterns and site packages to make use of their built in authentication system.

User Story:

- As a developer, I want to create a job model and API view so that users can create job postings

Implementation:

Endpoint: /jobs/

Methods:

POST - Used to create job post
GET - Used to get a list of job postings
Endpoint: /jobs/int:pk/

Methods:

GET - Get a single job request
PUT - Used to update a single job request
DELETE - Used to delete a job request

- As a developer, I want to create a skill model and API view so that users can create skill postings

Implementation:

Endpoint: /skills/

Methods:

POST - Used to create skill post
GET - Used to get a list of skill postings
Endpoint: /skills/int:pk/

Methods:

GET - Get a single skill request
PUT - Used to update a single skill request
DELETE - Used to delete a skill request

User Story:

- As a user, I want to be able to view edit or delete a post

- As a user, I want to able to create a post and list posts

Implementation:

Endpoint: /posts/

Methods:

POST - Used to create post
GET - Used to get a list of posts
Endpoint: /posts/int:pk/

Methods:

GET - Get a single post
PUT - Used to update a single post
DELETE - Used to delete a post
User Story:

- As a developer, I want to create a new blank profile with default image when a user is created.

Implementation:

In the profiles app, a signal was created in order to create a new user profile on signup.

User Story:

- As a user, I want to able to get a list of profiles

Implementation:

Endpoint: /profiles/

Methods:

POST - Used to create post
GET - Used to get a list of posts
Endpoint: /profiles/int:pk/

Methods:

GET - Get a single profile
PUT - Used to update a single profile
DELETE - Used to delete a profile


## Security

A permissions class was added called IsOwnerOrReadOnly to ensure only users who create the content are able to edit or delete it.

## Technologies used

- Django
    - Main framework used for application creation
- Django REST Framework
    - Framework used for creating API
- Cloudinary Platform
    - Used for static image hosting
- Heroku
    - Used for hosting the application
- Git
    - Used for version control
- Github
    - Repository for storing code base and docs

## Python Packages

Details of packages:

- cloudinary==1.30.0
    - Used to store static images
- dj-database-url==0.5.0
    - Used to parse the DATABASE_URL connection settings
dj-rest-auth==2.2.6
- Django==3.2.16
    - Main framework used to start the project
- django-allauth==0.50.0
    - Used for authentication
- django-cloudinary-storage==0.3.0
    - Used to help connect with the google cloud storage bucket
- django-cors-headers==3.13.0
    - Used for Cross-Origin Resource Sharing (CORS) headers to responses
- django-filter==22.1
    - Used to filter API results in serializers
- djangorestframework==3.14.0
    - Framework used to build the API endpoints
- djangorestframework-simplejwt==5.2.2
    - Used with django rest framework to create access tokens for authentication
- gunicorn==20.1.0
    - Used for deployment of WSGI applications
- Pillow==9.4.0
    - Imaging Libray - used for image uploading
- psycopg2==2.9.5
    - PostgreSQL database adapter to allow deployed application to perform crud on the postgresql db
- PyJWT==2.6.0
    - For creating the Python Json Web Tokens for authentication


## Testing

Unit tests in posts app
![test](/documentation/test.png "test")

The API's were tested locally during development but the core testing was done as part of the front end repos and testing to the real API's manually via form inputs and page loads.

### Validator Results

All folders were run through flake8. Several issues appeared with various reasons, lines too long, blank spaces, indentation and docstrings.

All issues were resolved with the exception of lines too long in migration files (these are auto generated so I did not fix) and the auth validator lines in the settings.py which seem to be unbreakable but are framework code.

A warning appeared for env.py being imported but unused although this is being used in the development version, so this was ignored.

![flake8](/documentation/flake8.png "flake8")

## Bugs and their fixes

A bug occured causing which would not allow me to access the JobsList but after a call with tutor support, I have not define the JobsList correctly, which was then corrected.

## Deployment

### Version Control

he site was created using the gitpod workspace and pushed to github.

The following git commands were used throughout development to push code to the remote repo:

git add <file> - This command was used to add the file(s) to the staging area before they are committed.

git commit -m “commit message” - This command was used to commit changes to the local repository queue ready for the final step.

git push - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account

- Click the new button in the top right corner

- Select create new app

- Enter app name

- Select region and click create app

- Click the resources tab and search for Heroku Postgres

- Select hobby dev and continue

- Go to the settings tab and then click reveal config vars

- Add the following config vars:

    - SECRET_KEY: (Your secret key)
    - DATABASE_URL: (This should already exist)
    - ALLOWED_HOST:
    - CLIENT_ORIGIN: url for the client front end react application that wil be making requests to these APIs
    - CLIENT_ORIGIN_DEV: address of the local server used to preview and test UI during development of the front end client application
    - CLOUDINARY_URL: name of the bucket to upload images to.

- Click the deploy tab

- Scroll down to Connect to GitHub and sign in / authorize when prompted

- In the search box, find the repositoy you want to deploy and click connect

- Scroll down to Manual deploy and choose the main branch

- Click deploy
