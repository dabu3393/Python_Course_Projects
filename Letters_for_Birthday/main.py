
with open('./Input/Names/invited_names.txt') as names:
    invited_names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    starting_letter = letter.read()
    for name in invited_names:
        stripped_name = name.strip()
        new_letter = starting_letter.replace('[name]', stripped_name)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as file:
            file.write(new_letter)




