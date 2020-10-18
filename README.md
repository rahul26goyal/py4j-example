# py4j-example
A small project to demonstrate working on py4j

## Create a virtualenv for python

 `virtualenv -p python3.7 venv`

 `source ./venv/bin/activate`

 `pip install py4j`

 ## Setup the Java Dependency:
 Location of the Java jar

 - `./venv/share/py4j/py4j0.10.9.jar`

 If you are using intelliji, use this link to add jar to the dependecies: https://stackoverflow.com/questions/1051640/correct-way-to-add-external-jars-lib-jar-to-an-intellij-idea-project

 - I have added the jar to `./libs` and included that directory for dependent jars.

 ## Example 1: SampleGatewayServer.java

 - It starts the JVM and keep running until stopped
 - It runs on the default port 25333
 - Execute the java program
    - either via command line or via intelliji
 - Testing using python
   - active the virtual env where py4j was installed.
   - start python shell
   - execute the below code to check that we are able to attache to JVM from python shell
   ```
   >>> from py4j.java_gateway import JavaGateway
   >>> gatewayClient = JavaGateway()
   >>> random = gatewayClient.jvm.java.util.Random()
   >>> random.nextInt(2)
   1
   >>> random.nextInt(2)
   0
   >>>
   ```
   - Or Run this

   ` python ./python/sample_gateway.py`



## Example 2: CalculatoorGatewayServer

 - Calculator.java is the actual Implementation of Calculator Methods.
 - CalculatorGatewayServer is Gateway server which start by binding an instance of Calculator at start time
 - this instance is set as `entry_point`.

 - Testing using Python Code:
    - Run `./python/test_caclulator_service.py` file.


# Prevent committing secrets:
   Using https://github.com/awslabs/git-secrets for this:
   - `brew install git-secrets` => install plugin
   - `git secrets --install` => set pre-commit check for current repo.
   - `git secrets --register-aws` => adds common aws pattern.
   - `git secrets --scan-history` => scans previous commits too.
   - `git secrets --scan <file>` => adhoc scan.
