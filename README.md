# django-users

## Specification:

The task is made up of 5 parts plus an optional task.
1. Set up a basic (latest or LTS) Django installation
2. Extend the User model to have (yes, custom user model is the way to go):
   1. birthday field of type date
   2. random number field of type integer that is assigned a value from 1-100 on creation
   3. Do the changes in user model in a few steps - we want you to use schema migrations here
3. Create views for: list of all users, viewing, adding, editing and deleting a single user
4. Create two template tags:
   1. A tag that will display "allowed" if the user is > 13 years old otherwise display
   "blocked"
   2. A tag that will display the BizzFuzz result of the random number that was generated for the user. The BizzFuzz specification is that for multiples of three print "Bizz" instead of the number and for the multiples of five print "Fuzz". For numbers which are multiples of both three and five print "BizzFuzz"
   3. Add a column to the list view after the birthday column that uses the allowed/blocked tag
   4. Add a column to the list view after the random number column that uses the BizzFuzz tag
5. Unit test what you feel is appropriate to test.
6. Create a download link on the list view. The link would return the list of results in Excel's format (csv format is ok).

   **Sample Output:**

   | Username | Birthday | Eligible | Random Number | BizzFuzz |
   |----------|----------|----------|---------------|----------|
   | user1 | 1/1/2013 | blocked | 40 | Fuzz |
   | user2 | 11/4/1975 | allowed | 66 | Bizz |
   | user3 | 7/30/2010 | blocked | 51 | 51 |
   | user4 | 6/16/1968 | allowed | 30 | BizzFuzz |

[![codecov](https://codecov.io/gh/dzbrozek/django-users/branch/main/graph/badge.svg?token=Y06p3pzdwL)](https://codecov.io/gh/dzbrozek/django-users)


### Development

#### Requirements

This app is using Docker so make sure you have both: [Docker](https://docs.docker.com/install/)
and [Docker Compose](https://docs.docker.com/compose/install/)

#### Prepare env variables

Copy env variables from the template

```
cp .env.template .env
```

#### Build and bootstrap the app

```
make build
make bootstrap
```

Once it's done the app should be up app and running. You can verify that visiting [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

#### Running

Next time you want to start or stop the app use `up` or `down` command.

```
make up
```

```
make down
```

#### Users

Test users created during bootstrapping the project.

| Login    | Password | Superuser |
|----------|----------|-----------|
| demo     | password | yes       |

### Tests

To run tests use the `make test` command

### Local development

Read more about [local development](./docs/DEV.md)
