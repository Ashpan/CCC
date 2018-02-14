import java.util.*;
public class Main {
	public static void main(String[] args) {
	int x=0;
	int y=0;
	Scanner input = new Scanner(System.in);
	x = input.nextInt();
	y = input.nextInt();
	if(x<0){
		if(y<0){
			System.out.println("3");
		}else if(y>0){
			System.out.println("2");
		}
	}else if(x>0){
		if(y<0){
			System.out.println("4");
		}else if(y>0){
			System.out.println("1");
		}
	}
}
}