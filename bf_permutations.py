from itertools import ifilter, product

def gen_programs(length, excluded_chars):
    chars = set([">", "<", "+", "-", "[", "]", ",", "."]) - set(excluded_chars)
    return product(chars, repeat=length)

def valid_program(p):
    # Check that we have matching number of parens
    if p.count("[") != p.count("]"):
        return False

    count = 0
    for c in p:
        if c == "[":
            count += 1
        elif c == "]":
            count -= 1

        if count < 0:
            return False

    if count != 0:
        return False

    return True

def useful_program(p):
    if p.count("+") == 0 or p.count("-") == 0:
        return False

    for i in xrange(len(p)-1):
        char = p[i]
        next_char = p[i+1]

        if char == "[" and next_char == "]":
            return False

        if char == ">" and next_char == "<":
            return False

        if char == "<" and next_char == ">":
            return False

        if char == "+" and next_char == "-":
            return False

        if char == "-" and next_char == "+":
            return False

    return True

def bf_programs(length, excluded_chars=[",", "."]):
    return ifilter(useful_program, ifilter(valid_program, gen_programs(length, excluded_chars)))

def main():
    for n in xrange(3, 8):
        for p in bf_programs(n):
            print "".join(p)

if __name__ == '__main__':
    main()