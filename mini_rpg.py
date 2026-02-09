# мини рпг консольная
# словарь
# функции
# выход
from level_farm import level_farm


player = {
    "user": "",
    "age": 0,
    "gold": 100,
    "exp": 0,
    "exp_to_lvl": 100,
    "hp": 200,
    "max_hp": 200,
    "damage": 25,
    "levels_passed": 0
}

def create_profile(player):
    input("нажмите - Enter, чтобы создать профиль:-> ")

    while True:
        user = input("придумайте уникальный юзер:-> ")
        if user.replace(" ", "").isalpha():
            player["user"] = user
            break
        else:
            print("ошибка. попробуйте еще раз")

    while True:
        age = input("введите ваш возраст:-> ")
        if age.isdigit():
            player["age"] = age
            break
        else:
            print("ошибка. попробуйте еще раз")

    return player

def edit_profile(player):
    if player["user"] == "":
        print("сначала создайте профиль")
        return


    print("\n== выберите что изменить ==")
    print("1. юзер")
    print("2. возраст")
    print("3. ничего. выйти")

    choice = input("выберите действие:-> ")

    if not choice.isdigit():
        print("ошибка. попробуйте еще раз")
        return
    
    choice = int(choice)

    if choice == 1:
        
        while True:
            new_user = input("придумайте новый юзер:-> ")
            if new_user.replace(" ", "").isalpha():
                player["user"] = new_user
                break
            else:
                print("ошибка. попробуйте еще раз")

    elif choice == 2:

        while True:
            new_age = input("введите ваш новый возраст:-> ")
            if new_age.isdigit():
                player["age"] = new_age
                break
            else:
                print("ошибка. попробуйте еще раз")

    elif choice == 3:
        print("выйти")
        return
    else:
        print("ошибка. попробуйте еще раз!")
    

def battle_level(player, level):
    enemy = level_farm[level].copy()
    player["hp"] = player["max_hp"]
    print(f"вы встретили врага: {enemy['name']}")

    while player["hp"] > 0 and enemy["hp"] > 0:
        input("нажмите - Enter, чтобы ударить врага")

        enemy["hp"] -= player["damage"]
        print(f"удар, у врага {enemy['hp']}")

        if enemy["hp"] <= 0:
            print(f"вы победили, {enemy['name']}")
            print(f"вы получили: {enemy['gold']} золота и {enemy['exp']} опыта!")
            player["gold"] += level_farm[level]["gold"]
            player["exp"] += level_farm[level]["exp"]
            break

        player["hp"] -= enemy["damage"]
        print(f"вас ударили, у вас {player['hp']} хп")

        if player["hp"] <= 0:
            print("вы проиграли")
            break


def explore(player):
    print("\n== исследовать ==")
    print(f"пройденные уровни: {player['levels_passed']}")
    print("0. выйти")

    for lvl in range(1, player['levels_passed'] + 2):
        print(f"{lvl}, {level_farm[lvl]['name']}"
              f"HP: {level_farm[lvl]['hp']}, Damage: {level_farm[lvl]['damage']}")
        
    choice = input("выберите уровень:-> ")

    if not choice.isdigit():
        print("ошибка. попробуйте еще раз!")
        return
    
    choice = int(choice)

    if choice == 0:
        return
    
    if choice < 1 or choice > player['levels_passed'] + 1:
        print("уровень закрыт")
        return
    
    battle_level(player, choice)

    if player["hp"] > 0 and choice == player['levels_passed'] + 1:
        player["levels_passed"] += 1
        print(f"открыт новый уровень: {player['levels_passed']}")


while True:
    print("\n== Стартовое меню ==")
    print("1. создать профиль")
    print("2. изменить профиль")
    print("3. исследовать")
    print("4. профиль")
    print("5. выйти с игры")

    choice = input("выберите действие:-> ")

    if not choice.isdigit():
        print("ошибка. попробуйте еще раз")
        continue

    choice = int(choice)

    if choice == 1:
        create_profile(player)

    elif choice == 2:
        edit_profile(player)

    elif choice == 3:
        explore(player)

    elif choice == 4:
        if player["user"] == "":
            print("сначала создайте профиль - Пункт (1)")
        else:
            print("\n== Ваш профиль ==")
            print(f"user: {player['user']}")
            print(f"золото: {player['age']}")
            print(f"exp: {player['exp']}")
            print(f"исследование уровни пройдено: {player['levels_passed']}")

    elif choice == 5:
        print("выйти с игры")
        break
    else:
        print("ошибка. попробуйте еще раз")