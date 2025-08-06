#include <bits/stdc++.h>
using namespace std;

int v, e, st;

vector<pair<int, int>> adj[20005];
const int INF = 1e9 + 10;
int d[200005];
int main(void){
    cin >> v >> e >> st;
    fill(d, d+v+1, INF);
    
    while(e--){
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({w, v});
    }
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    d[st] = 0;
    pq.push({d[st], st});
    while(!pq.empty()){
        int now = pq.top().second;
        int dist = pq.top().first;
        pq.pop();
        if(d[now] != dist) continue;
        for(int i=0; i<adj[now].size(); i++){
            int cost = dist + adj[now][i].first;
            if(d[adj[now][i].second] < cost) continue;
            d[adj[now][i].second] = cost;
            pq.push({cost, adj[now][i].second});
        }
    }
    
    for(int i=1; i<=v; i++){
        if(d[i] == INF) cout << "INF\n";
        else cout << d[i] << "\n";
    }
}