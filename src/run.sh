#!/bin/bash

# check if python is installed
if [[ ! "$(python3 -V)" =~ "Python 3" ]]
then
    echo ""
    echo "[ERROR] Python 3 is not installed"
    echo ""

    exit
fi

# run the app
python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
python3 main.py