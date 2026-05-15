questions={
    "What is 73-21 ?": "52"
    "What is 5+9 ?": "14"
    "What is 7*4 ?": "28"
}
score = 0
for question, answer in questions. items():
    user_anser = input (question +" ").strip().capitalize()
    if user_answer == answer:
        print("correct!")
        score +=1
    else:
        print(f"Worng the correct answer is {answer}.")
    print(f"find score:{score}/{len(questions)}")