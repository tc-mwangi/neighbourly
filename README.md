# neighbourly

**neighbourly** An web application to know what's happening in your neighbourhood and find local businesses.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Installation
OS X

### Pre-requisites
* [Python 3](https://www.python.org/)
* [Django version 1.11.17](https://www.djangoproject.com/download/)
* IDE of your choice.


### Steps

* Clone the app to a directory.
```
git clone https://github.com/tc-mwangi/tuzwa-app.git
```

* Build Locally

```
$ python -m venv virtual
$ source virtual/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```

* Serve

```
Then visit http://localhost:8000 to view the app. 
```


### User Stories

* **As a User** I would like to:

* Post a project to be reviewed/rated.
* View posted projects details.
* Search for projects.
* View Projects Overall Score.
* Rate/Review Projects.
* View User Profile Page


### BDD
|     | Behaviour    |          Input                | Output    | 
|--- | ---         |     ---      |          --- |
|  1. | login registered User |  display login form   | redirect user to their profile page  |
|  2. | sign up new User | display sign up form   | save user details, redirect to signup, redirect to login after signup |
|  3. | enable image uploads |  display image uploads form  |  save, display image on user's timeline and also on timeline  |
|  4. | enable profile photo upload | display upload form|  redirect to profile page after post |
|  5. | follow or unfolow other users |  display navigation options to view followers and following  | add or subtract to number of followers, diplay following  posts on users timeline  |
|  6. | like a post |  display like button  | add or subtract to likes counter |
|  7. | comment on a post |  display comment form  | display comment feed  |


## Authors

* **Lose Mwangi** - *Initial work* - [archigram](https://github.com/tc-mwangi/tuzwa-app.git)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details