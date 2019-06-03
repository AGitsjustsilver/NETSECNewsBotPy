# NETSECNewsBotPy
A python bot that listens to direct mentions for commands related to RSS feeds for news distribution

## Bot Info
Python 2.7  
pip  
virtualenv  
Slack  

## Using the Bot
### Installing 
``` bash
    virtualenv starterbot
    source starterbot/bin/activate
    pip install slackclient
    export SLACK_BOT_TOKEN='your bot user access token here'
```

**Note**: it would be easier to put your token as a Environmental variable in your .bashrc file. Put the last line from the install commands in your .bashrc or use the command every time your start up your project

### Starting up 
``` bash
    source starterbot/bin/activate
    # start bot
    python starterbot.py
```


## Credit Links
I took some inspiration and code from these sites and modified to work for my bot

#### Matt Makai from [Full Stack Python](https://www.fullstackpython.com/)
[*Base python bot*](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)

#### [Alvin Alexander](https://alvinalexander.com/)
[*RSS pulling in python*](https://alvinalexander.com/python/python-script-read-rss-feeds-database)
