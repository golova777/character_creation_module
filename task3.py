# импортируем функции из библиотеки math для рассчёта расстояния
from math import radians, sin, cos, acos


class Point:
    def __init__(self, latitude: float, longitude: float) -> None:
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)
    # считаем расстояние между двумя точками в км

    def distance(self, other) -> int:
        cos_d = (sin(self.latitude) * sin(other.latitude) +
                 cos(self.latitude) * cos(other.latitude) *
                 cos(self.longitude - other.longitude))
        return int(6371 * acos(cos_d))


class City(Point):
    def __init__(self, latitude: float, longitude: float, 
                 name: str, population: int) -> None:
        # допишите код: сохраните свойства родителя
        # и добавьте свойства name и population
        super().__init__(latitude, longitude)
        self.name: str = name
        self.population: int = population

    def show(self) -> None:
        print(f'Город {self.name}, население {self.population} чел.')


class Mountain(Point):
    # допишите код: напишите конструктор, в нём сохраните свойства родителя
    # и добавьте свойства name и height
    # Создайте метод show(self):
    # информацию о горе нужно вывести в формате:
    # "Высота горы <название> - <высота> м."
    def __init__(self, latitude: float, longitude: float,
                 name: str, height: int) -> None:
        super().__init__(latitude, longitude)
        self.name: str = name
        self.height: int = height

    def show(self) -> None:
        print(f'Гора {self.name}, высота {self.height} м.')


# эта функция печатает расстояние
# между двумя любыми наследниками класса Point
def print_how_far(geo_object_1, geo_object_2):
    print(f'От точки «{geo_object_1.name}» до точки «{geo_object_2.name}» — {geo_object_1.distance(geo_object_2)} км.')


# основной код
moscow = City(55.7522200, 37.6155600, 'Москва', 12615882)
everest = Mountain(27.98791, 86.92529, 'Эверест', 8848)
chelyabinsk = City(55.154, 61.4291, 'Челябинск', 1200703)
moscow.show()
everest.show()
print_how_far(moscow, everest)
print_how_far(moscow, chelyabinsk)
