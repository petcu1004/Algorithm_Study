//3460

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main3460 {

    public static void main(String[] args) throws IOException {

        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int testcase=Integer.parseInt(br.readLine());

        for(int i=0;i<testcase;i++){
            int count=0;
            int n=Integer.parseInt(br.readLine());
            while (true){
                if(n==1){
                    System.out.println(count);
                    break;
                }
                if(n%2==1)
                    System.out.print(count+" ");
                count++;
                n /=2;
            }
        }
    }
}
