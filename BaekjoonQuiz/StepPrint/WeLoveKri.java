package BaekjoonQuiz.StepPrint;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class WeLoveKri {
    static public void main(String args[]) throws IOException{
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String strong = "강한친구 대한육군";
        bw.write(strong);
        bw.newLine();
        bw.write(strong);

        bw.flush();
        bw.close();
    }
}
