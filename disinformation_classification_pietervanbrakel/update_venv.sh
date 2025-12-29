#!/bin/bash
source venv/bin/activate
pip install --upgrade pip
pip-compile requirements.in
pip install -r requirements.txt --upgrade
echo "Virtuele omgeving bijgewerkt!"