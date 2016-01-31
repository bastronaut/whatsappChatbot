from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity



class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over

        print 'on message werkt'
        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())

            print messageProtocolEntity.getBody()

            messagebody = messageProtocolEntity.getBody().lower()
            sjoerd = 'sjoerd'
            if sjoerd in messagebody -1:

                outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    'DIE IS HELEMAAL GEK!!!',
                    to = messageProtocolEntity.getFrom())

            else:
                outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    messageProtocolEntity.getBody(),
                    to = messageProtocolEntity.getFrom())

            self.toLower(receipt)
            self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        print 'receipt hier'
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)
