from events.models import Event

def generateEvent():
    print("I just created a generator file!")
    # We need to get an event based on whether we want a story event and,
    # if it is a story event, to get the next story event.
    #-------
    # Events are made up of sub-events, ranging in size according to settings
    # set by the game.
    #-------
    # We need to return an object that looks like this:
    # {
    #     story: <bool>,
    #     type: <event_type_id>,
    #     characters: {
    #         info: {
    #             name: <string>
    #             type: <type_id>
    #         }
    #         dialogue: {
    #             content: <string>
    #             responses: {
    #                 <response_id>: <string>,
    #                 ...
    #             }
    #         },
    #         ...
    #     }
