import json

def save_user(user_text, victories, draws, defeats):
    try:
        with open("password_file.json", "r") as user_list:
            users = json.load(user_list)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        users = []
    if not test_user(user_text, users):
        new_user = {
            "username": user_text,
            "victories": victories,
            "draws": draws,
            "defeats": defeats
        }
        users.append(new_user)
        with open("password_file.json", "w") as user_list:
            json.dump(users, user_list)
    else:
        print("User already exists")

def test_user(user_text, users):
    for user in users:
        if user["username"] == user_text:
            return True
    return False
