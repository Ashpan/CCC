package CCC2016;
import java.util.*;
public class MagicSquares {

	@SuppressWarnings("resource")
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		int [] [] grid = new int[4][4];
		int [] sums = new int[8];
		int count = 0;
		for (int i = 0; i<grid.length; i++){
			int total = 0;
			for(int j =0; j<grid.length;j++){
			grid[i][j] = input.nextInt();
			total = total + grid[i][j];
			}
			sums[count] = total;
			count++;

		}
				
		for (int j = 0; j<grid.length; j++){
			int total = 0;
			for(int i=0; i<grid.length;i++){
			total = total + grid[i][j];
			}
			sums[count] = total;
			count++;
			}
			
			int prev=sums[0];
			int magic = 0;
			for(int x:sums){
				if(x!=prev){
					magic = 0;
					prev=x;
				}else{
					magic=1;
				}
			}
			if(magic==1){
				System.out.println("magic");
			}else{
				System.out.println("not magic");
			}
		
	}


}