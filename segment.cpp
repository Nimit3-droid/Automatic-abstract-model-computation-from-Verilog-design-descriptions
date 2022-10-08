#include<bits/stdc++.h>
using namespace std;
#define ll long long

struct segmenttree {
    int n;
    vector<int> st;
    
    void init(int _n) {
        this->n = _n;
        st.resize(4 * _n, 0);
    }

    void build(int start, int end, int node, vector<int> &v) {
        if (start == end) {
            st[node] = v[start];
            return;
        }
        int mid = (start + end) / 2;
        
        // left subtree : [start, mid]
        build(start, mid, 2 * node + 1, v);
        
        // right subtree : [mid+1, end]
        build(mid + 1, end, 2 * node + 2, v);

        // IMPORTANT : compute for current node
        st[node] = st[2 * node + 1] ^ st[2 * node + 2];
    }

    int query(int start, int end, int l, int r, int node) {
        if (start > r || end < l) { // Non overlapping
            // IMPORTANT : return something that won't affect the ans
            return 0;
        }

        if (start >= l && end <= r) {   // completely overlapping
            return st[node];
        }
        // Partial overlapping
        int mid = (start + end) / 2;
        int q1 = query(start, mid, l, r, 2 * node + 1);
        int q2 = query(mid + 1, end, l, r, 2 * node + 2);
        // compute query ans
        return q1 ^ q2;
    }


    void update(int start, int end, int node, int idx, int val) {
        if (start == end) {
            st[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) {   // Left subtree
            update(start, mid, 2 * node + 1, idx, val);
        } else {            // Right subtree
            update(mid + 1, end, 2 * node + 2, idx, val);
        }
        // making changes to nodes
        st[node] = st[2 * node + 1] ^ st[2 * node + 2];
    }


    void build(vector<int> &v) {
        build(0, n - 1, 0, v);
    }

    int query(int l, int r) {
        return query(0, n - 1, l, r, 0);
    }

    void update(int idx, int val) {
        update(0, n - 1, 0, idx, val);
    }

};
// elements
// 1 2 3 2
// [1,3] 1 2 3
// 3
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);


    int n;
    cin >> n;
    vector<int> array(n);
    for (auto &ai : array) {
        cin >> ai;
    }
    segmenttree tree;
    tree.init(n);
    tree.build(array);
    
    return 0;
}
