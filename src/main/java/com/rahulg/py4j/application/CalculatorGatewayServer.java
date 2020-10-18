package com.rahulg.py4j.application;

import py4j.GatewayServer;

public class CalculatorGatewayServer {

    public static void main(String[] args) {
        System.out.println("Starting CalculatorGatewayServer Server..");
        GatewayServer gateway = new GatewayServer(new Calculator());
        gateway.start();
        System.out.println("Gateway Server Started...this will keep running.");
    }
}
