#!/bin/bash

# check if python is installed
if [[ ! "$(python3 -V)" =~ "Python 3" ]]
then
    echo ""
    echo "[ERROR] Python 3 is not installed"
    echo ""

    exit
fi

# check if the venv already exists
if python3 -m venv .venv; then
    echo "Virtual environment created successfully."
    source .venv/bin/activate
else
    echo "Error: Virtual enviroment failed to create"
fi

# run the app
pip3 install colored
python3 main.py