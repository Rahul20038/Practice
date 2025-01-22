def pallindrome_w(s):
    s = s.lower()
    return s == s[::-1]
print(pallindrome_w("Refer"))