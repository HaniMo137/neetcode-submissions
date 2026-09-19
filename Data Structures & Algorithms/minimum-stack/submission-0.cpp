class MinStack {
public:
    vector<int> s;
    vector<int> mins;
    MinStack() {
    }
    
    void push(int val) {
        if (s.empty())
           mins.push_back(val);
        s.push_back(val);
        if ((val <= mins.back())&&(mins.size()> 0))
            mins.push_back(val);
    }
    
    void pop() {
        if (s.back() == mins.back())
            mins.erase(mins.end()-1);
        s.erase(s.end()-1);
    }
    
    int top() {
        return s.back();
    }
    
    int getMin() {
        return mins.back();
    }
};
