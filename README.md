# Tornado-Example-Blog
An example blog built from Python Tornado.

Tornado is a webserver and asynchronous network library built in Python.

This is a very simple blog that is created to explore some of functionality that Tornado offers.
It doesn't go in-depth (posts are stored in memory, not in a database, for example), but it does implement templating (with extend and include), a basic CRUD model, and a basic MVC pattern.

After installing Python, Tornado, and the Tornado Prerequisites (see http://www.tornadoweb.org/en/stable/), simply go to the project root directory, run `python App.py` (assuming python is in your PATH variable), and the Tornado server will start listening to localhost port 8888 and you can view the results by visiting http://localhost:8888/ in your browser.

The aim of this project is to get something basic working, and to document it well. It might not do everything exactly right, but the it definitely works.

Built in Python 2.7.11, but it should work in any version supported by Tornado.
