class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int max_profit = 0;
        int currMin = prices[0];
        int curr_price;
        int curr_profit;
        for(int i = 0; i < prices.size(); i++){
            curr_price = prices[i];
            curr_profit = (curr_price - currMin);
            if (curr_profit > max_profit){
                max_profit = curr_profit;
            }
            currMin = std::min(currMin ,curr_price );



        }
        
        return max_profit;
    }
};
