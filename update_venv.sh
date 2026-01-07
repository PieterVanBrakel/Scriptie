#!/bin/bash
# update_venv.sh — update de virtuele omgeving

# 1️⃣ Activeer venv
source .venv/bin/activate

# 2️⃣ Upgrade pip en pip-tools
python -m pip install --upgrade pip
python -m pip install --upgrade pip-tools

# 3️⃣ Compileer requirements.in naar requirements.txt
pip-compile --upgrade --output-file requirements.txt requirements.in

# 4️⃣ Installeer alles uit requirements.txt
python -m pip install --upgrade -r requirements.txt

echo "✅ Virtuele omgeving bijgewerkt!"
