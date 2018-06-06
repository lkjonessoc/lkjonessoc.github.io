# there is  a package called nltk which is the natural language toolkit. load it for this file.
import nltk

#opening a file is something you have to do all the time so why not make it a method? And then you don't have to keep doing the same code, opening yourself up to mistakes
def open_file_and_get_text(filename):

    #given a file name, open it
    with open(filename, 'r') as our_file:
        #takes the file and reads the text and stores it.
        text = our_file.read()
    #this line needs to be included when you change this from just a function in the code to being a method
    return text

def clean_tokens(words):
    #given some tokens, lowercase them all
    #create an empty list called clean_words

    clean_words = []

    #loop over every word item in the words list
    for word in words:
        clean_words.append(word.lower())
    return clean_words


#Point the program to the filename that is going to be fed into this program.
our_file = "eyre.txt"

text = open_file_and_get_text(our_file)


words = nltk.word_tokenize(text)
text = open_file_and_get_text(our_file)
# take a long string and break it into words.
words = nltk.word_tokenize(text)
clean_words = clean_tokens(words)

# print out first 30 words of our clean tokens
print(clean_words[0:30])
word_counts = nltk.FreqDist(clean_words)
print(word_counts.most_common(10))
print(word_counts['jane'])
nltk.Text(clean_words).dispersion_plot(['he', 'she', 'jane', 'tony'])
