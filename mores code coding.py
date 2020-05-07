MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
def encode(message):
    encoded = ''
    encode_character = ''

    for letter in message:
        if letter != ' ':
            encode_character = MORSE_CODE_DICT[letter]
            encoded += encode_character
            encoded += ' '

        else:
            encoded += ' '

    print(encoded)
encode('HEISENBURG')

def decode(message):
    decoded = ''
    lst_backup = []
    lst_morse = message.split('  ')
    for i in lst_morse:
        x = i.split(' ')
        lst_backup += x
        lst_backup += [' ']

    for i in lst_backup:
        if i != ' ':
            for key, value in MORSE_CODE_DICT.items():
                if i == value:
                    decoded += key
        else:
            decoded += ' '

    print(decoded)

decode('.... . .. ... . -. -... ..- .-. --. ')