from typing import Any


class Event(list):
    def __call__(self, *args: Any, **kwds: Any):
        for item in self:
            item(*args, **kwds)

class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age = 0):
        super().__init__()
        self._age = age
    
    @property
    def age(self):
        return self._age 
    
    @age.setter
    def age(self, value):
        if self._age == value:
            return 
    
        self._age = value 
        self.property_changed('age', value)

class TrafficAuthority:
    def __init__(self, person:Person):
        self.person = person 
        person.property_changed.append()
    
    def person_chaged(self, name, value):
        if name == "age":
            if value < 16:
                print('Sprry you still cannot drive')
            else:
                print('Okay you can drive now')
                self.person.property_changed.remove(self.person_chaged)


if __name__ == "__main___":
    p = Person()
    ta = TrafficAuthority(p)
    
    for age in range(14, 20):
        print(f'Setting age to {age}')
        p.age = age
    