#!/usr/bin/env python
import requests
import click
import logging

from alkivi.logger import Logger
from requests.auth import HTTPDigestAuth

# Define the global logger
logger = Logger(min_log_level_to_mail=None,
                min_log_level_to_save=None,
                min_log_level_to_print=logging.DEBUG)

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


@click.command()
@click.option('--user', default='private', help='User to log in.')
@click.option('--password', default='lip', help='Password for user.')
@click.option('--ip', prompt='Switch IP', help='IP of the phone.')
def reboot(user, password, ip):
    """Script to reboot phone."""

    # Global session
    s = requests.Session()

    # Auth
    auth = HTTPDigestAuth(user, password)

    # Url
    reboot_url = 'http://{0}:8000/goform/setReboot'.format(ip)
    data = {
        'reboot_btn': 'Reboot'
    }
    s.post(reboot_url, data=data, auth=auth)


if __name__ == '__main__':
    reboot()
