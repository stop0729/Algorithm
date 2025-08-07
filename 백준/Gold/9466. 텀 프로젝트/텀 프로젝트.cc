#include <bits/stdc++.h>

using namespace std;

int arr[100005];
int n;
int state[100005];

int NOT_VISITED = 0;
int IN_CYCLE = -1;

void run(int x){
    int cur = x;
    while(true){
        state[cur] = x;
        cur = arr[cur];
        
        if(state[cur] == x){
            while(state[cur] != IN_CYCLE){
                state[cur] = IN_CYCLE;
                cur = arr[cur];
            }
            return;
        }
        else if(state[cur] != 0) return;
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while(t--){
        cin >> n;
        fill(state+1, state+n+1, 0);
        for(int i=1; i<n+1; i++) cin >> arr[i];
        for(int i=1; i<n+1; i++){
            if(state[i] == NOT_VISITED) run(i);
        }
        int ans = 0;
        for(int i=1; i<n+1; i++){
            if(state[i] != IN_CYCLE) ans += 1;
        }
        cout << ans << '\n';
    }
}