#include <iostream>
#include <cstring>
#include <fstream>
#include <cstdlib>
#include <sstream>
using namespace std;
ifstream finCost("cost.txt");
ifstream finQ("q.txt");
ofstream fout("DPresult.txt");
#define maxN 1000
#define INF 999999

int cost[maxN][maxN];
int q[maxN];
int f[200][50][5000];
int a[200][50][5000][2]; //save the assignment

int n = 150;
int m = 10; 
int R = 10;
int cmax = 27;
int qB = 0;

int main(){
	//input
	for(int i = 0; i < m; i++)
		for(int j = 0; j < n; j++){
			finCost>>cost[i][j];
		}	
	for(int j = 0; j < n; j++){
		//finQ>>q[j];
		q[j] = 50;
	}
	qB = 5000;
	//initialization
	memset(f, 0, sizeof(f));
	for(int i = 0; i < m; i++){
		f[0][i][cost[i][0]] = q[0];
	}
	
	int fmax = 0;	
	int lastK = 0;  
	bool selected = true; 
	//dp
	for(int j = 1; j < n; j++){
		for(int i = 0; i < m; i++){
			for(int c = 0; c < n*cmax+1; c++){
				if(c < cost[i][j]) continue;
				fmax = 0;
				for(int k = 0; k < m; k++){
					if(f[j-1][k][c] > fmax){
						fmax = f[j-1][k][c];
						lastK = k;
						selected = false; //did not select f[j][i][c] 
					}
					if(f[j-1][k][c-cost[i][j]]+q[j] > fmax){
						fmax = f[j-1][k][c-cost[i][j]]+q[j];
						lastK = k;
						selected = true; //selected f[j][i][c]
					}
				}
				
				f[j][i][c] = fmax;
				
				if(selected){
					a[j][i][c][0] = 1;
					a[j][i][c][1] = lastK;
				}
				else{
					a[j][i][c][0] = 0;
					a[j][i][c][1] = lastK;
				}
				
			}
		}
	}
	
	int resj, resi, resc;
	int cmin = INF;
	for(int j = 0; j < n; j++){
		for(int i = 0; i < m; i++){
			for(int c = 0; c < n*cmax+1; c++){
			if(f[j][i][c] >= qB)
				if(c < cmin){
					cmin = c;
					resj = j; resi = i; resc = c;
				}
			}
		}
	}
	
	
	int nowi = resi;
	int nowc = resc;
	int temp;
	for(int j = resj; j >= 0; j--){
		if(a[j][nowi][nowc][0] == 0){  //if did not select i,j
			nowi = a[j][nowi][nowc][1];
			continue;
		}
		else{ //if selected i,j
			fout<<nowi<<"\t"<<j<<endl;
			temp = nowi;
			nowi = a[j][nowi][nowc][1];
			nowc -= cost[temp][j];
		}
	}
	cout<<cmin<<endl;
	cout<<qB<<endl;
	cout<<f[resj][resi][resc];
//	cout<<res<<endl;
		
	
}
