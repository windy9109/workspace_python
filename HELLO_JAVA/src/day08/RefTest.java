package day08;

public class RefTest {

	static int a = 3;
	static int[] b = {1};
	
	public static void main(String[] args) {

		
		myincrease0(a, b);
		myincrease(a);
		myincrease2(b);
		myincrease0(a, b);
		
	}
	
	public static void myincrease0(int a ,int[] arr) {
		System.out.println("a:"+a);
		System.out.println("b:"+arr[0]);
	}
	
	
	public static void myincrease(int a) {
		a++;
	}
	public static void myincrease2(int[] arr) {
		arr[0]++;
	}

}
