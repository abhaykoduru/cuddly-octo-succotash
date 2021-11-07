# cuddly-octo-succotash

## Quickstart
TBD

## Project requirements

* Support multi-tenancy.
* Support 2 kinds of files:
    * Security documents - will have title and content
    * Security questionnaires - will have question and answer pairs.
* 2 kinds of users
    * Application users who can:
        * upload files
    * Admin users who can:
        * Add question and answer pairs.
        * Search on titles of security documents.
        * Search on question-answer pairs of security questionnaires.
* Script for creating batch users?

## Assumptions and limitations of this project

* This project uses PostgreSQL as the database which is a SQL databse. So, files uploaded should conform to the respective db schema.
* Currently, this supports .csv files only.
* Implements psuedo-multitenancy which gives access to records created by the requesting user only. Although, admin users will be able to access all records.

## Todo

* [x] Setup database (PostgreSQL, AWS)
* [x] Setup Django app
* [x] Connection to database
* [x] Create django models
    * [x] User
    * [x] Documentx
    * [x] Questionnaire
* [ ] Add APIs
    * [x] Authentication
    * [ ] File upload
    * [ ] Document search on title
    * [ ] Questionnaire search on q & a
* [ ] Add unit tests
* [ ] Add UI pages
    * [ ] Login page
    * [ ] Upload page
    * [ ] See uploaded documents?
    * [ ] Use django admin for admin users? With less than admin level perms?
