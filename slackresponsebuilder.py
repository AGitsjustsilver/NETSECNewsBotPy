"""
Slack Response Builder
Author: Alessandro Guaresti
Purpose: To build strings that conform to the way slack's chat.postMessage() 
API method wants it. Also makes it easy to have a style guide for posting
slack messages as the bot
"""

"""
Must use Methods
"""
def start_message():
    return "[ "

def end_message():
    return " ]"

"""
Might Use
"""
def new_item():
    return ","


"""
Blocks
"""

# Section
# Divider
def new_devider():
    response = '{ "type": "divder"}'
    return response

# Image
def new_image(img_url=None, alt_txt=None, title=None, block_id=None):
    if img_url is None or alt_txt is None:
        response = error_message("Missing required field")
# Action
# Context
