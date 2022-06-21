package javaCode.src;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Fibbonacci {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Fibbonacci fibo = new Fibbonacci();

        int time = Integer.parseInt(bf.readLine());

        int num = 0;
        for (int i = 0; i < time; i++) {
            num = Integer.parseInt(bf.readLine());
            bw.write((num != 0 ? Integer.toString(fibo.fibonacci(num - 1)) : 1) + " " + Integer.toString(fibo.fibonacci(num)));
            bw.newLine();
        }

        bw.flush();
        bw.close();
    }

    public int fibonacci(int number) {
        Double head = Math.pow(1 + Math.pow(5, 0.5), number) - Math.pow(1 - Math.pow(5, 0.5), number);
        Double body = Math.pow(2, number) * Math.pow(5, 0.5);
        return (int) (head / body);
    }
}
