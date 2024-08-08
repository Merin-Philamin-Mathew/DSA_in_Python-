def reverse_string(string):
    n = len(string)-1
    if len(string)<1:
        return ''
    else:
        return string[n]+reverse_string(string[:n])


rev = reverse_string('merin')
print(rev)
