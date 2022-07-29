# Blogpost
first blog Api with comment
This project make it possible for post blog and also comment on blog post only. list,create,update,delete .

# Setup and Installation
*Note**: Make sure to download/clone this repository and navigate to the folder in your terminal. Now follow the instructions below

Create the virtual environment.
virtualenv /path/to/venv --python=/path/to/python3
You can find out the path to your python3 interpreter with the command which python3.

Set up .env file by duplicating the .env file(and editing if required).

Activate the environment and install dependencies.

Linux
source /path/to/venv/bin/activate
pip install -r requirements.txt

Windows
./path/to/venv/bin/activate
pip install -r requirements.txt
Launch the app
# Documenation
https://blogpostapi1.herokuapp.com/docs#/

python manage.py runserver localhost:8000

# Prerequisites

Python 3.10.4 Download
fastapi
Heroku Account Signup
A working fastapi Project. If you don't have one you can clone this
virtualenv or an alternative

# REFERENCES

anyio==3.6.1
asgiref==3.5.2
click==8.1.3
colorama==0.4.4
dnspython==2.2.1
fastapi==0.78.0
gunicorn==20.1.0
h11==0.13.0
idna==3.3
pydantic==1.9.1
pymongo==4.1.1
sniffio==1.2.0
starlette==0.19.1
typing_extensions==4.2.0
uvicorn==0.17.6
