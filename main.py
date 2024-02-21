from ytscm import YTSCMonitor


def main():
    
    # create a new super chat monitor
    monitor = YTSCMonitor("client_secret.json", "chat", update_function)

    # start monitoring super chats (update every 5 seconds)
    monitor.start(interval=5)

    # stop monitoring super chats
    # monitor.stop()


def update_function(event):
    """
    This function gets called when our monitor detects a new Super Chat!
    Prints out the name and amount of the supporter's Super Chat. 
    :param event - the new Super Chat event
    """

    # get an object containing information about the supporter
    supporter_details = event.get_author_details()

    print(supporter_details)


if __name__ == '__main__':
    main()