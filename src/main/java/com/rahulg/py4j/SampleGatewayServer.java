package com.rahulg.py4j;

import py4j.GatewayServer;

public class SampleGatewayServer {

    public static void main(String[] args) {
        System.out.println("Starting Java gateway Server..");
        GatewayServer gateway = new GatewayServer();
        gateway.start();
        System.out.println("Gateway Server Started...this will keep running.");
    }
}
