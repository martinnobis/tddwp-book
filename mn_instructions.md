# Simple instructions
To work on the virtualenv:
$ workon superlists

To deactivate:
$ deactivate

To run the server (required for the tests):
$ python manage.py runserver

To run the functional test:
$ python manage.py test functional_test/

To run the unit test (it automatically creates a new test database):
$ python manage.py test

To create the database table (for development purposes):
$ rm db.sqlite3
$ python manage.py makemigrations

To create the production database:
$ python manage.py migrate

=======================

## 5/11/2017:
Finished chapter 4. Start chapter 5 next time.

## 07/11/2017:
Half way through chapter 5, see lists/tests.py change with ItemModelTest

## 12/11/2017
5/6s down the page on chapter 5. Search for 'will the functional test pass?'.

## 13/11/2017 
Start of chapter 7.

## 16/11/2017
2/3 into chapter 7, search for 'Green? Refactor'

## 25/11/2017
Search for Oh dear! in chapter 7

## 1/12/2017
In chapter 7, search for:
HOORAY! Oh, and a quick check on our to-do list:

## 6/12/2017
Chapter 8, search for:
A Few Things That Didn’t Make It

## 14/12/2017
Chapter 13, search for:
def test_validation_errors