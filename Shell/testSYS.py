import sys
#print(sys.path)
sys.path.append("/Users/noorulainnoor/projects/OOP")

#import Person
#p = Person.Person("Usman", 23)

from Person import Person
p = Person("Usman", 23)

print p.name
print p.age


print(sys.path)