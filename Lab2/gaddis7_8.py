# Programming Exercise 7-8

# Read the boy text file
# make sure 'BoyNames.txt' is saved in same folder as this script
boy_input = open('BoyNames.txt', 'r')

# Read all the lines in the file into a list.
popular_boy_names = boy_input.readlines()

# create an empty list. We will fill this list up with strings as its elements
b = []
# Strip trailing '\n' from all elements of the list.
# rstrip is a method of the strings object
for i in range(len(popular_boy_names)):
    b.append(popular_boy_names[i].rstrip('\n'))


# Repeat for girls txt file
girl_input = open('GirlNames.txt', 'r')

# Read all the lines in the file into a list.
popular_girl_names = girl_input.readlines()

# create an empty list. We will fill this list up with strings as its elements
g = []
# Strip trailing '\n' from all elements of the list.
# rstrip is a method of the strings object
for i in range(len(popular_boy_names)):
    g.append(popular_girl_names[i].rstrip('\n'))


def is_popular_boys_name(name):
    if name in b:
        return True
    else:
        return False

    
def is_popular_girls_name(name):
    if name in g:
        return True
    else:
        return False
