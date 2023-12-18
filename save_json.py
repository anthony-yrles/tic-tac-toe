import json

def save_user(user_text):
    try:
        with open("password_file.json", "r") as user_list:
            users = json.load(user_list)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        users = []
    test_user(user_text, users)
    users.append(user_text)
    with open("password_file.json", "w") as user_list:
        json.dump(users, user_list)

def test_user(user_text, users):
    while True:
        for i in users:
            if i == user_text:
                print("existe déjà")
        break