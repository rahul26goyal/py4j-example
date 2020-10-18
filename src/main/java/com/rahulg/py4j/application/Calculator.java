package com.rahulg.py4j.application;

import com.sun.org.apache.xerces.internal.xs.StringList;

import java.util.ArrayList;
import java.util.List;

public class Calculator {

    public int add(Integer a, Integer b) {
        System.out.println("Adding...");
        return a + b;
    }

    public int sub(Integer a, Integer b) {
        return a - b;
    }

    public int multiply(Integer a, Integer b) {
        return a * b;
    }

    public int divide(Integer a, Integer b) {
        return a / b;
    }

    public Integer add(Integer[] args) {
        System.out.println("Adding Array..." + args.toString());
        int sum = 0;
        for(Integer i = 0; i < args.length; i++) {
            sum += args[i];
        }
        return sum;
    }

    public Integer add(List<Integer> args) {
        System.out.println("Adding List..." + args.toString());
        int sum = 0;
        for(Integer ele : args) {
            sum += ele;
        }
        return sum;
    }

    public String display() {
        return "This is a calculator Service Object..";
    }

    public List<String> getListOfOperations() {
        List<String> l1 = new ArrayList<String>();
        l1.add("addition");
        l1.add("subtraction");
        l1.add("Multiplication");
        l1.add("division");
        return l1;

    }
}
