def byFreq(pair):
    return pair[1]

def main():
     print("This program analyzes word frequency in a file")
     print("and prints a report on the n most frequent words.\n")
# get the sequence of words from the
fname = input("File to analyze: ")
text = open(fname,'r').read()
text = text.lower()
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
     text = text.replace(ch, ' ')
words = text.split()

# construct a dictionary of word counts
counts = {}
for w in words:
   counts[w] = counts.get(w,0) + 1
# print words and associated counts
#for w in uniqueWords:
#    print(w, counts[w])
#uniqueWords = list(counts.keys())
#uniqueWords.sort()

# output analysis of n most frequent words.
n = eval(input("Output analysis of how many words? "))
items = list(counts.items())
items.sort()  # orders pairs alphabetically
items.sort(key=byFreq, reverse=True)    # orders by frequency

for i in range(n) :
     word, count = items [i]
     print("{0:<15}{1:>5}".format(word,count))        #.format (*items [i]) )
     
if __name__ == "__main__":main()
