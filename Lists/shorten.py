"""
Shorten

Fill out the function shorten(lst, max_len) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is max_len items long. If lst is already shorter than max_len you should leave it unchanged. We've written a main() function for you which passes the SAMPLE_LIST and MAX_LENGTH constants into your function once you run the program; you can change the values of these constants to play around with different inputs!
"""

SAMPLE_LIST = ['a', 'b', 'c', 'd', 'e']
MAX_LENGTH = 3

def shorten(lst, max_len):
    # write your code below!
    while len(lst) > max_len:
        print(lst.pop())
    print(lst)    

def main():
    shorten(SAMPLE_LIST, MAX_LENGTH)

if __name__ == "__main__":
    main()

