class UtilityManager(object):

    def __init__(self):
        pass

    @classmethod
    def get_external_network_ip(cls):
        data = json.loads(urllib.urlopen("http://ip.jsontest.com/").read())
        print data["ip"]

    @classmethod
    def get_default_gateway(cls):
        import socket
        gateway = socket.gethostbyname(socket.gethostname())
        print gateway