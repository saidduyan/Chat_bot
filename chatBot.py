import json
from difflib import get_close_matches


def database_load():
    with open('C:\\Users\\Said\\OneDrive\\Masaüstü\\ChatBot\\dataBase.json', 'r') as file:
        return json.load(file)
    
def database_write(datas):
    with open('C:\\Users\\Said\\OneDrive\\Masaüstü\\ChatBot\\dataBase.json', 'w') as file:
        json.dump(datas, file,  indent=2)

def close_matches(ask, asks):
    matches= get_close_matches(ask, asks, n=1, cutoff=0.6)
    return matches[0] if matches else None

def find_answer(ask, dataBase):
    for ask_answers in dataBase["asks"]:
        if ask_answers["ask"]== ask:
            return ask_answers["answer"]
    return None


def chatBot():
    database = database_load()

    while True:
        ask = input("you : ")
        if ask == "exit":
            break

        feedback = close_matches(ask, [ask_answers["ask"] for ask_answers in database["asks"]])
        if feedback:
            given_answer = find_answer(ask, database)
            print(f"Bot : {feedback}")


        else:
            print(f"Bot: I dont know how to respond but maybe you can teach me.")
            new_answer = input(" you can write for teaching or 'quit' : ")

            if new_answer!= 'quit':
                database["asks"].append({
                    "ask": ask,
                    "answer": new_answer
                })
                database_write(database)
                print("Bot : Thanks, I learned new things thanks to you :D")

if __name__== '__main__':
    chatBot()