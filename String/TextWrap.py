def wrap(string, max_width):
    string = textwrap.fill(string, max_width)
    return string
    
    
    #given
    if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
