from edit_code.list_levels import list_levels, levels


class Games:
    def __init__(self, levels):
        self.levels = levels
        self.results = {}

    def load_levels(self):  # для подгрузки уровня сложности
        if self.levels == 'легкий':
            return list_levels[0]
        elif self.levels == 'средний':
            return list_levels[1]
        elif self.levels == 'тяжелый':
            return list_levels[2]

    def play_games(self):  # основной процесс игры
        for word, answer in self.load_levels().items():
            print(f'{word}, {len(answer)} буквы начинается на {answer[0:1]}...')
            if self.user_answer() == answer:
                self.results[word] = True
                print(f'Верно, {word} - это {answer.title()}')
            else:
                print(f"Неверно, {word} - это {answer.title()}")
                self.results[word] = False

    def user_answer(self):  # ответы юзера на вопросы
        answer = input().lower()
        return answer

    def result(self):
        print("Ваше знание:")
        total = int(0)
        for answer in self.results.values():
            if answer:
                total += 1
        print(levels[total])


if __name__ == '__main__':
    while True:
        user_level = input(f"{'-' * 50}\nВыберете один из уровней сложности:\nЛегкий, Средний, Тяжелый\n").lower()
        if user_level not in ["легкий", "средний", "тяжелый"]:
            print(f'Такого уровня нет\n{"-" * 50}')
            continue
        games = Games(user_level)
        games.load_levels()
        games.play_games()
        games.result()
        break

# TODO: Таким образом код сокращен в 2 раза (97 и 50 строк соответственно)
