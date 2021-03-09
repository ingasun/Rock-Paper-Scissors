from collections.abc import Hashable
# the object_list has already been defined
# write your code here
#object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
hash_list = []
for object_ in object_list:
    if isinstance(object_, Hashable):
        hash_list.append(hash(object_))

#print(hash_list)
        
sum_ = 0
occurences = []
for hvalue in hash_list:
    number = hash_list.count(hvalue)
    if number > 1:
        occurences.append(number)
        
eliminate = list(set(occurences))
print(sum(eliminate))
