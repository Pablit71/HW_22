easy = {"дом": "home", "банан": "banana", "стол": "table", "кружка": "cup", "тетрадь": "notebook"}
medium = {"приватный": "private", "письменый": "writing", "подушка": "pillow", "дерево": "wood", "диалог": "dialogue"}
hard = {"выделить": "highlight", "беспокоиться": "worry", "подходить": "suit", "одолжить": "borrow", "диван": "sofa"}
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}
results = {

}

complexity = ["легкий", "средний", "тяжелый"]
print("Выберете один из уровней сложности: легкий, средний, тяжелый")
level_selection = input().lower()
for i in complexity:
    if i == level_selection:
        print(f"Вы выбрали сложность - {level_selection}, зададим 5 слов")
        break
else:
    print(f"Ошибка.")
    exit()

print(" ")
print(" ")

print("Нажмите enter")
pressing = input()

if level_selection == "легкий":
    for k, v in easy.items():
        if len(v) <= 4:
            num_lit = "буквы"
        else:
            num_lit = "букв"
        print(f"{k}, {len(v)} {num_lit}, начинается на {v[0:1]}...")
        answer = input()
        if answer == v:
            print(f"Верно, {k} - это {v.title()}")
            results[k] = True

        else:
            print(f"Неверно, {k} - это {v.title()}")
            results[k] = False

if level_selection == "средний":
    for k, v in medium.items():
        if len(v) <= 4:
            num_lit = "буквы"
        else:
            num_lit = "букв"
        print(f"{k}, {len(v)} {num_lit}, начинается на {v[0:1]}...")
        answer = input()
        if answer == v:
            print(f"Верно, {k} - это {v.title()}")
            results[k] = True

        else:
            print(f"Неверно, {k} - это {v.title()}")
            results[k] = False

if level_selection == "тяжелый":
    for k, v in hard.items():
        if len(v) <= 4:
            num_lit = "буквы"
        else:
            num_lit = "букв"
        print(f"{k}, {len(v)} {num_lit}, начинается на {v[0:1]}...")
        answer = input()
        if answer == v:
            print(f"Верно, {k} - это {v.title()}")
            results[k] = True

        else:
            print(f"Неверно, {k} - это {v.title()}")
            results[k] = False

print("Правильно отвеченные слова:")
for i in results:
    if results[i] == True:
        print(i)
print("Неправильно отвеченные слова:")
for i in results:
    if results[i] == False:
        print(i)

print("Ваш ранг:")
total = int(0)
for v in results.values():
    if v == True:
        total += 1

print(levels[total])
