package CCC2015;
import java.util.Scanner;
public class J1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
int month = 0;
int day = 0;
		// System.out.println("Enter the number of month");
		month = input.nextInt();
		// System.out.println("Enter the number of day");
		day = input.nextInt();
		if(month == 2 && day < 18){
			System.out.println("Before");
		}else if (month < 2){
			System.out.println("Before");
		}else if(month == 2 && day == 18){
			System.out.println("Special");
		}else{
			System.out.println("After");
		}

		
	}
}
