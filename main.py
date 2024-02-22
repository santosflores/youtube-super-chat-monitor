from ytscm import YTSCMonitor
from ytscm.superchat_event import YTSCEvent

import requests
import json

def main():

    # create a new super chat monitor
    monitor = YTSCMonitor("client_secret.json", "chat", super_chat_processing)

    # start monitoring super chats (update every 5 seconds)
    monitor.start(interval=5)

    # stop monitoring super chats
    # monitor.stop()


def super_chat_processing(event: YTSCEvent):
    """
    This function gets called when our monitor detects a new Super Chat!
    Prints out the name and amount of the supporter's Super Chat. 
    :param event - the new Super Chat event
    """
    # get an object containing information about the supporter
    supporter_details = event.get_supporter_details()
    comment = event.get_comment_text()
    inputs = comment.split(',')
    year = int(inputs[0])
    zodiac_sign = str(inputs[1])
    question = str(inputs[2])
    username = str(event.get_supporter_details().get_display_name())
    data = {
        "yearOfBirth": year,
        "zodiacSign": zodiac_sign,
        "question": question,
        "username": username
    }    
    # Set the headers to indicate JSON data
    headers = {"Content-Type": "application/json"}
    response = requests.post(url='http://127.0.0.1:5000/request-fortune', data=json.dumps(data), headers=headers)


if __name__ == '__main__':
    # main()
    e = YTSCEvent({
        'id': 0,
        'snippet': {
            'commentText': '1998,Gemini,What will the future bring to my life?',
            'createdAt': 'a',
            'channelId': 'youtube#liveChatMessage',
            'amountMicros': 'a',
            'currency': 'a',
            'displayString': 'a',
            'supporterDetails': {
                'channelId': '1',
                'channelUrl': '2',
                'displayName': '3',
                'profileImageUrl': '4',
            }
        },
    })
    super_chat_processing(e)
