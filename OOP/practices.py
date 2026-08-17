class safe():
    def __init__(self, name): 
        self.name = name 
    
    def __get__(self, instance, name):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        instance.__dict__[self.name] = value



class Vehicle():
    vehicles_created = 0
    _max_speed = safe("_max_speed")
    _mileage = safe("_mileage")
    distance  = safe("distance")

    def __init__(self, brand, _max_speed):
        self.brand = brand
        self._max_speed = _max_speed
        Vehicle.vehicles_created += 1
        self._mileage = 0
        
        
    
    def get_max_speed(self):
        return self._max_speed
    
    def get_mileage(self):
        return  self._mileage
    
    def drive(self,  distance):
        self._mileage += distance
    
    def display_info(self): 
        print(f"""Марка: {self.brand}
Макс. скорость: {self._max_speed} км/ч
Пробег: {self._mileage} км""")

class Car(Vehicle):
    def __init__(self,brand, _max_speed,  engine_type): 
        super().__init__(brand, _max_speed)
        self.engine_type = engine_type

    def display_info(self): 
        super().display_info()
        print(f"Тип двигателя: {self.engine_type}")
    
class Bicycle(Vehicle):
    def __init__(self, brand, _max_speed, frame_material):
        super().__init__(brand, _max_speed)
        self.frame_material = frame_material

    def display_info(self):
        super().display_info()
        print(f"Материал рамы: {self.frame_material}")
        
    



