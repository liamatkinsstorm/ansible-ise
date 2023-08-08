#!/bin/bash

#sudo apt update 
#sudo apt upgrade
#sudo apt -y install python3-pip
#sudo apt -y install virtualenv
#sudo apt install python3-venv

python3 -m venv /home/liam/Documents/venv # Creates a directory named 'venv' in the current directory, which contains pip, interpreter, scripts, and libraries.
source /home/liam/Documents/venv/bin/activate

pip install -r /home/liam/GitRepo/ansible-ise-1/requirements.txt  # install required Python packages

#deactivate