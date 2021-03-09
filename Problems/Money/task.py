from collections import defaultdict

transactions = [(38177, 34.38), (876, 999.99), (654276, 653678), (54366, 0.99),
                (546, 987.65), (876, 3456), (654276, 0.55), (38177, 876.75), (876, 98.7)]

# create transaction_dict
transaction_dictionary = defaultdict(list)


for word in transactions:
    transaction_dictionary[word[0]].append(word[1])

print(transaction_dictionary)