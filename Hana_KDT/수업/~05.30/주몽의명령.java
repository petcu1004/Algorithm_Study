package Hana_KDT.수업;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 주몽의명령{
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int m=Integer.parseInt(br.readLine());

        int[]a = new int[n];
        StringTokenizer st= new StringTokenizer(br.readLine());
        for(int i=0;i<a.length;i++){
            a[i]=Integer.parseInt(st.nextToken());
        }
        Arrays.sort(a);

        int count=0; //경우수(가짓수)의 합
        int i=0, j=n-1;
        while(i<j){
            if(a[i]+a[j]<m) i++;
            else if(a[i]+a[j]>m) j--;
        }
        
        System.out.println(count);


    }
}