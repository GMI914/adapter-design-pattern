class MyShelter:
	animals = []
	
	def __init__(self, animals = []):
		self.animals = animals

	def add_pet(self, pet):
	    self.animals.append(pet)

	def adopt_pet(self, id):
		pet = [a for a in self.animals if a['id'] is id]
		if len(pet):
		    self.animals.remove(pet[0])
		return pet[0] if len(pet) else false


class AnimalRegistree:
    registered_animals = {}
    
    def __init__(self, animals = {}):
        self.registered_animals = animals
        
    def register_animal(self, name, animal_info):
        self.registered_animals[name] = animal_info
        
    def find_animal(self, name):
        return self.registered_animals.get(name)
    
class RegistreeAdapter:
    
    def __init__(self, registree):
        self.registree = registree
    
    def register_animal(self, pet):
        self.registree.register_animal(pet['name'], pet)
        return pet['name']
    
    def find_animal(self, name):
        return self.registree.find_animal(name)

shelter = MyShelter()
shelter.add_pet({'id': 1, 'type': 'dog', 'name': 'chapie'})
shelter.add_pet({'id': 2, 'type': 'cat', 'name': 'lulu'})

registree = AnimalRegistree()
adapter = RegistreeAdapter(registree)

dog = shelter.adopt_pet(1)
dog_id = adapter.register_animal(dog)

print(registree.registered_animals)
print(adapter.find_animal(dog_id))
