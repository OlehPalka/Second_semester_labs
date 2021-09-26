import game

стрийська = game.Street("вул. Стрийська")
стрийська.set_description("Страшна вулця")

козельницька = game.Street("вул. Козельницька")
козельницька.set_description(
    "Ще страшніша вулиця.")

франка = game.Street("вул. І.Франка")
франка.set_description(
    "Красива, але страшна вулиця.")

краківська = game.Street("вул. Краківська")
краківська.set_description(
    "Нова, але страшна вулиця.")

стрийська.link_street(козельницька, "південь")
козельницька.link_street(стрийська, "північ")
козельницька.link_street(франка, "південь")
франка.link_street(козельницька, "північ")
франка.link_street(краківська, "захід")
краківська.link_street(франка, "схід")
first_street = стрийська
last_street = краківська

drunk_student = game.Enemy(
    "Студент", "Студент, який ледве стоїть на ногах, але тим не менше дуже небезпечний.")
drunk_student.set_conversation("What's up, dude! I'm hungry.")
drunk_student.set_weakness("Лопата")
козельницька.set_character(drunk_student)

gopnic = game.Enemy(
    "gopnic", "Гопнік, який постійно до всіх пристає.")
gopnic.set_conversation("""Єсть мобіла подзвонить?
Чьо по мєлочі?""")
gopnic.set_weakness("Біта")
франка.set_character(gopnic)

bomg = game.Enemy(
    "bomg", "Гроза району, ніхто не проходив повз нього не заплативши йому.")
bomg.set_conversation("УАУАРУЕАРУОАЛОУЛРПАГПМАОУИРПАПУ...")
bomg.set_weakness("Гроші")
краківська.set_character(bomg)

bita = game.Item("Біта")
bita.set_description("біта - краще будь-яких слів.")
стрийська.set_item(bita)

showel = game.Item("Лопата")
showel.set_description("Хороша, добротна лопата 1984 року.")
козельницька.set_item(showel)

money = game.Item("Гроші")
money.set_description("Бабло завжди перемагає зло.")
drunk_student.set_item(money)
final_boss = bomg

current_street = стрийська
backpack = []

dead = False

while dead == False:

    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()

    if inhabitant == final_boss:
        command = "битися"
    else:
        command = input("> ")

    if command in ["північ", "південь", "схід", "захід"]:
        # Move in the given direction
        current_street = current_street.move(command)
    elif command == "говорити":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "битися":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is
            if current_street.name == "вул. Краківська":
                print("Бомж - останні босс, якого тобі потрібно пройти!")
                print(
                    "Щоб його перемогти, тобі потрібно йому заплатити, а інакше ти програв!")

            print("З чим ти хочеш битися?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_street.character = None
                    if inhabitant.given_item != None:
                        backpack.append(inhabitant.given_item.name)
                    if bomg.defeat == True:
                        print(
                            "Вітаємо, ти успішно відвів дівчину додому нічним Львовом!")
                        print(
                            f"Ти переміг {inhabitant.get_defeated()} львівських монстрів!")
                        print(
                            f"Шанс, що дівчина буде з тобою зустрічатися = {inhabitant.get_defeated()}/3!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Лол, ти програв.")
                    print("Це кінець...")
                    dead = True
            else:
                print("Ти не маєш " + fight_with)
                if inhabitant.name == "bomg":
                    print(
                        "Бомж побив тебе, і тепер твоя дівчина зустрічається з ним:(")
                    print("Ти програв.")
                    dead = True
        else:
            print("Тут немає з ким битися")
    elif command == "взяти":
        if item is not None:
            print("Ти поклав " + item.get_name() + " в рюкзак.")
            backpack.append(item.get_name())
            print(backpack)
            current_street.set_item(None)
        else:
            print("Тут нічого немає!")
    else:
        print("Я не знаю що таке " + command)
