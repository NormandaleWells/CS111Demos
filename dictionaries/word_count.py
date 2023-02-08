'''
word_count.py - program to count word frequencies in a text file

usage: python word_count.py <in_file> <out_file>
    <in_file>   - the name of the input file
    <out_file>  - the name of the output file containing the word counts

This module is over-commented for pedagogical purposes.
'''

import sys

'''
get_word_counts

This function creates a dictionary mapping each word in the given file
to the number of times in appears in the text.

Parameters:
    filename - the name of the file to analyze
'''
def get_word_counts(filename):
    f = open(filename, "r")

    # Start with an empty dictionary.
    counts = {}

    # For each line in the file, start by splitting it into words.
    for line in f:
        words = line.strip().split()

        # if the word is in the dictionary, add 1 to its current count.
        # Otherwise, create a new entry with a count of 1.
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    return counts

'''
print_word_counts

This function writes the dictionary of word counts to the a file.

Parameters:
    counts  - the dictionary of word counts
    f       - the file (not the filename!) to write to
'''
def print_word_counts(counts, f):
    for word,count in counts.items():
        # print() has a named parameter which we can use to
        # specify the file to write to.
        print(f"{word:>20} : {count}", file=f)


'''
print_sorted_word_counts

This function writes the dictionary of word counts to the a file,
in order from most frequently to least frequently used

Parameters:
    counts  - the dictionary of word counts
    f       - the file (not the filename!) to write to
'''
def print_sorted_word_counts(counts, f):

    # Get all the key/value pairs as a list.
    item_list = list(counts.items())

    # Sort the list, using the value (the second item in the key/value
    # tuple) as the key.
    item_list.sort(key = lambda item: item[1], reverse=True)

    # Print the sorted list.
    for word,count in item_list:
        # print() has a named parameter which we can use to
        # specify the file to write to.
        print(f"{word:>20} : {count}", file=f)


if __name__ == "__main__":

    # Get the actual program arguments.  (Index 0 contains the
    # program name.)  If there are none, print a usage statement.
    args = sys.argv[1:]
    if len(args) == 0:
        print("usage: python word_count.py <in_file> <out_file>")
        sys.exit(0)

    # We know now that args[0] is the input file, so we can
    # go get the word counts.
    word_counts = get_word_counts(args[0])

    # If there was only 1 program argument, there is no output
    # file; write the results to standard output.
    if len(args) == 1:
        print_word_counts(word_counts, sys.stdout)
    
    # Otherwise, we have an output file.  Open it, and write
    # the results there.
    else:
        f = open(args[1], "w")
        print_word_counts(word_counts, f)
        f.close()
