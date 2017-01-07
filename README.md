cython-post
===========

This repo contains the sources used to demonstrate what happens
when playing with cython and dangling pointers while wrapping c code
that stores pointers to python objects.

Please have a look at this [little post](https://francesco.pischedda.info/posts/cython-and-c-pointers/) about the problem.

This repo contains:
* cytest.pyx : the cython code that generates the c code that stores the pointers
* segfault.py : a script that triggers a segmentation fault
* overwrite.py : a script that shows how some memory can be overwritten in a non obvious way

How to setup the environment
----------------------------

The steps to setup the working environment are:
- create a virtualenv and activate it
- install requirements with pip install -r requirements.txt
- run python setup.py install to install the extension in the venv

To run the samples just run those scripts in the venv created in the setup phase.
