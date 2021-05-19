"""
Get first element

Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty.

You can change the items in the SAMPLE_LIST list to test your code!
"""

SAMPLE_LIST = [1, 2, 3, 'a', 'b', 'c']

def get_first_element(lst):
    # write your code below!
    print(lst[0])

def main():
    get_first_element(SAMPLE_LIST)

if __name__ == "__main__":
    main()
