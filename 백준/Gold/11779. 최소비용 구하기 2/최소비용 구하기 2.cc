#include <bits/stdc++.h>
using namespace std;

int v, e, st, ed;

vector<pair<int, int>> adj[1005];
const int INF = 1e9 + 10;
int d[1005];
int pre[1005];

int main(void){
    cin >> v >> e;
    fill(d, d+v+1, INF);
    
    while(e--){
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({w, v});
    }
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    cin >> st >> ed;

    d[st] = 0;
    pq.push({d[st], st});
    while(!pq.empty()){
        int now = pq.top().second;
        int dist = pq.top().first;
        pq.pop();
        if(d[now] != dist) continue;
        for(int i=0; i<adj[now].size(); i++){
            int cost = dist + adj[now][i].first;
            int next_node = adj[now][i].second;
            
            if(d[next_node] > cost){ // 새로운 경로가 더 짧은 경우에만
                d[next_node] = cost;
                pq.push({cost, next_node});
                pre[next_node] = now;
            }
        }
    }
    
    cout << d[ed] << '\n';

    vector<int> path;
    int cur = ed;
    while (cur != st){
        path.push_back(cur);
        cur = pre[cur];
    }
    path.push_back(cur);
    reverse(path.begin(), path.end());

    
    cout << path.size() << '\n';
    
    for (auto x : path) cout << x << ' ';

}