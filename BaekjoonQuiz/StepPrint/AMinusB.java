package BaekjoonQuiz.StepPrint;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class AMinusB {
    static public void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String typed[] = br.readLine().split(" ");

        int result = Integer.parseInt(typed[0]) - Integer.parseInt(typed[1]);

        System.out.println(result);
    }
}
