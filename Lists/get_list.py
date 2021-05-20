"""
Get list

Write a program in get_list.py which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

Here's a sample run:

$ python get_list.py
Enter a value: 1
Enter a value: 2
Enter a value: 3
Enter a value: 
Here's the list:
['1', '2', '3']
"""

def main():
    # write your code below!
    lst = []
    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        lst.append(value) 
    print("Here's the list:")
    print(lst)

if __name__ == "__main__":
    main()
