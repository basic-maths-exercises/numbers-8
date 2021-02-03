# Constructing numbers using multiplication

You possibly found writing a program to generate the Roman numerals to be a bit of a pain.  What 'av the Roman's ever done for us eh? Monty Python asside I hope we can all agree that the Roman system of number is much less elegant than the system that was developed by the Arabs.  

It is still worth looking at the Roman system of number, however, as there is an interesting difference between these systems of number.  In the Arabic number system, a combination of multiplication and addition is used when constructing the final number from the symbols that have been written down.  In the Roman system, by contrast, the values associated with each of the symbols are simply added.  In other words, no multiplication is used in the algorithm that converts a list of Roman numerals into the final number.

The Roman system is an extension on what is arguably the most ancient number system: the tally.  In this system of number, notches were carved into a stick.  The number this represents is then equal to the total number of notches in the stick.   IIIIIIII on a tally stick is thus used to represent the number eight.  

The tally system of number is interesting as only one symbol (I) and one operation (addition) are required to represent all the natural numbers.  Given this one might, therefore, ask: how many symbols are required to represent all the natural numbers if we design our system of representing numbers around multiplication?  Over the next few tasks, we are thus going to investigate this question.   

__To complete the task, I would like you to write a function called `genMultiplications` which takes a single integer `N` as input.  This function should then return the set of numbers that can be constructed by taking all `N`x`N` possible products of the `N` non-negative integers that are less than `N`.__  As you are returning a set here each of the numbers will only only included once.  If your function was run for `N=2` the output should thus be a set containing 0 and 1.

To get you started, if you were to call your function `genMultiplications` with 1 as input you would need to calculate the following four products:

![](https://render.githubusercontent.com/render/math?math=0\times\0\qquad\0\times\1\qquad\1\times\0\qquad\1\times\1)

Notice that these four products are calcualted and printed by the following code:

````
for i in range(2) : 
    for j in range(2) : print( i*j )
````
 
Notice, last of all that in this exercise I want you to use a new type of python object called a set.  A set is different from a Python list or a NumPy array as:

- The data in a set is unordered and unindexed.  You thus cannot use the square bracket syntax you have seen for NumPy arrays and lists to get the value of the nth element.  You must always access the whole set at once.
- A set cannot contain multiple copies of the same object.  In other words, while you can have a NumPy array that has all N>0 elements that are all equal to zero, you will only ever have one zero in a set.

To create a called myset that contains a 1 and to add a 2 to it you use commands like these ones:

````
myset = set([1])
myset.add(2)
```` 

Run your function for various values of `N` before you submit.  Is it possible to generate all the natural numbers by performing multiplications?  What numbers are missing?
