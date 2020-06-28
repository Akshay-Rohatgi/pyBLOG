#!/bin/bash 

cat ./pyBLOG/static/text_logo

echo "-----------------------------------"
echo "Beginning installation process now!"
echo "-----------------------------------"

apt-get update
apt-get install python3.6

pip3 install Flask
pip3 install sqlite3
pip3 install datetime
pip3 install hashlib