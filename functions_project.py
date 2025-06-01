import json
import time

#function to enter questions and answers and save them to json file

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
    with open ("test_data.json", "r", encoding="utf-8")as json_file:
            return json.load(json_file)

#function to shuffle answers
        

#fuction to print questions and answers with timesleep
#need to add the ability to enter and save answers
        
def test_print(load_test):
    
    val = list(load_test.values())
    keys = list(load_test.keys())
    for i in range (len(load_test)):
        print(f"{i+1}. {keys[i]}")
        print(f"{",".join(val[i])}")
        time.sleep(1)
    

        
data = test_input()
test_save(data)
load_test = test_open()
test_print(load_test)
