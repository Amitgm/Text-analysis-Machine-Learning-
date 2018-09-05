import string
from nltk.corpus import stopwords
s1=stopwords.words('english')[0:500]
str1="this is my first test string. wow!! we are doing just fine"
no_punc=[char for char in str1 if char not in string.punctuation]
print(no_punc)
no_punc= ''.join(no_punc)
print(no_punc)
print(no_punc.split())
clr_stopword=[word for word in no_punc.split() if word not in stopwords.words('english')]
print(clr_stopword)
clr_stopword=''.join(clr_stopword)
print(clr_stopword)
