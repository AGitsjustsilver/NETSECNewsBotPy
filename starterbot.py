import os
import time
import re
import logging
import rss
from slackclient import SlackClient

logging.basicConfig()

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
COMMANDS = [
    "add", 
    "remove",
    "list",
    "recent"
]

def parse_bot_commands(slack_events):
    """
    Description: Parses a list of events coming from the Slack RTM API to
                 find bot commands. If a bot command is found, this function 
                 returns a tuple of command and channel.
    Argument(s):
    slack_events - Array of  events that slack gets from the Real Time 
                 Messaging API (RTM API)
    Returns:
       If no tuple is found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
    Description: Finds a direct mention (a mention that is at the beginning)
                 in message text 
    Argument(s):
    message_text - The whole messge gotten from the RTM API and slack chat
    Returns: 
       Returns the user ID which was mentioned. If there is no direct mention,
       returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    """
    Description: Executes bot command if the command is known
    Argument(s):
    command    - The String that contains the whole command after the direct 
                 message
    channel    - The channel from which the message was posted to. used to put
                 returning messages into that channel
    Returns:
       None - but calls the API method chat.postMessage() to post to the 
       original channel
    """
    # Default response is help text for the user
    default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)
    
    # Finds and executes the given command, filling in response
    response = None
    # This is where you start to implement more commands!
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
    elif command.startswith(COMMANDS[0]):
        # add command
        response = add_feed()
    elif command.startswith(COMMANDS[1]):
        # remove command
        response = remove_feed()
    elif command.startswith(COMMANDS[2]):
        # list command
        response = list_feeds()
    elif command.startswith(COMMANDS[3]):
        # recent command
        response = list_recent_articles()
        
    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # read bot's user ID by calling web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Execption traceback printed above.")
 
