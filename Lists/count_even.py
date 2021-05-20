"""
Count even

Fill out the function count_even(lst) which takes in a list of integers and prints the number of even numbers in the list. We've added some DocTests you can use to check your code, just press the Check button in the bottom right corner. We've also written a main() function for you which inputs the constant SAMPLE_LIST; you can change this to whatever input you'd like, or add more DocTests!
"""

SAMPLE_LIST = [1,2,3,4,5,6]

def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    # write your code below!
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    # here's another way to do this same thing, with a different kind of for loop:
    # for i in range(len(lst)):
    #     num = lst[i]
    #     if num % 2 == 0:
    #         count += 1
    print(count)   

def main():
    count_even(SAMPLE_LIST)

if __name__ == "__main__":
    main()
