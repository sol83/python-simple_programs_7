"""
Get last element

Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
"""

SAMPLE_LIST = [1, 2, 3, 'a', 'b', 'c']

def get_last_element(lst):
    # write your code below!
    print(lst[-1])
    # using the pop() function could also give us the last element of the list, this way however the list would be mutated
    # print(lst.pop())
    # print(SAMPLE_LIST)

def main():
    get_last_element(SAMPLE_LIST)

if __name__ == "__main__":
    main()
