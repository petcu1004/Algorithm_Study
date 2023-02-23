//3425

import java.util.ArrayList;
import java.util.Scanner;

class GoStack {
    ArrayList<Integer> list = new ArrayList<Integer>();

    public void NUM(int data) {
        if(data<0)
        {
            if(data>(10^9))
                System.out.println("ERROR");
            System.exit(0);

        }
        list.add(data);
    }

    public int POP() {
        if (list.size() == 0) {
            System.out.println("ERROR");
            System.exit(0);
            return 0;
        }
        return list.remove(list.size() - 1);
    }

    public void INV() {
        int first = POP();
        NUM(-first);

    }

    public void DUP() {
        int data = list.get(list.size() - 1);
        NUM(data);
    }

    public void SWP() {
        int data1 = POP();
        int data2 = POP();
        NUM(data1);
        NUM(data2);
    }

    public void ADD() {
        int data1 = POP();
        int data2 = POP();

        int res = data1 + data2;
        NUM(res);
    }

    public void SUB() {
        int data1 = POP();
        int data2 = POP();

        int res = data2 - data1;
        NUM(res);
    }

    public void MUL() {
        int data1 = POP();
        int data2 = POP();

        int res = data1 * data2;
        NUM(res);
    }

    public void DIV() {
        int data1 = POP();
        int data2 = POP();
        boolean check= false;

        if(data1==0 || data2==0) {
            System.out.println("ERROR");
            System.exit(0);
        }

        if(data1<0) {
            check=true;
            data1=-data1;
        }

        if(data2<0) {
            check=true;
            data2=-data2;
        }

        int res = data2 / data1;
        if(check==true) {
            NUM(-res);
        }
        NUM(res);
    }

    public void MOD() {
        int data1 = POP();
        int data2 = POP();
        boolean check= false;

        if(data1==0 || data2==0)
        {
            System.out.println("ERROR");
            System.exit(0);
        }
        if(data1<0) {
            check=true;
            data1=-data1;
        }

        if(data2<0) {
            check=true;
            data2=-data2;
        }

        int res = data2 % data1;
        if(check==true) {
            NUM(-res);
        }
        NUM(res);
    }

    public void CHECK(){
        if(list.size()==1){
            System.out.println("ERROR");
            System.exit(0);
        }
    }



}

public class Main3425 {

    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);
        GoStack stack = new GoStack();
        String input;

        do {
            input = sc.nextLine();
            String[] i=input.split(" ");

            switch (i[0]) {

                case "NUM":
                    String data=i[1];
                    int data1=Integer.valueOf(data);
                    stack.NUM(data1);
                    break;
                case "POP":
                    stack.POP();
                    break;
                case "INV":
                    stack.INV();
                    break;
                case "DUP":
                    stack.DUP();
                    break;
                case "SWP":
                    stack.CHECK();
                    stack.SWP();
                    break;
                case "ADD":
                    stack.CHECK();
                    stack.ADD();
                    break;
                case "SUB":
                    stack.CHECK();
                    stack.SUB();
                    break;
                case "MUL":
                    stack.CHECK();
                    stack.MUL();
                    break;
                case "DIV":
                    stack.CHECK();
                    stack.DIV();
                    break;
                case "MOD":
                    stack.CHECK();
                    stack.MOD();
                    break;
                case "QUIT":
                    if(stack.list.size()==1) {
                        System.out.println("ERROR");
                        System.exit(0);
                    }


            }
            System.out.println(stack.list);
            if(stack.list.size()==0) {
                System.out.println("ERROR");
            }

        }
        while (true) ;

    }
}