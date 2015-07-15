You decide to test if your oddly-mathematical heating company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee#.

Write a class TempTracker with these methods:

* `insert()` - records a new temperature
* `get_max()` - returns the highest temp we've seen so far
* `get_min()` - returns the lowest temp we've seen so far
* `get_mean()` - returns the mean # of all temps we've seen so far
* `get_mode()` - returns the mode # of all temps we've seen so far

Optimize for space and time. Favor speeding up the `get_` functions over speeding up the `insert()` function.

`get_mean()` should return a float, but the rest of the `get_` functions can return integers. Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..1100..1100..110.

If there is more than one mode, return any of the modes.

Problem from [Interview Cake](https://www.interviewcake.com/).
