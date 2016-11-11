# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print('\nName: Zoe Halbeisen\nUnique name: zoeanne\nUnique ID: 84194416\nSection Day/Time: Wednesday 5:30-6:30\n')

print("START*******")

import nltk
import random
from nltk import word_tokenize, sent_tokenize
from nltk.book import *
from nltk import bigrams

tokens = text2[:150] #This makes it so that I only get 150 tokens 
tagged_tokens = nltk.pos_tag(tokens)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective","PRON":"a pronoun"} #I got started with my code from Colleen's madlib code and just added a pronoun category
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1,"PRON":.1}

def spaced(word): #again this is from Colleen's madlib code
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = [] #creating a list to append the new text to
original_words = [] #creating a list to append the old text to
for word in tokens:
	original_words.append(spaced(word))

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print("".join(original_words))
print ("".join(final_words))

print("\n\nEND*******")
