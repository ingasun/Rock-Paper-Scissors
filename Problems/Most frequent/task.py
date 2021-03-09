from collections import Counter
#text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
#        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

text = ('1 bla bla')
freq_counter = Counter(text.split()).most_common()
if len(text) == 1:
    print(f'{text[0]} 1')
else:
    for thing in freq_counter:
        print(f'{thing[0]} {thing[1]}')

# print(freq_counter)
# Counter({'a': 3, 'in': 2, 'or': 2, 'gambit': 1, 'is': 1, 'chess': 1, 'opening': 1,
# 'which': 1, 'player': 1, 'risks': 1, 'one': 1, 'more': 1, 'pawns': 1, 'minor': 1,
# 'piece': 1, 'to': 1, 'gain': 1, 'an': 1, 'advantage': 1, 'position': 1})
