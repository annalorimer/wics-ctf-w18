This is an integer overflow problem. 

1. We know that the backend is adding tax but it's also checking if we put in a number that's bigger than INT_MAX. 
2. Put in a number that's less than INT_MAX but when 13 is added to it it's bigger than INT_MAX. 
