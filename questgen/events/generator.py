from events.models import Event

def generateEvent():
    print("I just created a generator file!")
    # We need to get an event based on whether we want a story event and,
    # if it is a story event, to get the next story event.
    #-------
    # Events are made up of sub-events, ranging in size according to settings
    # made by the game.
