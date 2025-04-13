class Computer:
    def __init__(self, cpu, memory):
        self.cpu = cpu
        self.memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return {
            "sum": self.cpu + self.memory,
            "difference": self.cpu - self.memory,
            "multiplication": self.cpu * self.memory,
            "division": self.cpu / self.memory if self.memory != 0 else "Error: division by zero"
        }

    def __str__(self):
        return f"Computer(cpu={self.cpu}, memory={self.memory})"

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

class Phone:
    def __init__(self, sim_cards_list):
        self.sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, new_list):
        self.__sim_cards_list = new_list

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.sim_cards_list):
            sim = self.sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim}")
        else:
            print("Ошибка: такой сим-карты не существует")

    def __str__(self):
        sims = ', '.join(self.sim_cards_list)
        return f"Phone(sim_cards=[{sims}])"

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    def __str__(self):
        sims = ', '.join(self.sim_cards_list)
        return f"SmartPhone(cpu={self.cpu}, memory={self.memory}, sim_cards=[{sims}])"

computer = Computer(cpu=8, memory=16)
phone = Phone(sim_cards_list=["Beeline", "O!"])
smartphone1 = SmartPhone(cpu=4, memory=32, sim_cards_list=["MegaCom", "O!"])
smartphone2 = SmartPhone(cpu=6, memory=16, sim_cards_list=["Beeline"])


print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print("\n--- Методы объектов ---")

print("Вычисления на компьютере:")
print(computer.make_computations())

phone.call(1, "+996 555 00 11 22")
phone.call(3, "+996 555 00 11 22")  # Ошибка


smartphone1.call(2, "+996 777 99 88 11")
smartphone1.use_gps("Бишкек")

print("\n--- Сравнение объектов Computer ---")
computer2 = Computer(cpu=2, memory=32)
print("computer == computer2:", computer == computer2)
print("computer != computer2:", computer != computer2)
print("computer < computer2:", computer < computer2)
print("computer <= computer2:", computer <= computer2)
print("computer > computer2:", computer > computer2)
print("computer >= computer2:", computer >= computer2)

