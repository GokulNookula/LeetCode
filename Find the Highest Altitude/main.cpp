class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int max = 0;
        int current = 0;
        for (int i = 0; i < gain.size(); i++)
        {
            current += gain.at(i);
            if (current > max)
            {
                max = current;
            }
        }
        return max;
        
    }
};
