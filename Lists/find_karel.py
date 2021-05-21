"""
Where's Karel?

Fill in the function find_karel(roster) which takes in a list, roster, and prints "Karel is here!" if 'karel' is an element in roster, or prints "Karel isn't here." if 'karel' isn't an element in roster. You can assume all elements in roster will be lowercase. 

We've written some DocTests for you (and note that DocTests are very picky about output -- make sure you're printing exactly "Karel is here!" or "Karel isn't here.") and also written a main() function which passes the SAMPLE_ROSTER constant into find_karel(roster). You can change SAMPLE_ROSTER or add DocTests to test your code with different inputs.
"""

SAMPLE_ROSTER = ['miranda', 'karel', 'shrek', 'donkey']

def find_karel(roster):
    """
    Prints whether or not Karel is in the roster.
    >>> find_karel(['chris', 'mehran'])
    Karel isn't here.
    >>> find_karel(['karel', 'is', 'here'])
    Karel is here!
    """
    # write your code below!
    if 'karel' in roster:
        print("Karel is here!")
    else:
        print("Karel isn't here.")    
    
def main():
    find_karel(SAMPLE_ROSTER)

if __name__ == "__main__":
    main()
