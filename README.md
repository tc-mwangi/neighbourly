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

* Sign in with the application
* Set up a profile with general location and neighbourhood name
* Find a listing of different businesses in my neighbourhood
* Find contact information of Police and Health services
* Create Posts visible to members of the neibourhood.
* Change Neighbourhood when I decide to move out.
* Only view details of a single neighbourhood.


### BDD
|     | Behaviour    |          Input                | Output    | 
|--- | ---         |     ---      |          --- |
|  1. | login registered User |  display login form   | redirect user to their profile page  |
|  2. | sign up new User | display sign up form   | save user details, redirect to signup, redirect to login after signup |
|  3. | enable edit profile |  display edit profile form  |  save, display changes on user's profile page and also on timeline  |
|  4. | see listing of neighbourhood businesses| |  display list of businesses and their contact details |
|  5. | post on the neighbourhood thread |  display post form  | update neighbourhood thread |



## Authors

* **Lose Mwangi** - *Initial work* - [archigram](https://github.com/tc-mwangi/tuzwa-app.git)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details