"""
RSS module
Author: Alessandro Guaresti
Purpose: To be a place for all commands that the bot will have to manipulate
RSS feeds and their articles. All functions return a string of less than 4000
charcters as to comply to Slack's api chat.postMessage command 

Utils: Will probably use the mysql module I will make
"""

def add_feed(feed_URL, feed_id=None, feed_title=None):
    """
    Description: Adds to the feed to the database
    Argument(s): 
    feed_URL   - The http(s):// URL to the feed that you wish to pull from
    feed_id    - Default to None will generate an id, else user given int id
    feed_title - Defalt to None will see if it can pull a title from feed,
                 else will set the title to the main domain of the feed
    Returns:
       a composite string of tidy JSON to post to the channel if the addition
       was successful or not
    """

def remove_feed(feed_id):
    """
    Description: Removes the given feed_id from the database
    Argument(s):
    feed_id    - an existing feed id from the database to remove from the
                 feeds database and it's corresponding articles from the
                 articles db
    Returns:
       a composite string of tidy JSON to post to the channel if the removal
       was successful or not
    """

def list():
    """
    Description: lists all the feeds in the database
    Argument(s): 
                 NONE
    Returns:
       a string of tidy JSON to list all the feeds that exist in the feed db
    """

def list_recent(identifier=None, amount=5):
    """
    Description: grabs the most recent articles from the given identifiers 
                 if None is specified then the most recent articles from 
                 the articles db will be fetched. The default amount of 
                 articles fetched will be 5 unless stated otherwise
    Argument(s):
    identifier - It can be either the URL, feed id, or feed Title to get
                 artcles from the articles db. If left blank, then it will
                 gather articles regardless of which feed
    amount     - The number of articles to pull from the recent database
                 The default amount of articles that will be produced is 5
    Returns:
       A tidy string of JSON that lists the articles, if the amount is more
       than 4000 characters then i need to figure out what to do with it
    """
    
def cmd_help(command=None):
    """
    Description: gives help for the command specified or general use 
                 for commands
    Argument(s):
    command    - The command to specify help. Defaults to None if no 
                 no specific command is stated then all commands will be 
                 breifly talked about
    Return:
       a tidy JSON string that displays how to use the command 
    """
