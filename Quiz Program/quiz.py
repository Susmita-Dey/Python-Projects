# a dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop through the dictionary using the key value pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1": {
        "question": "What is the capital of India?",
        "answer": "Dehli"
    },
    "question2": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question7": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct answer!!')
        score += 1
        print("Your current score: "+str(score))
        print("")
    else:
        print('Wrong answer!!')
        print("The correct answer would be " + value["answer"])
        print("Your current score: "+str(score))
        print("")

print("You got "+str(score)+" out of 7 questions correctly.")
print("Your percentage is "+str(int(score/7 * 100))+"%")
