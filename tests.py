from responseBuilder import ResponseBuilder

rb = ResponseBuilder()

print 'starting...'

class SampleMessageProtocolEntity:



    def __init__(self, sender, message):
        self.sender = sender
        self.message = unicode(message)

    def getFrom(self):
        return self.sender

    def getBody(self):
        return self.message

# msg1 = SampleMessageProtocolEntity('bas', 'hoi')
# msg2 = SampleMessageProtocolEntity('bas', 'Hi there')
# msg3 = SampleMessageProtocolEntity('bas', 'bad!s')
# msg4 = SampleMessageProtocolEntity('bas', 'hoi')
# msg5 = SampleMessageProtocolEntity('bas', 'How about you?')
#
# testmessages = [msg1, msg2, msg3, msg4, msg5]
#
# for msg in testmessages:
#     responses = rb.getResponsesForMessage(msg)


while True:
    incomingmsg = raw_input('Incoming message:')
    msgentity = SampleMessageProtocolEntity('bas', incomingmsg)
    rb.getResponsesForMessage(msgentity)
