# Script for LG Phones

Simple script to reboot LG Phones

## Installation

You need python3 and pipenv, install this tools via your favorite way.

```shell
git clone https://github.com/alkivi-sas/python-lg-phones
cd python-lg-phones
pipenv install
pipenv shell
```

## Usage

Once in your pipenv shell

```shell
./phones.py --help
Usage: phones.py [OPTIONS]

  Script to reboot phone.

Options:
  --user TEXT      User to log in.
  --password TEXT  Password for user.
  --ip TEXT        IP of the phone.
  --help           Show this message and exit.
```
