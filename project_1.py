import random

def shuffleWord(wrd):
    pw=random.sample(wrd,k=len(wrd))
    return ''.join(pw)

def printpuzzleQuestion(word,score):
    problemword=shuffleWord(word)
    print("\nArrange the letters to form a valid ")
    print(problemword)
    userWord=input()
    print()
    if userWord.upper()==word:
        print("correct")
        score+=1
    else:
        print("Wrong")
        score-=1
        return score

def main():
    score = 0
    words=["FATHER", "BREAK", "COUNTRY", "GREEN"]
    words=random.sample(words,k=len(words))

    for word in words:
        score=printpuzzleQuestion(word,score)



        print("Your Score is",score)
        print()

main()