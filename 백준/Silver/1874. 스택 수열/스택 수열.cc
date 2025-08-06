#include <bits/stdc++.h>

using namespace std;

int n;

int main(){
    cin >> n;
    stack<int> st;
    int cnt = 1;
    string ans;
    
    while(n--){
        int t;
        cin >> t;
        while(cnt <=t){
            st.push(cnt);
            cnt ++;
            ans += "+\n";
        }
        if(st.top() != t){
            cout << "NO\n";
            return 0;
        }
        st.pop();
        ans += "-\n";
    }
    cout << ans;
}