import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num_of_letters = len(alphabet)
program_running = True

while program_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % num_of_letters

    def caeser(text, shift, direction):
        final_message = ''
        if direction == 'decode':
                shift *= -1
        for char in text:
            if char in alphabet:
                placement = alphabet.index(char)
                new_placement = placement + shift
                if new_placement > 25:
                    new_placement -= num_of_letters
                elif new_placement < 0:
                    new_placement += num_of_letters
                final_message += alphabet[new_placement]
            else:
                final_message += char
        print(f'The {direction}d text is {final_message}')

    caeser(text, shift, direction)

    go_again = input('Type \'yes\' if you want to go again. Otherwise type \'no\'.\n').lower()

    if go_again == 'yes':
        pass
    elif go_again == 'no':
        program_running = False
        print('Goodbye')
    else:
        program_running = False
        print('That\'s not an option. Goodbye.')


