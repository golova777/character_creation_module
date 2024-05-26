

class Bird:

    def __init__(self, name: str, size: str) -> None:
        self.name: str = name
        self.size: str = size

    def describe(self, full: bool = False) -> str:
        return (f'Размер птицы {self.name} — {self.size}')


class Parrot(Bird):
    def __init__(self, name: str, size: str, color: str) -> None:
        super().__init__(name, size)
        self.color: str = color
    
    def repeat(self, phrase: str) -> str:
        return (f'Попугай {self.name} говорит: {phrase}.')

    def describe(self, full: bool = False) -> str:
        if full:
            return (f'Попугай {self.name} — заметная птица, окрас её перьев '
                    f'— {self.color}, а размер — {self.size}. Интересный факт:'
                    f' попугаи чувствуют ритм, а вовсе не бездумно двигаются '
                    f'под музыку. Если сменить композицию, то и темп '
                    f'движений птицы изменится')
        else:
            return super().describe()


class Penguin(Bird):
    def __init__(self, name: str, size: str, genus: str) -> None:
        super().__init__(name, size)
        self.genus: str = genus

    def swimming(self) -> str:
        return (f'Пингвин {self.name} плавает со средней скоростью 11 км/ч.')
    
    def describe(self, full: bool = False) -> str:
        if full:
            return (f'Размер пингвина {self.name} из рода {self.genus} '
                    f'— {self.size}. Интересный факт: однажды группа '
                    f'геологов-разведчиков похитила пингвинье яйцо, и их'
                    f' принялась преследовать вся стая, не пытаясь, впрочем, '
                    f'при этом нападать. Посовещавшись, похитители '
                    f'вернули птицам яйцо, и те отстали.')
        else:
            return super().describe()


kesha = Parrot('Ара', 'Средний', 'Красный')
kowalski = Penguin('Ковальский','большой','Aptenodytes')

print(kesha.describe())
print(kowalski.describe())

print(kesha.describe(True))
print(kowalski.describe(True))

print(kesha.repeat("popka durak!!!"))
print(kowalski.swimming())
