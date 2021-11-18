#!/bin/sh
sudo apt install python3-venv
python3 -m venv data_collection
source data_collection/bin/activate
pip3 install -r requirements.txt
python3 collect_data.py
