from ytscm import YTSCMonitor


def main():
    
    # create a new super chat monitor
    monitor = YTSCMonitor("client_secret.json", update_function)

    # start monitoring super chats (update every 5 seconds)
    monitor.start(interval=5)

    # stop monitoring super chats
    # monitor.stop()


def update_function(super_chat_event):
    """
    This function gets called when our monitor detects a new Super Chat!
    Prints out the name and amount of the supporter's Super Chat. 
    :param super_chat_event - the new Super Chat event
    """

    # get an object containing information about the supporter
    supporter_details = super_chat_event.get_supporter_details()

    print(supporter_details)


if __name__ == '__main__':
    main()