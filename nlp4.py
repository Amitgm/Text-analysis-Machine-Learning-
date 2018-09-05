from nltk.tokenize import sent_tokenize,word_tokenize
import string
from nltk.corpus import stopwords

sentence="hello there, how are you??? nice to meet you. yes go Germany"
for i in word_tokenize(sentence):
    print(i)
no_punc=[char for char in sentence if char not in string.punctuation]
no_punc=''.join(no_punc)
print(no_punc)
print(word_tokenize(no_punc))
print(sent_tokenize(no_punc))
print(no_punc.split())
clr_stopword=[word for word in no_punc.split() if word not in stopwords.words('english')]
print(clr_stopword)
