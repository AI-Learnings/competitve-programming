"""

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

"""

## Method 1   = ======= problem: Time complexity =========>

def minion_game(string):
    # your code goes here
    vowel = list('AEIOU')
    stuart = {'name':'Stuart', 'score':0, 'indices':[]}
    kevin = {'name':'Kevin', 'score':0, 'indices':[]}
    
    length = len(string)
    for i in range(length):
        if string[i] in vowel:
            kevin['score'] += 1
            for i in range(i+1, length):
                kevin['score'] += 1
        else:
            stuart['score'] += 1
            stuart['indices'].append(i)
            for i in range(i+1, length):
                stuart['score'] += 1

    if stuart['score'] > kevin['score']:
        print("{} {}".format(stuart['name'], stuart['score']))
    elif stuart['score'] < kevin['score']:
        print("{} {}".format(kevin['name'], kevin['score']))
    else:
        print("Draw")
    
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
    
    




# method 2 ====================================== Good ===========>


def minion_game(string):
    # your code goes here

    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print("Kevin {}".format(kevsc))
    elif kevsc < stusc:
        print("Stuart {}".format(stusc))
    else:
        print("Draw")
        
if __name__ == '__main__':