#!/usr/bin/python3
"""Trivia Game with the Trivia API"""

from pprint import pprint 

import requests

from random import randint
from random import shuffle

base_url = "https://opentdb.com/api.php?"

def main():

    print("Welcome! I'm going to give you some trivia questions. Ready?")
    print("How many questions do you want?") 
    amount = input(">>> ")

    print("How difficult do you want the questios? easy, medium, hard")
    difficulty = input(">>> ")
    
    while difficulty not in ("easy", "medium", "hard"):
        print("Difficulty not found. Must be: easy, medium or hard")
        difficulty = input(">>> ")

    trivia = requests.get(base_url + f"amount={amount}&difficulty={difficulty}")
    trivia = trivia.json()
    
    question_dict = trivia.get("results")
     
    print("\n")

    num = 1
    for q in question_dict:
        print(f"Question {num}: {q['question']}")
        answers = q['incorrect_answers']
        answers.append(q['correct_answer'])

        shuffle(answers)
        correct = answers.index(q['correct_answer']) + 1

        x = 1
        for a in answers:
            print(f"{x}) {a}")
            x += 1
        
        print("Enter your guess (1, 2, 3, or 4)")
        guess = input(">>> ")
        
        print(f"Your guess: {answers[int(guess) - 1]}")
        print(f"Correct answer: {q['correct_answer']}\n")

        if guess == str(correct):
            print("Correct!\n")
        else:
            print("Sorry, that is incorrect.\n")

        input()   

        num += 1
                


if __name__ == "__main__":
    main()
