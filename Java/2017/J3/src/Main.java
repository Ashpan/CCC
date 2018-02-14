import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int start[] = new int [2];
		int end[] = new int [2];
		int fuel = 0;
		int x = 0;
		int y = 0;
		System.out.println("Enter inital");
		String StartCoords = input.nextLine();
		for(x=0;x<StartCoords.length();x++){
			if(StartCoords.charAt(x) == ' '){
				String lol = StartCoords.substring(0, x);
				System.out.println(lol);
				String lol2 = StartCoords.substring(x+1, StartCoords.length());
				System.out.println(lol2);
				int firstnuminitial = Integer.parseInt(lol);
				int secondnuminitial = Integer.parseInt(lol2);
				System.out.println(firstnuminitial);
				System.out.println(secondnuminitial);
				
			}
		}
		
		input.nextLine();
		System.out.println("Enter final");
		end[y] = input.nextInt();
		input.nextLine();
		System.out.println("Enter fuel");
		fuel = input.nextInt();
		System.out.println("first char of final destination is " + end[0]);
		System.out.println("second char of final destination is " + end[1]);
		System.out.println("first char of initial location is " + start[0]);
		System.out.println("second char of initial location is " + start[1]);
		
		int xdiff=end[0]-start[0];
		int ydiff=end[1]-start[1];
		System.out.println("Xdiff is " + xdiff);
		System.out.println("Ydiff is " + ydiff);
		
		
		
		
	}
}