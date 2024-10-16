def check_freq(s):
    frequency={}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency
s = "Rahul"

print(check_freq(s))