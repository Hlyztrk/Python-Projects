import string

alphabeth = list(string.ascii_lowercase)

def caesar(choice, message, shift):
    shifted_letters = []
    for i in message:
        if i in alphabeth:
            index_of_letter = alphabeth.index(i)
            if choice == 'encode': 
                shifted_letters.append(alphabeth[(index_of_letter + shift) % len(alphabeth)])
            elif choice =='decode':
                 shifted_letters.append(alphabeth[(index_of_letter - shift) % len(alphabeth)])
        else:
            index_of_symbol = message.index(i)
            shifted_letters.append(message[index_of_symbol])

    return ''.join(shifted_letters)

continue_game = True
while continue_game:
    user_choice = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()
    user_message = input("Type your message: ").lower()
    type_shift = int(input("Type the shift number: "))
    print(f"Here is your {user_choice}d message: {caesar(user_choice, user_message, type_shift)}")
    try_again = input("Type 'yes' if you would like to try again. Otherwise type 'no': ").lower()
    if try_again == 'no':
         print("Goodbye!")
         continue_game = False