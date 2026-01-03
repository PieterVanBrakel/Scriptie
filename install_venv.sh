#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
echo "Virtuele omgeving klaar!"
