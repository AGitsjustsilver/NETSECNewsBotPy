"""pull
Name: mysql
Author: Alessandro Guaresti
Description: 
This module is used to interact with mysql for database purposes 
regardless of databases in use for the project
"""
import os
import mysql.connector

# constants
user = os.environ.get('SQL_USER')
pswd = os.environ.get('SQL_USER_PSWD')

FEED_DB = None
ARTCL_DB = None

def create_db(name):
    """
    if no database exists then create it
    """

def create_table(name):
    """
    if the tables dont exist create it
    """

def add_line():
    """
    insert into table
    """

def remove_line():
    """
    delete from by
    """

def get_from_table():
    """
    gets data from a table
    """

def sort_table():
    """
    Order by 
    """
