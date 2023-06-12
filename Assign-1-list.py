# Given a list with first names and another list with last names. Combine the lists such that the Full name is present.

first_names = ['Micheal','Jim','Pam','Dwight','Stanley']
last_names = ['Scott','Halpert','Beasely','Hudson']

full_names = [first + " " + last for first, last in zip(first_names, last_names)]

print(full_names)