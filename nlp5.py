from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()

words='swim swimmer swimming swims swimly'

words=word_tokenize(words)

for w in words:
 print(ps.stem(w))



