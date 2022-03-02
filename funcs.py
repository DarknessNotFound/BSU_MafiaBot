from global_variables import *

def list_to_str(daList):
    return ' '.join(daList)

def sendMsg(msg):
    return msg

def accessible_channel(message):
    if (str(message.channel.id) == MY_CHANNEL):
        return True
    else:
        return False