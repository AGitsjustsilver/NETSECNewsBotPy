"""
Slack Response Builder
Author: Alessandro Guaresti
Purpose: To build strings that conform to the way slack's chat.postMessage() 
API method wants it. Also makes it easy to have a style guide for posting
slack messages as the bot

Ideas: 
     - Make the functions able to work with one another like to be able to 
       make dynamic messages kinda like building blocks
"""

"""
Must use Methods
"""
def start_msg():
    return "[ "

def end_msg():
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
def new_divider():
    """
    Description: creates a new devider. A single new line divider. For example 
                -------------------------------------------------
    Argument(s): 
                 NONE
    Returns:
       The JSON format string for a divider in slack
    """
    response = '{ "type": "divder" }'
    return response

# Image
def new_image_block(img_url=None, alt_txt=None, title=None, block_id=None):
    """
    Description: Creates a single image to be displayed in the message
    Argument(s):
    img_url    - The http(s):// link to the image - Required
    alt_txt    - The text that displays in case that the url fails
                 - Required
    title      - A text object that has a string of text when hovering
                 over the image. When Image Block is used within Section 
                 blocks you should use new_image_element() instead
    block_id  -  The Identifier for the image incase you want to do an
                 action with it
    Returns:
       The JSON format string for an Image Block in slack
    """
    if img_url is None or alt_txt is None:
        err_txt = "Missing required field: "
        if img_url and alt_txt is None:
            err_txt += "Image URL and Alternate Text is required."
        elif img_url is None:
            err_txt += "No URL found. Using Alternate Text"            

        response = error_message(err_txt)
    else:
        response = '{ "type": "image", '
        if title is None:
            response += ' "block_id": "' + block_id + '"' + new_item()
                     +  ' "image_url": "' + img_url + '"' + new_item()
                     +  ' "alt_text": "'  + alt_txt + '"' + ' }' 
        elif block_id is None:
            response += ' "title": '     + title    + new_item()
                     +  ' "image_url": "' + img_url + '"' + new_item()
                     +  ' "alt_text": "'  + alt_txt + '"' + ' }'
        else:
            response += ' "title": '     + title    + new_item()
                     +  ' "block_id": "' + block_id + '"' + new_item()
                     + ' "image_url": "' + img_url + '"'  + new_item()
                     +  ' "alt_text": "' + alt_txt + '"'  + ' }'
    return response

# Action

# Context


"""
Elements
"""

# Image

# Button

# Select Menus

# Overflow Menu

# Date Picker

"""
Objects
"""

# Text

# Confirmation Dialog

# Option

# Option Group

"""
Pre-built Messages
"""

def error_message(err_text=None):
    response = start_message() + 
    if err_text is None:
        response +=
    else:
        response

    response += end_message()
    return response
