//COLOR THE PICTURE

#include<bits/stdc++.h>
using namespace std;

void solve(){

    //the picture will be strip of rows with col more than 2 or strip of cols with row more than 2

    int n,m,k;
    cin >> n >> m >> k;

    vector<int> a(k);

    for(int i=0;i<k;i++) cin >> a[i];

    long long cols = 0;
    int flag = 0;
    for(int i=0;i<k;i++){
        if(a[i]/n > 2) flag = 1;
        if(a[i]/n >=2) cols += a[i]/n;
    }

    if(cols >= m && (flag || m%2==0)){
        cout << "YES" << endl;
        return;
    }

    long long rows = 0;
    flag = 0;
    for(int i=0;i<k;i++){
        if(a[i]/m > 2) flag = 1;
        if(a[i]/m >=2) rows += a[i]/m;
    }

    if(rows >= n && (flag || n%2==0)){
        cout << "YES" << endl;
        return;
    }

    cout << "NO" << endl;
}

int main()
{
   #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
   #endif

   int t;
   cin>>t;

   while(t--)
   {
      solve();
   }
   
   cerr<<"time taken : "<<(float)clock()/CLOCKS_PER_SEC<<" secs"<<endl;
   return 0;
}
