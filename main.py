with open("text.txt","r") as file:
    text = file.read()
words = text.split()

long_words = []
total_count = 0
count = 0
freq = {}
longest_word = ""
most_freq = ""
avg = 0
total_length = 0
above_avg = []

for w in words:
    if len(w) > 5:
        long_words.append(w)
        count = count+1
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

longest_word = max(long_words, key=len) 
most_freq = max (freq, key=freq.get)
unique = set(words)
total_count = len(words)
#total_length = len(text.replace(" ",""))
#avg = total_length / total_count

for w in words:
    total_length += len(w)

avg = total_length / total_count

for w in words:
   if len(w) > avg:
    above_avg.append(w)

print("\n=== FILE TEXT ANALYZER ===\n")
print("Text from file is: ",text)
print ("Words are: ",words)
print ("Total count of words is: ",total_count)
print ("Long words: ",long_words)
print ("Count of long words: ",count)
print ("Quantity of words: ",freq)
print ("Longest word is: ",longest_word)
print ("Most frequent word is: ",most_freq)
print ("Unique words are: ",unique)
print("Total length of words: ",total_length)
print("Average word length: ",avg)
print("Words longer than average: ",above_avg)
