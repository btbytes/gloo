# Gloo

Gloo wants to be a Really Good paste.

## Requirements

 * Python 2.4 and above
 * [web.py 0.3](https://code.launchpad.net/~anandology/webpy/webpy.dev)

## Install

 1. Create tables in the database of your choice using setup.sql. _Note_: Given SQL works on MySQL.
 2. Change the values for `db`, `user`, and `passwd` in settings.py accordingly.

## Running

Run `webapp.py` from console; `$ python webapp.py`
Access the application on [http://localhost:8080](http://localhost:8080)

##  FAQ

1. How to I run the app on a different port, say on 8090?
> `$ python webapp.py 8090`
