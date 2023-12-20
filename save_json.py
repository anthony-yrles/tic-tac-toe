import json

def save_user(user_text, victories, draws, defeats):
    try:
        with open("player_stat.json", "r") as user_list:
            users = json.load(user_list)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        users = []
    user_exists = False
    for user in users:
        if user["username"] == user_text:
            user_exists = True
            user["victories"] += victories
            user["draws"] += draws
            user["defeats"] += defeats
            break

    if not user_exists:
        new_user = {
            "username": user_text,
            "victories": victories,
            "draws": draws,
            "defeats": defeats
        }
        users.append(new_user)
    with open("player_stat.json", "w") as user_list:
        json.dump(users, user_list)

def test_user(user_text, users):
    for user in users:
        if user["username"] == user_text:
            return True
    return False
