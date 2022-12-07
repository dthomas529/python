# Program generates a mad libs using string concatenation
# Examples
# print('Subscribe to' + (youtuber)
# print('Subscribe to' {}.format(youtuber)
# print(f'Subscribe to (youtuber)')

# Prompt the user for adjectives and nouns
adj1 = input('Type an adjective: ')
adj2 = input('Type an adjective: ')
bird = input('Type the name of a bird: ')
room = input('Type the name of a room: ') 

# Mad Lib
madlib = 'It was a  '+ adj1  + ' cold November day. \
I woke up to the '+ adj2 + ' smell of ' + bird + ' roasting  in the ' + room + ' downstairs. '

print(madlib)