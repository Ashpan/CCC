import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int timeafter = input.nextInt();
		int hour = 12;
		int counter = 0;
		while (timeafter > 59) {
			hour++;
			timeafter = timeafter - 60;
		}
		while (hour > 12) {
			hour = hour - 12;
		}
//		System.out.println("minutes " + timeafter);
//		System.out.println("hour " + hour);
		if (timeafter < 10 && timeafter > 0) {
			int firstDigit = 0;
			int secondDigit = timeafter;
		} else if (timeafter == 0) {
			int firstDigit = 0;
			int secondDigit = 0;
		}
		int h = 0;
		int m = 0;
		for (h = hour; h > 12; h--) {
			for (m = timeafter; m > 0; m--) {
				int secondDigitHour = 0;
				int firstDigitHour = 0;
				int firstDigitMin = Integer.parseInt(Integer.toString(timeafter).substring(0, 1));
				int secondDigitMin = Integer.parseInt(Integer.toString(timeafter).substring(1, 2));
				if (hour > 9) {
					firstDigitHour = Integer.parseInt(Integer.toString(hour).substring(0, 1));
					secondDigitHour = Integer.parseInt(Integer.toString(hour).substring(1, 2));
				} else if (hour < 10) {
					firstDigitHour = Integer.parseInt(Integer.toString(hour).substring(0, 1));
					secondDigitHour = 0;

				}
				int difference = secondDigitMin - firstDigitMin;
//				System.out.println(firstDigitMin);
//				System.out.println(secondDigitMin);
//				System.out.println("difference is " + difference);
				if (secondDigitHour == 0) {
					if (difference == firstDigitMin - firstDigitHour) {
						counter++;
					}

				} else if (secondDigitHour > 0) {
					if (difference == firstDigitMin - secondDigitHour
							&& difference == secondDigitHour - firstDigitHour) {
						counter++;
					}
				}
			}
		}
		System.out.println(counter);

	}

}
