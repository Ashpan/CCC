import java.util.*;
public class Main {

	public static void main(String[] args) {
		int n=0;
		int k=0;
		int sum=0;
		Scanner input = new Scanner(System.in);
		n=input.nextInt();
		k=input.nextInt();
		sum=n;
		String phase = String.valueOf(n);
		int increment=0;
		boolean theresasum=true;
		while(increment<k){
			if(k>0){
				phase = phase+"0";
				sum=sum+Integer.parseInt(phase);
				increment++;
			}else if(k==0){
				theresasum=false;
			}
		}
			if(theresasum=true){
				System.out.println(sum);
			}
//			if(k==k){
//				break;
//			}
		
	}

}
