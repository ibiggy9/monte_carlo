# monte_carlo
This is a python program that takes user input to define parameters for a random triangular monte carlo simulation for the purposes of producing the probabilities of outcomes to improve forecasting. 

The reason I used randomized triangle dist was because its the most adaptable distribution for most forecasts. 

This is a very simple first pass. What I would like to do is eliminate all globals and create classes that inheret the variables as methods to simplify the multiprocessing. 


To use:
1) Run in terminal
2) Enter the maximum possible value of your projection
3) Enter the minimum possible value of your projection
4) Enter the number that you think is most likely to occur across various iterations. 

How to interpret the output:

Terminal Output:
The terminal outputs the probability of various bins within the range provided occuring. In practice, you may combine a few of these buckets to tighten the range of your estimation. 

Graph Output:
The graph is mean't to show you the most likely outcomes and the upper and lower limits of your estimation. 
