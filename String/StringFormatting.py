def print_formatted(number):
    # your code goes here
    
    w = len(str(bin(number))[2:])
    for i in range(1, number + 1):
        decimal = str(i)
        octal = str(oct(i))[1:]
        hexadecimal = str(hex(i))[2:]
        hexadecimal = hexadecimal.upper()
        binary = str(bin(i))[2:]
        print('{:>{width}} {:>{width}} {:>{width}} {:>{width}}'.format(decimal, octal, hexadecimal, binary, width = w))
    
    
    #given
    if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
