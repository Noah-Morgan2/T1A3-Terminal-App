#!/bin/bash


python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
pip3 install emojis
python3 contact_book.py