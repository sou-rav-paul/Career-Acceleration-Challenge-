names = ['A','B','C']
ages = [20,30,35]

zip_obj = zip(names,ages)
NameAgeDict = dict(zip_obj)
print(NameAgeDict)

# Output: {'A':20,'B':30,'C':35}