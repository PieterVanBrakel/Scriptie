#!/bin/bash
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pip-tools
pip-compile requirements.in
python -m pip install -r requirements.txt --upgrade
echo "Virtuele omgeving bijgewerkt!"