import java.util.*;
public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int number = input.nextInt();
		int solutions = 0;
		int lefth = number;
		int righth = 0;
		
		while(lefth >= righth){
			solutions++;
			lefth--;	
			righth++;
		}
	System.out.println(solutions);
	}

}