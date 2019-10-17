#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """

    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        nopunc = [char for char in content[1] if char not in string.punctuation]
        text_string = ''.join(nopunc)
        stemmer = SnowballStemmer("english")
        stemmed = []
#         for word in list(text_string):
#             stemmed.append(stemmer.stem(word))
        stemmed = [stemmer.stem(word) for word in text_string.split()]
        text_string = ' '.join(stemmed)
#         text_string = content[1].translate(str.maketrans("", ""), string.punctuation)

        ### project part 2: comment out the line below
        words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        




    return words

    

def main():
    ff = open("test_email-Copy1.txt", "r")
    text = parseOutText(ff)
    print (text)



if __name__ == '__main__':
    main()
