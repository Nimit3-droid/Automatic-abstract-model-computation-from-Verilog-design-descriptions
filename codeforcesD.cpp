#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

void solve(){
    int n;
    cin >> n;

    vector<int> spend(n);
    vector<int> budget(n);
    // int a;

    for(int i = 0; i < n; i++){
        cin >> spend[i];
    }

    for(int i = 0; i < n; i++){
        cin >> budget[i];
    }

    vector<int> surplus;
    for(int i = 0; i < n; i++){
        surplus.push_back(budget[i]-spend[i]);
    }

    sort(surplus.begin(), surplus.end());

    int i = 0;
    int j = n-1;

    int grp = 0;

    while(i < j){
        if(surplus[j] + surplus[i] >= 0){
            grp++;
            i++;
            j--;
        }
        else{
            i++;
        }
    }

    cout << grp << endl;
}

int main(){
// #ifndef MYNK
//     freopen("input.txt", "r", stdin);
//     freopen("output.txt", "w", stdout);
// #endif
    int t;
    cin >> t;
    while(t--){
        solve();
    }

    return 0;
}
