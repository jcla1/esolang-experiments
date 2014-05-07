import itertools

def bf_programs(length, excluded_chars=[","]):
    chars = set([">", "<", "+", "-", "[", "]", ",", "."]) - set(excluded_chars)
    return itertools.product(chars, repeat=length)

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

    for i in xrange(len(p)):
        char = p[i]
        if char == "[" and p[i+1] == "]":
            return False

    return True

def main():
    for p in itertools.ifilter(useful_program, itertools.ifilter(valid_program, bf_programs(5))):
        print "".join(p)

if __name__ == '__main__':
    main()