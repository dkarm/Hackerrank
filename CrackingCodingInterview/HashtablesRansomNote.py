def ransom_note(magazine, ransom):
    potential_words = {}
    for word in magazine:
        potential_words[word] =0
    for word in magazine:
        potential_words[word]  += 1
    for word in ransom:
        if potential_words[word] > 0:
            potential_words[word] -= 1
        else:
            return False
    return True


m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print "Yes"
else:
    print "No"