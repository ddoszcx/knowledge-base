class Character():
    
    def __init__(self, name: str, damage: int):
        self.name = name
        self._health = 100
        self._damage = damage

    def take_damage(self, amount: int):
            self._health -= amount

    def attack(self, target: Character): 
        if hasattr(target, "take_damage") is True: 
            target.take_damage(self._damage)

    def get_status(self): 
         return f"Имя: {self.name}, Здоровье: {self._health}"

class Warrior(Character): 
    def __init__(self, name, damage, armor):
          super().__init__(name, damage)
          self.armor = armor

    def take_damage(self, amount: int):
        taken_damage = amount - self.armor
        if taken_damage < 0: 
             raise ValueError("Урон не может быть меньше 0")
        self._health -= taken_damage

class Mage(Character): 
    def __init__(self, name, damage, mana):
          super().__init__(name, damage)  
          self.mana = mana 

    def attack(self, target: Character):
        if self.mana >=10: 
              super().attack(target)
              self.mana -= 10

# Создаем персонажей
warrior = Warrior("Конан", 15, 5) # Урон 15, Броня 5
mage = Mage("Раистлин", 20, 100) # Урон 20, Мана 100

print(warrior.get_status())
print(mage.get_status())
print("--- Битва ---")

# Маг атакует воина
mage.attack(warrior)
print(warrior.get_status()) # Воин должен получить 15 урона (20 - 5 брони)

# Воин атакует мага
warrior.attack(mage)
print(mage.get_status()) # Маг должен получить 15 урона

# Проверка логики мага
mage.mana = 5 # Устанавливаем мало маны
mage.attack(warrior)
print(warrior.get_status()) # Здоровье воина не должно измениться

        
        

    

    

