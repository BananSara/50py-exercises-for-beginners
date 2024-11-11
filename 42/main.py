
import re
def splitter(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)  # Split after .!? and space
    return sentences

text = """Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? 
Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."""

for sentence in splitter(text):
    print(sentence)
