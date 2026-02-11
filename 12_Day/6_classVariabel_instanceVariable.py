class Cordata:
    species = 'Human'
    def __init__(self,name):
        self.name = name

cordata1 = Cordata('A')
cordata2 = Cordata('B')

print(cordata1.species)     # Human
print(cordata2.species)     # Human

# Changing species 
Cordata.species = 'Alien'
print(cordata1.species)     # Alien
print(cordata2.species)     # Alien