package runner;

import java.util.Scanner;

import runner.model.OutOfBoundException;

public class FizzBuzz {
	
	public static void fizzBuzz(int n) throws OutOfBoundException {
		
		if (n <= 0) {
			throw new OutOfBoundException(n);
		}
		
		for (int i = 1; i <= n; ++i) {
			
			if (i%15 == 0) {
				System.out.println("FizzBuzz");
			}
			else if (i%5 == 0) {
				System.out.println("Buzz");
			}
			else if (i%3 == 0) {
				System.out.println("Fizz");
			}
			else {
				System.out.println(i);	
			}
			
		}
		
	}
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int inputNumber = sc.nextInt();
		sc.close();
		
		try {
			fizzBuzz(inputNumber);
		} catch (OutOfBoundException e) {
			e.printStackTrace();;
		}
		
	}

}
