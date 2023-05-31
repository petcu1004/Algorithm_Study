
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;



public class DNA비밀번호 {

    static int checkArr[];
    static int myArr[];
    static int checkSecret;

    public static void main(String[] args) throws IOException{
        //DNA 암호 구하기 - 슬라이딩 문제
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int s = Integer.parseInt(st.nextToken()); //문자열의 크기 9
        int p = Integer.parseInt(st.nextToken()); //부분 문자열의 길이 8
        int result=0;
        
        char a[] = new char[s];
        checkArr=new int[4];
        myArr=new int[4];
        // checkArr=0;

        a=bf.readLine().toCharArray();
        st=new StringTokenizer(bf.readLine());

        for (int i=0;i<4;i++){
            checkArr[i]=Integer.parseInt(st.nextToken());
            if(checkArr[i]==0){
                checkSecret++;
            }

        }

        for(int j=0;j<p;j++){
            add(a[j]);
        }

        if(checkSecret==4){
            result++;
        }

        for(int i=p;i<s;i++){
            int j=i-p;
            add(a[i]);
            remove(a[j]);
            if(checkSecret==4){
                result++;
            }
        }}

    private static void add(char c) {
        //새로 들어온 문자W를 처리하기
        switch(c){
            case 'A':myArr[0]++;
            if(myArr[0]==checkArr[0]) checkSecret++;
            break;
            case 'C':myArr[1]++;
            if(myArr[1]==checkArr[1]) checkSecret++;
            break;
            case 'G':myArr[2]++;
            if(myArr[2]==checkArr[2]) checkSecret++;
            break;
            case 'T':myArr[3]++;
            if(myArr[3]==checkArr[3]) checkSecret++;
            break;

        }

        } 

    private static void remove(char c) {
        //제거되는 문자를 처리하기
        switch(c){
            case 'A':myArr[0]++;
            if(myArr[0]==checkArr[0]) checkSecret--;
            myArr[0]--;
            break;
            case 'C':myArr[1]++;
            if(myArr[1]==checkArr[1]) checkSecret--;
            myArr[1]--;
            break;
            case 'G':myArr[2]++;
            if(myArr[2]==checkArr[2]) checkSecret--;
            myArr[2]--;
            break;
            case 'T':myArr[3]++;
            if(myArr[3]==checkArr[3]) checkSecret--;
            myArr[3]--;
            break;

        }

    }

      

}

