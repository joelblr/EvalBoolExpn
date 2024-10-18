// package Infix2Postfix;

import java.util.*;
public class in2Postfix {

	static String postfix;
	static HashMap <Character, Integer> unique = new HashMap<>();
	char type;
	String infix;

	/// type : A, Arithmetic Expn; type = B, Boolean Expn
	in2Postfix(String infx, char type) {
		this.infix = infx;
		this.type = type;
	}


	int prior(char ch) {

		if (ch == '(' || ch == '#')
            return 1;
		else if (ch == '+' || ch == '-')
            return 2;
        else if (ch == '*' || ch == '/')
            return 3;
        else if (ch == '^')
            return 4;
        else if (ch == '.')
            return 5;
        else if (ch == '!')
            return 6;
		return 0;
	}


	void getPostfix() {

		postfix = "";
		int top = -1;
		char stac[] = new char[infix.length()];
		int k = 0;

		stac[++top] = '#';
		for (int i = 0; i < infix.length(); i++) {

			/////
			char ch1 = infix.charAt(i);
			char ch2 = Character.toUpperCase(ch1);

			if (Character.isWhitespace(ch1)) {
				continue;

			}else if (Character.isLetter(ch1)) {
				postfix += ch1;
				if (!unique.containsKey(ch2))
					unique.put(ch2, k++);

			}else if (ch1 == '(' || ch1 == '!') {
				stac[++top] = ch1;

			}else if (ch1 == ')') {
				while (stac[top] != '(')
					postfix += stac[top--];
				top--;

			}else {
				while (prior(stac[top]) >= prior(ch1))
					postfix += stac[top--];
				stac[++top] = ch1;

			}

		}while (stac[top] != '#')
			postfix += stac[top--];
	}

	void display() {
		for (int i = 0; i < postfix.length(); i++)
			System.out.print(postfix.charAt(i)+" ");
		System.out.println();
	}

}
