import json
import time
import random

#function to enter questions and answers, save test to json file

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
    
    save_test = input("Do you want to save the test to json file(yes/no?) ")
   
    if save_test == "yes":
        test_save(data_dict)
    else:
        return data_dict



#function to save test to json file
def test_save(data_dict):
    
    with open("test_data.json", "w", encoding="utf-8") as json_file:
        json.dump(data_dict, json_file, indent=4, ensure_ascii=False)
    


#function to open json file and load questions
def test_open():
    with open ("test_data.json", "r", encoding="utf-8") as json_file:
            return json.load(json_file)


             

#fuction to run the test: print questions, offer shuffling and allow user to enter answers
   
def test_print(load_test):
    
    answers_list = []

    shuffle_user = input("Do you want to shuffle questions before displaying the test (yes/no)?: ")

    if shuffle_user == "no":
        val = list(load_test.values())
        keys = list(load_test.keys())
        for i in range (len(load_test)):
            print(f"{i+1}. {keys[i]}")
            print(f"{",".join(val[i])}")
            answer_user = input("Enter your answer to the question: ")
            answers_list.append(answer_user)
            time.sleep(1)

    elif shuffle_user == "yes":
        qa_pairs = list(load_test.items())
        random.shuffle(qa_pairs)   

        for i, (question, answer) in enumerate(qa_pairs, 1):
            print(f"{i}. {question}")
            print(f"{",".join(answer)}")
            answer_user = input("Enter your answer to the question: ")
            time.sleep(1)
            answers_list.append(answer_user)
    
    save_option = input("Do you want to save the answers to json file (yes/no)? ")
    if save_option == "yes":
        save_answer_user(answers_list)
    else:
        return answers_list


#function to save user answers to json file
def save_answer_user(answers_list):
     with open("answers_list.json", "w", encoding="utf-8") as json_file:
          return json.dump(answers_list, json_file, indent=4, ensure_ascii=False)



data = test_input()
test_save(data)
load_test = test_open()
answers_list = test_print(load_test)



#interface
print("This is interactive test generator.")
print("Choose one of the options below:  ")
# 1 - create test
# 2 - load test from the file 
# 3 - take the test

 