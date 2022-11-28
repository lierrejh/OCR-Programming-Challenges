# Write a program that gets two words from the user and then displays a message saying 
# if the first word can be created using the letters from the second word or not.
# For example:
# • The word EAT can be formed from the word ATE as the first word uses one E, 
# one A and one T and the second word also contains one of each of these letters.
# • The word EAT can be formed from the word HEART as the second word contains one E,
#  one A and one T which are the letters needed to form the first word.
# • The word TO can be formed from the word POSITION as the second word contains one T 
# and (at least) one O which are the letters needed to form the first word.
# • The word MEET cannot be formed from the word MEAT as the second word only contains
# one E and two Es are needed to form the first word.
# You may assume that the user will only enter words that consist of upper case letters.

def main(word1, word2):
    print("We will see if word 1 can be made with the letters of word 2")
    word1list = list(word1) #abba
    word2list = list(word2) #abbc
    try:
        for i in word1list: word2list.remove(i)
        print("Yes, word 1 can be made with the letters of word 2")
    except: 
        print("Word 1 can't be made with the letters of word 2")

word1 = input("Enter word 1: ")
word2 = input("Enter word 2: ")
main(word1, word2)