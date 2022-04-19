package BaekjoonQuiz.StepPrint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ASubB {
    static public void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] typed = br.readLine().split(" ");

        System.out.println(Integer.parseInt(typed[0]) + Integer.parseInt(typed[1]));
    }
}
