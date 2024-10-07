import time
import os


d = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot',
    'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
    'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec', 'r': 'romeo',
    's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey',
    'x': 'x-ray', 'y': 'yankee', 'z': 'zulu'}

def speak_ICAO(text):
    words = text.lower().split()
    a = []
    for word in words:
        for char in word:
            if char in d:
