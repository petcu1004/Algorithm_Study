/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// double b;
// char g;
// String var;
// long AB;
// a = sc.nextInt();                           // int 변수 1개 입력받는 예제
// b = sc.nextDouble();                        // double 변수 1개 입력받는 예제
// g = sc.nextByte();                          // char 변수 1개 입력받는 예제
// var = sc.next();                            // 문자열 1개 입력받는 예제
// AB = sc.nextLong();                         // long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// double b = 1.0;               
// char g = 'b';
// String var = "ABCDEFG";
// long AB = 12345678901234567L;
//System.out.println(a);                       // int 변수 1개 출력하는 예제
//System.out.println(b); 		       						 // double 변수 1개 출력하는 예제
//System.out.println(g);		       						 // char 변수 1개 출력하는 예제
//System.out.println(var);		       				   // 문자열 1개 출력하는 예제
//System.out.println(AB);		       				     // long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
import java.util.Arrays;
import java.util.Scanner;
import java.io.FileInputStream;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
	public static void main(String args[]) throws Exception
	{
		/*
		   아래의 메소드 호출은 앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
		   여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
		   이 코드를 프로그램의 처음 부분에 추가하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
		   따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 메소드를 사용하셔도 좋습니다.
		   단, 채점을 위해 코드를 제출하실 때에는 반드시 이 메소드를 지우거나 주석 처리 하셔야 합니다.
		 */
		//System.setIn(new FileInputStream("res/input.txt"));

		/*
		   표준입력 System.in 으로부터 스캐너를 만들어 데이터를 읽어옵니다.
		 */
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/
		String n;
		int x, y;
		for(int test_case = 1; test_case <= T; test_case++)
		{
			
			n=sc.next();
			x=sc.nextInt();
			y=sc.nextInt();
			int[] N = new int[n.length()]; // input 문자열 길이만큼 배열 준비.
			for(int i=0;i<n.length();i++) {
				N[i] = n.charAt(i) - '0'; // i=0 일때, '1' - '0' = 1 이됨.
			}

			int[] res = new int[n.length()];
			// System.out.println(res);			

			System.out.print("#"+test_case+" ");

			if(n.length()==1){ //N이 한자리수일 경우
				//n과 비교했을 때 x가 0이면서, y까지 가서 n보다 작은 값이면 성공, 하지만 x가 작은 값인데 y가 큰값이면 안되고, 
				//x가 더 큰값일 경우는 y까지 안가도 그냥 안됨.
				if(x==0 && N[0]>y){
					//결과값 나옴
					System.out.println(y);
					
				}
				else{ 
					//-1 출력
					System.out.print(-1);
				}
			}
			else if(n.length()==2){ //N이 두 자리수 이상
				//x가 작은 경우, y값은 다 상관없음.
				if(N[0]>x){
					//결과값 나옴
					if(N[1]>y){
						res[0]=y;
						res[1]=x;

						for(int i=0;i<res.length;i++){
							System.out.print(res[i]);
						}
						// System.out.println(Arrays.toString(res));
					}
				}
				//x가 같은 경우, y값보다 작거나 같아야함.
				else if(N[0]==x){
					if(N[1]>y){
						//결과값 나옴.
						res[0]=x;
						res[1]=y;
						for(int i=0;i<res.length;i++){
							System.out.print(res[i]);
						}
					}
					else{
						System.out.println(-1);
					}
				}
				//x가 큰 경우, -1 출력
				else if(N[0]<x){
					//-1 출력
					System.out.println(-1);
				}
			}
			else{ //3자리 수 이상
				
					if(N[0]>y){ //x, y값이 첫번째 시작값보다 작은 경우
						for(int i=0;i<n.length();i++){
						//결과가 나옴
						res[i]=y;
						}
						for(int i=0;i<res.length;i++){
							System.out.print(res[i]);
						}
					}
					else if (N[0]==x && N[0] <y && N[1] !=y){ //x값은 같지만 y값보다는 더 작은 경우 y값이 결과값 안에 들어가야하는데 들어갈 수 있는 지 뒤에 값을 계속 비교해줘서 각을 봐야함.
						//ex) 475555 4 8 의 경우 - N[1]보다 x값이 더 작아서 가능
						if(N[1]>x){
							res[0]=x;
							if(N[1]>y){ //ex) 475555 4 6 의 경우
								res[1]=y;
							}
							else res[1]=x;  //ex) 475555 4 8 의 경우 => 4488888
							for(int i=2;i<n.length();i++){ //2번째 숫자가 어떻게 됐든 작으니까 그 뒤에 나오는 숫자는 신경쓸거 없이 큰 y값 넣으면 됨.
								res[i]=y;
							}	
							for(int i=0;i<res.length;i++){
								System.out.print(res[i]);
							}
						}
						else if( N[1]<x){ //ex) 4155555 4 8의 경우 - N[1]보다 x값이 더 커서 불가능
							System.out.print(-1);
						}
					}
					else if (N[0]==x && N[1]==y){ //x, y 순서대로 값이 들어갈 수 있지만 다음 나오는 값들이 y보다 작거나 같은 값이 나와야함. y보다 큰값이 나오게 되면 -1 출력
						//ex) 4788858 4 7 의 경우 - N[2]값이 x보다 커서 가능
						res[0]=x;
						res[1]=y;
						
						for(int i=2;i<n.length();i++){
							
							if(N[i]>x){
								if(N[i]>=y){ //ex) 4788858/4777758  4 7 의 경우
									res[i]=y;
								}
								else if(res[i-1]<N[i-1]){ //앞에 값이 원래 값보다 더 작게 바뀌었다면 큰 값이 계속 나와도 됨!
									res[i]=y;
								}
								else{//ex) 4758858 4 7 의 경우  
									res[i]=x;
									// x=y;

								}
							}
							else if(N[i]<x){ //ex) 452555 4 5의 경우 - N[2]값이 x보다 작아서 불가능
								System.out.println(-1);
								break;
							}
							else if (N[i]==x){ //ex) 4544425 4 5의 경우 - N[5]값이 x보다 작아서 불가능
								res[i]=x;
							}

						}
						if(res[res.length-1]!=0){
							for(int i=0;i<res.length;i++){
								System.out.print(res[i]);
							}
						}
					}
					else if (N[0]<x){ //x값이 첫번째 자리보다 커버리면 값이 아예 만들어질 수가 없어서 -1 출력 
						System.out.print(-1);
						
					}
					else if (N[0]==y){ //첫번째 값이 x값보다는 작지만 y값과 같다면 뒤에 나오는 값 중 x보다 작은 값이 나와버리면 숫자를 만들수가 없음 -1 출력 (ex, 611111 4 6 일 경우) 그래서 각을 봄.
						
						if(N[1]>x){ //가능 (ex, 63555555 2 6 일 경우)
							
							res[0]=y;
							if(N[1]>y){//가능 (ex, 67555555 2 6 일 경우)
								res[1]=y;
							}
							else res[1]=x;
							
							for(int i=2;i<n.length();i++){
								if(res[i-1]<N[i-1]){ //앞에 값이 원래 값보다 더 작게 바뀌었다면 큰 값이 계속 나와도 됨!
									// System.out.println("--------------");
									res[i]=y;
									x=y;
								}
								else
									res[i]=x;
							}
							for(int i=0;i<res.length;i++){
								System.out.print(res[i]);
							}

						}

						else if(N[1]<x){ //불가능
							System.out.println(-1);
						}
						else if(N[1]==x){
						//ex) 325555  2 3 의 경우 - N[2]값이 x보다 커서 가능
							res[0]=y;
							res[1]=x;
							int flag=0;
							
							for(int i=2;i<n.length();i++){
								if(N[i]>y){
									if(res[i-1]<N[i-1]){ //앞에 값이 원래 값보다 더 작게 바뀌었다면 큰 값이 계속 나와도 됨!
										res[i]=y;
										
									}
									else res[i]=x;
								}
								else if(flag==1){
									res[i]=y;
								}
								else if(N[i]>=x){
									if(res[i-1]<N[i-1]){ //앞에 값이 원래 값보다 더 작게 바뀌었다면 큰 값이 계속 나와도 됨!
										res[i]=y;
										flag=1;
										
											
																	
									}
									
									else res[i]=x;

								}
								
								else if (N[i]<x){ //ex) 322211  2 3의 경우 - N[4]값이 x보다 작아서 불가능
									System.out.print(-1);
									break;
									
								}
								
								
							}
							if(res[res.length-1]!=0){
								for(int i=0;i<res.length;i++){
									System.out.print(res[i]);
								}
							}
							


						
						}
						

					}
					
				

			}
			System.out.println();

			

		}
	}
}