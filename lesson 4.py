class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name
    @property
    def  health(self):
        return self.__health
    @health.setter
    def health(self,value):
        self.__health = value

    @property
    def demage(self):
        return self.__damage
    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f' {self.__name} health: {self.__health} damage: {self.__damage}'

class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name,health,damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def  choose_defence(self, heroes):
        pass

    def attack(self, heroes):
        pass

    def __str__(self):
        ret


