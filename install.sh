#!/bin/sh
docker compose up -d
xargs brew install < brew.txt
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd terraform && tflocal init
zip ../lambda.zip ../lambda/*
tflocal plan && tflocal apply --auto-approve