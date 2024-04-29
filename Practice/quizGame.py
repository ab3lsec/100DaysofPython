
import random

questions = (
    "What is the capital city of France?",
    "Which planet is known as the Red Planet?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the chemical symbol for water?",
    "Who painted the Mona Lisa?",
    "What is the largest mammal in the world?",
    "In what year did the Titanic sink?",
    "What is the tallest mountain in the world?",
    "Who was the first person to step on the Moon?",
    "What is the powerhouse of the cell?"
)

options = (
    ["A. Paris", "B. London", "C. Berlin", "D. Rome"],
    ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
    ["A. Jane Austen", "B. William Shakespeare", "C. Charles Dickens", "D. Mark Twain"],
    ["A. NaCl", "B. CO2", "C. O2", "D. H2O"],
    ["A. Leonardo da Vinci", "B. Pablo Picasso", "C. Vincent van Gogh", "D. Michelangelo"],
    ["A. Elephant", "B. Giraffe", "C. Blue whale", "D. Hippopotamus"],
    ["A. 1910", "B. 1911", "C. 1912", "D. 1913"],
    ["A. Mount Everest", "B. K2", "C. Kangchenjunga", "D. Makalu"],
    ["A. Neil Armstrong", "B. Buzz Aldrin", "C. Yuri Gagarin", "D. John Glenn"],
    ["A. Nucleus", "B. Ribosome", "C. Mitochondria", "D. Chloroplast"]
)

answers = (
    "a. paris",
    "a. mars",
    "b. william shakespeare",
    "d. h2o",
    "a. leonardo da vinci",
    "c. blue whale",
    "c. 1912",
    "a. mount everest",
    "a. neil armstrong",
    "c. mitochondria"
)


currPrize = 0

usedNums= []


def selectQn(n):
    return questions[n]

def findAnswer(n):
    return answers[n]

def selectOptions(n):
    return options[n]


for i in range(1, 11):

    n = random.randint(0, 9)
    while n in usedNums:
        n = random.randint(0, 9)
    usedNums.append(n)

    question = selectQn(n)
    option = selectOptions(n)
    answer = findAnswer(n)

    print(i, ". ", question)
    for opt in option:
        print(opt)
    print("\n")


    userAns = input("Enter Your Answer: ").lower()
    print("\n")

    if userAns == answer[0].lower():
        print("Congrats, You got the Correct Answer!!")
        currPrize += 10000 * i
        print("Yout Account Balance is", currPrize)
        print("\n")
        continue

    else:
        print("Sorry, Your Answer is Wrong!!")
        currPrize -= 10000 * i
        if currPrize < 0:
            currPrize = 0
        print("Yout Account Balance is", currPrize)
        print("\n")


print("###########################")
print("\n")
print("THANK YOU TAKING THIS QUIZ!")
print("CONGRATS YOU'VE WON: ", currPrize)
print("\n")
print("###########################")


