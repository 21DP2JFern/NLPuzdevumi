import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import string

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

text = text.lower().translate(str.maketrans('', '', string.punctuation))
words = word_tokenize(text)


freq_dist = FreqDist(words)

print(freq_dist.most_common())
