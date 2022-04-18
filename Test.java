import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Test { // class 명 Main
    static public void main(String args[]) throws IOException {
        System.out.println("Hello World!");
        // print method for Baekjoon time out
        /*
        BufferedReader : 버퍼 리더는 가공없이 string으로 입력 받음
        scanner : 스캐너는 값을 받으면 받는 값에 따라 달라지고 공백에 대해 나눠져서 받는다.
        
        단 buffered reader 사용 시 readline으로 받는데, 이때 main에 반드시 throws IOException이 필요하다.
        readline은 반드시 string으로 받음. 형변환이 필요.
         - try catch도 가능

        read data 가공 시 StringTokenizer st = new StringTokenizer(s);
        st.nextToken()으로 pop처럼 사용가능.

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out))
        bw.write() 출력, .newLine() 줄바꿈, 
        flush() 남은 데이터 모두 출력, close() 스트림 out 메모리 삭제.
        BufferedWriter는 버퍼를 잡아놓았기 때문에 반드시 flush, close를 통해 뒤처리를 해야함.
        */
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s = bf.readLine();
        bw.write(s);
        bw.newLine();
        bw.write("##########");

        bw.flush();
        bw.close();
    }
}