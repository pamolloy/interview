/*
 * apple-stock/solution.c - A solution to the Apple Stock problem on Interview Cake
 *
 * gcc -pedantic -std=c99 -o solution solution.c; ./solution
 */

#include <stdio.h>
#include <assert.h>

int best_profit(int[], int);

int main() {
    int example[5] = {5, 10, 3, 5};
    int profit = best_profit(example, 5);
    printf("Best profit: %i\n", profit);
    //assert(4 == profit);
}

int best_profit(int stock_prices[], int length) {
    int best_profit = stock_prices[1] - stock_prices[0];
    int bottom = 0;   // Trailing index
    for (int i = 1; i < length; i++) {
        if (stock_prices[i] < stock_prices[bottom]) {
            bottom = i;
        }
        int increase = stock_prices[i] - stock_prices[bottom];
        if (increase > best_profit) {
            best_profit = increase;
        }
    }
    return best_profit;
}
