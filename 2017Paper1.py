# One method that can be used to compress text data is run length encoding (RLE). When RLE is used the compressed 
# data can be represented as a set of character/frequency pairs. When the same character appears in consecutive 
# locations in the original text it is replaced in the compressed text by a single instance of the character 
# followed by a number indicating the number of consecutive instances of that character. Single instances of a 
# character are represented by the character followed by the number 1.
# Figure 9 and Figure 10 show examples of how text would be compressed using this method.

# Figure 9
# Original text: AAARRRRGGGHH, Compressedtext: A 3 R 4 G 3 H 2

# Figure 10
# Original text: CUTLASSES, Compressed text: C 1 U 1 T 1 L 1 A 1 S 2 E 1 S 1

# Task 1:
# Write a program that will perform the compression process described above. The program should display a 
# suitable prompt asking the user to input the text to compress and then output the compressed text.
# Task 2:
# Test the program works by entering the text AAARRRRGGGHH.
# Task 3:
# Test the program works by entering the text A.

def Compression():
    wordToBeCompressed = input('Please enter text to be compressed: ')
    letters = list(wordToBeCompressed)
    output = ""
    i = 0
    while i < len(letters):
        count = 1
        while i+1 < len(letters) and letters[i] == letters[i+1]:
            count +=1
            i+=1
        output += letters[i] + str(count)
        i +=1
    print(output)

Compression()
