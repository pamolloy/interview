I have an array `stock_prices_yesterday` where:

* The indices are the time in minutes past trade opening time, which was 9:30am local time.
* The values are the price in dollars of Apple stock at that time.

For example, the stock cost $500 at 10:30am, so `stock_prices_yesterday[60] = 500.`

Write an efficient algorithm for computing *the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.*

No "shorting"-you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).

Problem from by [Interview Cake](https://www.interviewcake.com/question/stock-price).
