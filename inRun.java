// package Infix2Postfix;

public class inRun {

	public static void main(String[] args) {

		in2Postfix ob = new in2Postfix("A.b + a.B", 'B');
		ob.getPostfix();
		ob.display();
	}

}
