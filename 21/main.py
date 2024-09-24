def char_freq(chars):
    freq = {}
    for char in chars:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(char_freq('abbabcbdbabdbdbabababcbcbab'))