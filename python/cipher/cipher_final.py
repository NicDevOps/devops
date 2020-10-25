import argparse

def parse_command_line():
    
    parser = argparse.ArgumentParser()
    
    # positional arguments
    parser.add_argument('infile',help = 'input file to be encrypted or decrypted')

    # Add optional argument
    parser.add_argument('-o', '--outfile', help = '--outfile outfile_path')

    parser.add_argument('-k', '--key', metavar = 'KEY', type = int, help = 'encryption/decryption key (must be positive) (default = 1)')

    parser.add_argument('-d', '--decrypt', action = 'store_true', help = 'decrypt the input file')

    parser.add_argument('-a', '--all', action = 'store_true', help = 'decrypt using all keys [1, 25], save outputs in different files. (useful in case the key is lost or unknown)')

    parser.add_argument('-v', '--verbose', action = 'store_true', help = 'verbose mode')
    
    # Parse command-line arguments
    return parser.parse_args()
    
    

def read_file(file_path):
  
    try:
    
        with open(file_path, 'r') as file_path:
            x = file_path.read()
            return x

    except Exception as exception_object:
        print("Unexpected exception", exception_object)

        
def write_file(message, file_path):
    
    try:
    
        with open(file_path, 'w') as file_path:
            file_path.write(message)

    except Exception as exception_object:
        print("Unexpected exception", exception_object)

def transform(message, key, decrypt):

    nw_message = ''
    if decrypt:
        for i in message:
            try:
                nw_message = nw_message + shift(i, -(key))
            except TypeError:
                nw_message = nw_message + ' '
        
        return nw_message
    
    else:
        for i in message:
            try:
                nw_message = nw_message + shift(i, key)
            except TypeError:
                nw_message = nw_message + ' '
        
        return nw_message
    
 
def shift(char, key):    
  
    # ordered lower case alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # will contain shifted lower case alphabet
    shifted_alphabet = ''
    for i in range(len(alphabet)):
        shifted_alphabet = shifted_alphabet + alphabet[(i + key) % 26]
 
    if char.isalpha():
        char_index = alphabet.index(char.lower())
        shifted_char = shifted_alphabet[char_index]
    
        # keep char's case (upper or lower)
        if char.isupper():
            return shifted_char.upper()
        else:
            return shifted_char
    else:
        return char


def main():
    # parse command line arguments
    args = parse_command_line()

    # args.infile, args.outfile, args.key, args.decrypt, args.all, args.key, args.verbose = args1[0], args1[1], args1[2], args1[3], args1[4], args1[5], args1[6]

    # read content of infile to a string
    instring = read_file(args.infile)
    
    # verbose
    if args.verbose:
        print("Input file:")
        print("------------")
        print(instring)
        print()
    
    # key is specified
    if not args.all:
        # encrypt/decrypt content of infile
        outstring = transform(instring, args.key, args.decrypt)
    
        # verbose
        if args.verbose:
            print("Output file:")
            print("------------")
            print(outstring)

        # write content of outstring to outfile
        write_file(outstring, args.outfile)
    
    # key is not specified, try all keys from 1 to 25 to decrypt infile
    else:
        for k in range(1, 26):
            # decrypt content of infile
            outstring = transform(instring, k, True)

            # verbose
            if args.verbose:
                print("Key =", k)
                print("------------")
                print(outstring)
                print()

            # write content of outstring to outfile
            write_file(outstring, "decrypted_by_" + str(k) + ".txt")
    
if __name__ == '__main__':
    main()