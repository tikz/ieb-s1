import logging
import sys

from twisted.internet import protocol, reactor

from product import ProductEncrypted as Product

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Client(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(sys.argv[2].encode('utf-8'))

    def dataReceived(self, data):
        Product().unserialize(data).pretty_print()


class ClientFactory(protocol.ClientFactory):
    protocol = Client

    def clientConnectionFailed(self, connector, reason):
        logger.error(f"Connection failed: {reason}")
        reactor.callFromThread(reactor.stop)

    def clientConnectionLost(self, connector, reason):
        logger.error(f"Connection lost: {reason}")
        reactor.callFromThread(reactor.stop)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: client.py <server>:<port> <product code>")
        sys.exit(1)

    server, port = sys.argv[1].split(":")

    f = ClientFactory()
    reactor.connectTCP(server, int(port), f)
    reactor.run()
