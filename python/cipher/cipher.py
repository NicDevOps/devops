


import argparse



def parse_command_line():
    
    """
    usage: cipher.py [-h] [-o outfile_path] [-k KEY] [-d] [-a] [-v] infile

     positional arguments:
       infile                input file to be encrypted or decrypted

     optional arguments:
       -h, --help            show this help message and exit
       -o outfile_path, --outfile outfile_path
                             output file
       -k KEY, --key KEY     encryption/decryption key (must be positive) (default
                             = 1)
       -d, --decrypt         decrypt the input file
       -a, --all             decrypt using all keys [1, 25], save outputs in
                             different files. (useful in case the key is lost or
                             unknown)
       -v, --verbose         verbose mode
    """
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
    args = parser.parse_args()
    
    return args.infile, args.outfile, args.key, args.decrypt, args.all, args.key, args.verbose



  
        
        
       

    

aws = parse_command_line()

print(aws)

    
    