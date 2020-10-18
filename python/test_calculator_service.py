
from py4j.java_gateway import JavaGateway

from py4j.java_collections import ListConverter
from py4j.protocol import Py4JError, Py4JJavaError

def _main():
    print("Testing Claculator Serivice...")
    gateway = JavaGateway()
    # we can also set auto_convert=True to let py4j handle the basic conversions.
    calculatorClient = gateway.entry_point
    print("calculatorClient: " + calculatorClient.display())
    try:
        test_addition(calculatorClient)
        test_java_list_addition(gateway, calculatorClient)
        test_python_list_addition(gateway, calculatorClient)

        test_getting_java_list(gateway, calculatorClient)
    except Py4JError:
        print("Py4JError: Exception Occured...")
        traceback.print_exc()
    except Py4JJavaError:
        print("Py4JJavaError: Exception Occured...")
        traceback.print_exc()

def test_addition(client):
    print("Test addition:")
    result = client.add(3, 5)
    print("3 + 5 = %s" %result)


def test_java_list_addition(gateway, client):
    java_list = gateway.jvm.java.util.ArrayList()
    java_list.append(1)
    java_list.append(2)
    java_list.append(3)
    result = client.add(java_list)
    print("Result of addition %s = %s" % (java_list, result))

def test_python_list_addition(gateway, client):
    py_list = [1,2,3,4,5]
    java_list = ListConverter().convert(py_list, gateway._gateway_client)
    result = client.add(java_list)
    print("Result of addition py_list: %s = %s" % (py_list, result))
    # this will fail
    #result = client.add(py_list)

def test_getting_java_list(gateway, client):
    # what is returnes in an java List and not pytthon list.
    java_list = client.getListOfOperations()
    check_addition = java_list.contains("addition")
    print("Is addition Supported: %s" %check_addition)

    # convert java_list to python_list. creates a copy of the elements.
    py_list = list(java_list)


if __name__ == "__main__":
    _main()