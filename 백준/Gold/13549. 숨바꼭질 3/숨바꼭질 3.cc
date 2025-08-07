#include <bits/stdc++.h>

using namespace std;

int N, M;
int sis[100000+1];
queue<int> q;

int main(){
    cin >> N >> M;
    q.push(N);
    fill(sis, sis+100000+1, -1);
    sis[N] = 0;
        
    while(!q.empty()){
        int out = q.front();
        q.pop();
        
        int arr[] = {out, -1, 1};
        
        for(int i : arr){
            int temp = out + i;
            if (0<= temp && temp <= 100000){
                if (sis[temp] == -1){
                    if (i == out){
                        sis[temp] = sis[out];
                        q.push(temp);
                    }
                    else{
                        sis[temp] = sis[out] + 1;
                        q.push(temp);
                    }
                }
            }
        }
    }
    cout << sis[M];
}