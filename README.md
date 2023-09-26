# Demo Polls Application

## Description
This repo is intended for testing purposes.

## Getting started

Copying the repository

Before proceeding be aware that this exercise assumes you are using a linux machine with [pip](https://pip.pypa.io/en/stable) and [venv](https://docs.python.org/3/library/venv.html) installed.

To initialize the repository in your base directory execute ./initialize_repo.sh

To start the webserver locally, in your base directory execute ./run-server.sh

To run tests locally, in your base directory execute ./run-tests.sh

Access the application at http://localhost:8000
Login credentials have been shared with you via email

## Models description
The application uses 6 models
1. django.contrib.auth.models.User - stores user details and is an inbuilt Django model provided by the authentication system
2. polls.Site - stores details about a tenant
3. polls.Profile - stores additional details for a user. Users can have extra fields and these fields vary for every site based on the profile form. This model refers the _ProfilForm_ and _Site_ model
4. polls.ProfileForm - Each site can have their own profile form and this model stores the fields for the profile forms. This model has a reference to a _Site_.
5. polls.Poll - stores the question for the poll.
6. polls.Answer - stores answers to the poll and the user who provided the answer. This model has a reference to the _Poll_ and _User_ model.

## Exercise
We're going to have a Migrations Workshop.  

## Exercise Methodology  
**Teams**
You will be split into teams, each consisting of two members. 

**Migration Tasks**
During our upcoming session, you will receive your specific migration tasks. Each team will be responsible for implementing and completing their assigned migrations in separate branches.


If you have any questions or require assistance before the session, please do not hesitate to reach out. Please come prepared for the session, and let's make it a productive experience.  
