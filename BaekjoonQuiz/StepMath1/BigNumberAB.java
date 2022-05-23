package BaekjoonQuiz.StepMath1;

import java.math.BigInteger;
import java.util.*;

public class BigNumberAB {
    static public void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        String number = scanner.nextLine();
        String[] numbers = number.split(" ");
        BigInteger a = new BigInteger(numbers[0]);
        BigInteger b = new BigInteger(numbers[1]);
        BigInteger sum = a.add(b);

        System.out.println(sum);
        scanner.close();
    }
}