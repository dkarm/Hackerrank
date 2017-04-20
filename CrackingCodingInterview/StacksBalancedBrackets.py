def is_matched(expression):
    current_stack = []
    matched_brackets = {"{": "}", "[":"]", "(":")"}
    for el in expression:
        if el in matched_brackets.keys():
            current_stack.append(el)
        elif el in matched_brackets.values():
            if len(current_stack) ==0:
                return False
            if len(current_stack) > 0 and matched_brackets[current_stack.pop()] != el:
                return False
    if len(current_stack) > 0:
        return False
    return True


t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"

