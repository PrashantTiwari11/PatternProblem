"""
W
WO
WOW
WO
W
"""
word = str(input("Enter your word: "))
for i in range(1,len(word)+1):
    print(word[0:i])
for i in range(len(word)-1,0,-1):
    print(word[0:i])