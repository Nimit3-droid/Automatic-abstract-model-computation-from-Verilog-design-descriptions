/**
 *    author:  theHoodeyGuy   
**/
 
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
 
#define endl '\n'
#define nl '\n'

int dp[101][101][2];

int help(int e,int o,int s){

   // cout << e <<" "<<o<<" "<<s<<" "<<nl;
   if(o == 0){
      return 1^s;
   }

   if(e==0){
      if((o+1)%4) return s;
      return 1^s;
   }

   if(dp[e][o][s] != -1) return dp[e][o][s];

   int ans;

   if(s==0){
      //take even
      int ans1=1;
      if(e >= 2){
         ans1 = help(e-2,o,s);
      }
      ans1 = ans1 and help(e-1,o-1,s);

      //take odd
      int ans2=1;
      if(o >= 2){
         ans2 = help(e,o-2,1);
      }

      ans2 = ans2 and help(e-1,o-1,1);
      ans = ans1 or ans2;
   }

   else{
      //take even
      int ans1=1;
      if(e >=2){
         ans1 = help(e-2,o,s);
      }
      ans1 = ans1 and help(e-1,o-1,s);

      //take odd
      int ans2=1;
      if(o >=2){
         ans2 = help(e,o-2,0);
      }
      ans2 = ans2 and help(e-1,o-1,0);
      ans = ans1 or ans2;
   }
   return dp[e][o][s] = ans;
}

void solve(){

   int n;
   cin >> n;

   vector<int> a(n);

   int even = 0,odd = 0;

   for(int i=0;i<n;i++) {
      cin >> a[i];
      if(a[i]&1) odd++;
      else even++;
   }

   memset(dp,-1,sizeof(dp));

   cout << (help(even,odd,0) ? "Alice" : "Bob" )<< nl;
}
 
signed main()
{
   ios_base::sync_with_stdio(false);cin.tie(NULL);
 
   // #ifndef ONLINE_JUDGE
   //  freopen("input.txt", "r", stdin);
   //  freopen("output.txt", "w", stdout);
   // #endif
 
   int t ;
   cin>>t;
   while(t--)
   {
      solve();
   }
   
//    cerr<<"time taken : "<<(float)clock()/CLOCKS_PER_SEC<<" secs"<<endl;
   return 0;
}