#!/bin/bash

cd /home/jovyan/work

echo "Cloning fractopo-help repository"
git clone https://github.com/nialov/fractopo-help.git

echo "Copying network.ipynb notebook to current directory"
cp fractopo-help/network.ipynb .

echo "Upgrading pip"
pip install --upgrade pip

echo "Installing fractopo==0.2.1"
pip install fractopo==0.2.1
