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

* [x] Setup database (PostgreSQL on local)
* [x] Setup Django app
* [x] Connection to database
* [x] Create django models
    * [x] User
    * [x] Documentx
    * [x] Questionnaire
* [x] Add APIs
    * [x] Authentication
    * [x] File upload
    * [x] Document search on title
    * [x] Questionnaire search on q & a
* [ ] Add unit tests
* [ ] Add docstrings wherever needed
* [x] Add UI pages
    * [x] Login page
    * [x] Upload page
    * [ ] See uploaded documents?
    * [ ] Use django admin for admin users? With less than admin level perms?

## Improvements

* Support multiple choice questions on Questionnaire model.
* Support for storing all uploaded files on cloud.
* Support .csv files with headers in file and decide which model to save data to at runtime.
* Add .csv file validations and raise appropriate exception when something is not right. Ex: bad file format, missing columns etc.
* Use DjangoObjectPermissions to achieve pseudo multitenancy.
* Setup multiple DBs to achieve true multi-tenancy.
    * Implement an effecient way to access multiple tenant DBs for admin users.
* Support more file formats-.docx,.xlx,.txt,.pdf-may be write a service to cleanup and convert these files to loadable .csv.
* Write a custom JSONRenderer that can be used for all JSON requests.
* Implement pagination for all list APIs.
