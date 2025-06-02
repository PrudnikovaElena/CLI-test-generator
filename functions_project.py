import json
import time
import random

#function to enter questions and answers 

def test_input():
    data_dict = {}
    
    numb_quest = int(input("Enter number of questions: "))

##    if type(numb_quest) is not int:
##        print("Number of questions should be an integer.")

    for i in range (numb_quest):
        question_input = input("Enter question: ")
        answer_input = input("Enter answers (separated by comma): ")
        answers_list = answer_input.split(",")
        data_dict[question_input] = answers_list

    return data_dict

#function to save test to json file
def test_save(data_dict):
    
    with open("test_data.json", "w", encoding="utf-8") as json_file:
        json.dump(data_dict, json_file, indent=4, ensure_ascii=False)
    


#function to open json file and load questions
def test_open():
    with open ("test_data.json", "r", encoding="utf-8") as json_file:
            return json.load(json_file)

#function to shuffle questions
def questions_shuffle(load_test):
    qa_pairs = list(load_test.items())
    random.shuffle(qa_pairs)
    return qa_pairs
             

#fuction to run the test: print questions without shuffling and allow user to enter answers
        
def test_print(load_test):
    answers_list = []
    val = list(load_test.values())
    keys = list(load_test.keys())
    for i in range (len(load_test)):
        print(f"{i+1}. {keys[i]}")
        print(f"{",".join(val[i])}")
        answer_user = input("Enter your answer to the question: ")
        answers_list.append(answer_user)
        time.sleep(1)
    return answers_list

#function to run the test after shuffling
def test_shuffled_print(shuffled_test):
    answers_list = []
    for i, (question, answer) in enumerate(shuffled_test, 1):
         print(f"{i}. {question}")
         print(f"{",".join(answer)}")
         answer_user = input("Enter your answer to the question: ")
         answers_list.append(answer_user)
    return answers_list

#function to save user answers to json file
def save_answer_user(answers_list):
     with open("answers_list.json", "w", encoding="utf-8") as json_file:
          return json.dump(answers_list, json_file, indent=4, ensure_ascii=False)



data = test_input()
test_save(data)
load_test = test_open()
shuffled_test = questions_shuffle(load_test)
answers_list = test_print(load_test)
answers_list1 = test_shuffled_print(shuffled_test)
save_answer_user(answers_list)
save_answer_user(answers_list1)
