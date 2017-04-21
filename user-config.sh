#!/bin/bash -x

# sudo pip3 install virtualenvwrapper

# load virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=/vagrant
export VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
source /usr/local/bin/virtualenvwrapper.sh

# create virtual environment
mkvirtualenv -a $HOME questgen
workon questgen

# add to .bashrc to automatically enter virtual environment
echo export WORKON_HOME=$HOME/.virtualenvs >> $HOME/.bashrc
echo export PROJECT_HOME=/vagrant >> $HOME/.bashrc
echo export VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3' >> $HOME/.bashrc
echo source /usr/local/bin/virtualenvwrapper.sh >> $HOME/.bashrc
echo workon questgen >> $HOME/.bashrc

pip install -r /vagrant/requirements.txt

# Set default directory to Django project folder
echo cd /vagrant/questgen/ >> $HOME/.bashrc

# Start the django server automatically
echo screen python /vagrant/questgen/manage.py runserver 0.0.0.0:8000 >> $HOME/.bashrc
echo ^ad

# Set alias for django command
echo alias django='python /vagrant/questgen/manage.py' >> $HOME/.bashrc
