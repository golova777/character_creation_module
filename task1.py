import time
from datetime import datetime as dt


# Объявите класс Quest с методами и свойствами.
class Quest:
    def __init__(self, name: str, goal: str, description: str) -> None:
        self.name: str = name
        self.goal: str = goal
        self.description: str = description

        self.start_time = None
        self.end_time = None

    def __str__(self) -> str:
        class_str = f'$$$ Цель квеста {self.name} - {self.goal}'
        if self.start_time is None:
            class_str += ' Квест ещё не начат.'
        if self.end_time is not None:
            class_str += ' Квест завершён.'
        if self.start_time is not None and self.end_time is None:
            class_str += ' Квест выполняется.'
        return class_str

    def accept_quest(self) -> str:
        if self.end_time is not None:
            return ('C этим испытанием вы уже справились.')

        self.start_time = dt.now()
        return (f'Начало "{self.name}" положено.')

    def pass_quest(self) -> str:
        if self.start_time is None:
            return ('Нельзя завершить то, что не имеет начала!')

        self.end_time = dt.now()
        self.completion_time = int((self.end_time -
                                    self.start_time).total_seconds())
        return (f'квест "{self.name}" окончен. '
                f'Время выполнения квеста: {self.completion_time}')


# В этих переменных содержатся значения, которые нужно передать
# в качестве аргументов в экземпляр класса Quest.
quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''
# Создайте экземпляр класса Quest.

new_quest = Quest(quest_name, quest_description, quest_goal)
print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())
print(new_quest)
