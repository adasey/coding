package BaekjoonQuiz.StepPrint;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Cat {
    static public void main(String args[]) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write("\\    /\\\n");
        bw.write(" )  ( ')\n");
        bw.write("(  /  )\n");
        bw.write(" \\(__)|");

        bw.flush();
        bw.close();
    }
}
