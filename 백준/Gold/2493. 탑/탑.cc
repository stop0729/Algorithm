#include <bits/stdc++.h>
using namespace std;



int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    stack<pair<int, int>> tower;
    
    cin >> n;
    tower.push({100000001, 0});
    
    for(int i=1; i<n+1; i++){
        int temp;
        cin >> temp;
        while(tower.top().first < temp){
            tower.pop();
        }
        cout << tower.top().second << ' ';
        tower.push({temp, i});
    }
    
}