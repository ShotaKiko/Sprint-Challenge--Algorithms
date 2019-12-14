#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime would be O(n) as the number of times you loop through
incease n times


b)You have two loops, while i goes through range(n) as well as j < n so this is
O(n^2)


c)O(n) -- recursive and a linear relationship 

## Exercise II

A strategy top minimize dropped and broken eggs roughly means less iterations to find f.

By utilizing a binary search we can achieve O(log n) plus floors themselves are ordered so makes sense to proceed this way.

f = the floor/threshold where and egg throw means breaking the egg
n = floor/story of the building

def find_floor_of_humpty_dumptys_demise(n,f):

//1.) In a binary search first you find the middle and set it be the current floor youre evaluating

    current_floor =((n[0] + n[-1])/2) //floor at first index + floor at last / 2

//2.) Now that you know how you would evaluate your intial current floor set your base case. The egg breaks on threshold or f so

    if egg breaks on current_floor but is intact on current_floor - 1
        return middle // and you have found f

//3.) Since we a base case now we can use recusrion to get this this base case and find f
    
    if the egg breaks on current_floor and current_floor - 1 floor then the threshold is at a lower floor than we are considering now so
    return the functions and pass in floors that would be lower as n

    return find_floor_of_humpty_dumptys_demise(n[:current_floor],f): 
    //:current_floor(our current considered as middle) means from start to this index not including middle itself

    OR

    if the egg doesnt break on the current floor and thereby not on current_floor -1 floor either then our threshold is at a higher floor and we need to return the function and pass in higher floors as n

    return find_floor_of_humpty_dumptys_demise(n[current_floor:],f):
    // current_floor: (our current considered as middle) means from this index to the end of the array as we need a higher floor as n to determine threshold

So using binary search and then recursion we can achieve n/2 solution or once again a O(log n) runtime minimizing egg usage and earning humpty's favor





