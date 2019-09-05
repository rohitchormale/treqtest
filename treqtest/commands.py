"""
This module implements flask-cli commands.

@author: 
"""


import click
from flask.cli import AppGroup

txtest_cli = AppGroup("treqtest")


"""
Example command

@txtest_cli.command("add-user")
@click.option("--arg1")
@click.option("--arg2")
@click.option("--arg3")
def add_user(arg1, arg2, arg3):
    print("Command executed successfully")
"""
