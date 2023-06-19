class Solution {
public:
    int romanToInt(string s) {
        int total = 0;
        for (int i = 0; i < s.size(); i++)
        {
            if (i + 1 < s.size())
            {
                if (value(s[i]) >= value(s[i+1]))
                {
                    total += value(s[i]);
                }
                else
                {
                    total = total + value(s[i+1]) - value(s[i]);
                    i++;
                }
            }
            else
            {
                total += value(s[i]);
            }
        }
        return total;
    }

    int value(char r)
    {
        if (r == 'I')
        {
            return 1;
        }
        else if (r == 'V')
        {
            return 5;
        }
        else if (r == 'X')
        {
            return 10;
        }
        else if (r == 'L')
        {
            return 50;
        }
        else if (r == 'C')
        {
            return 100;
        }
        else if (r == 'D')
        {
            return 500;
        }
        else if (r == 'M')
        {
            return 1000;
        }
        return -1;
    }
};
