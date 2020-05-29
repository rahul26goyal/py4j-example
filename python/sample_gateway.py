from py4j.java_gateway import JavaGateway


def _main():
    print("Testing SampleGatewayServer Client...s")
    gateway = JavaGateway()
    randoom = gateway.jvm.java.util.Random()
    print("1. Random %s" %randoom.nextInt(10))
    print("2. Random %s" %randoom.nextInt(10))

if __name__ == "__main__":
    _main()