import argparse
from os import environ

from sqlalchemy import create_engine
from sqlalchemy import text


__author__ = 'fegger@ducksify.com'

BASEDIR = environ.get('BASEDIR')  or "example"
CONN_URL = environ.get('CONN_URL') or "sqlite:///example/inv.db"


"""
You can set CONN_URL via 
CONN_URL = "oracle+cx_oracle://scott:tiger@hostname:port/?service_name=myservice&encoding=UTF-8&nencoding=UTF-8")
"""


class Tag:
    def __init__(self, name, cat):
        self.name = name
        self.cat = cat


class Vm:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.tags = []

    def addtag(self, ta):
        self.tags.append(ta)


def menuentry():
    parser = argparse.ArgumentParser(description='Arguments for talking to Database')

    parser.add_argument('-u', '--conn',
                        required=False,
                        action='store',
                        help='Database connection URL')


    args = parser.parse_args()

    connurl = CONN_URL
    if args.conn:
        connurl = args.conn

    cathosts = {}
    engine = create_engine(connurl)
    with engine.connect() as connection:
        inventory = connection.execute(text("select * from inventory"))
        for vm in inventory:
            env = vm['env']
            service = vm['service'] or 'NA'
            app = vm['app']
            host = vm['host']
            if env not in cathosts:
                cathosts[env] = {}
            if service not in cathosts[env]:
                cathosts[env][service] = {}
            if app not in cathosts[env][service]:
                cathosts[env][service][app] = []

            cathosts[env][service][app].append(host)

    hostcount = 0

    # create ansible host inventory

    for env, services in cathosts.items():
        with open(f'{BASEDIR}/hosts{env}', 'w') as writer:
            for service, apps in services.items():
                writer.writelines(f"{service}:\n")
                writer.writelines(f"  children:\n")
                for app, hosts in apps.items():
                    writer.writelines(f"    {app}:\n")
                    hostcount += 1
                    writer.writelines(f"      hosts:\n")
                    for host in hosts:
                        writer.writelines(f"        {host}:\n")

    print(f"{hostcount} hosts written")


if __name__ == '__main__':
    menuentry()
