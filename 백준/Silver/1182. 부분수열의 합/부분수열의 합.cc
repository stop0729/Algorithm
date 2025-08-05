#include <bits/stdc++.h>
using namespace std;

int n, m;
bool isused[20];
int arr[20];
int total = 0;
int result;

void func(int c, int t){
    if (c==n){
        if (t==m) result += 1;
        return;
    }
    
    func(c+1, t);
    func(c+1, t+arr[c]);

}

int main(){
    cin >> n >> m;

    for(int i=0; i<n; i++){
        int temp;
        cin >> arr[i];
    }

    func(0, 0);
    if (m==0) result -= 1;

    cout << result;
}