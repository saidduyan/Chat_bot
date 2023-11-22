import json
import os
from difflib import get_close_matches

DATABASE_PATH = os.path.join(os.path.expanduser("~"), "OneDrive", "Masaüstü", "ChatBot", "dataBase.json")

def database_load():
    with open(DATABASE_PATH, 'r') as file:
        return json.load(file)

def database_write(datas):
    with open(DATABASE_PATH, 'w') as file:
        json.dump(datas, file, indent=2)

def close_matches(ask, asks):
    matches = get_close_matches(ask, asks, n=1, cutoff=0.6)
    return matches[0] if matches else None

def find_answer(ask, dataBase):
    for ask_answers in dataBase["asks"]:
        if ask_answers["ask"] == ask:
            return ask_answers["answer"]
    return None

def chatBot():
    database = database_load()

    while True:
        ask = input("you : ")
        if ask.lower() == "exit":
            break

        feedback = close_matches(ask, [ask_answers["ask"] for ask_answers in database["asks"]])
        if feedback:
            given_answer = find_answer(feedback, database)
            print(f"Bot : {given_answer}")
        else:
            print("Bot: I don't know how to respond, but maybe you can teach me.")
            new_answer = input("You can write for teaching or 'quit': ")

            if new_answer.lower() != 'quit':
                database["asks"].append({
                    "ask": ask,
                    "answer": new_answer
                })
                database_write(database)
                print("Bot : Thanks, I learned new things thanks to you :D")

                # Recalculate feedback after adding a new answer
                feedback = close_matches(ask, [ask_answers["ask"] for ask_answers in database["asks"]])
                if feedback:
                    given_answer = find_answer(feedback, database)
                    print(f"Bot : {given_answer}")

if __name__ == '__main__':
    chatBot()
