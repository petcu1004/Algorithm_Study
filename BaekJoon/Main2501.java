//2501

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main2501 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int p = Integer.parseInt(input.split(" ")[0]);
        int k = Integer.parseInt(input.split(" ")[1]);
        ArrayList<Integer> arr= new ArrayList<>();

        int res;

        for(int i=1;i<=p;i++){
            res=p%i;
            if(res==0){
                arr.add(i);
            }
        }

        if(arr.size()<k){
            System.out.printf("0");
        }
        else
            System.out.println(arr.get(k - 1));
    }
}
