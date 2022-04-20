package BaekjoonQuiz.StepIf;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class AramClock {
    static final int FORWARD_TIME = 45, OVER_TIME = 24, UNDER_TIME = 0, FULL_MINUTE = 60;

    static public void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String time[] = br.readLine().split(" ");
        int hour = Integer.parseInt(time[0]), minute = Integer.parseInt(time[1]);
        int settingTime = minute - FORWARD_TIME;

        if (settingTime < 0) {
            --hour;
            minute = FULL_MINUTE + settingTime;

            if (hour < UNDER_TIME) {
                hour = OVER_TIME - 1;
            }
        }

        else {
            minute = settingTime;
        }

        System.out.printf("%d %d", hour, minute);
    }
}
