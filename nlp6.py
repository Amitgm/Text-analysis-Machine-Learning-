import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer,word_tokenize

sample_test= state_union.raw("2006-GWBush.txt")
sample_train=state_union.raw("2005-GWBush.txt")

custom_sent_tokenizer=PunktSentenceTokenizer(sample_train)

tokenize=custom_sent_tokenizer.tokenize(sample_test)
#words =word_tokenize(tokenizerr)
#print(words)

for w in tokenize:
    words=word_tokenize(w)
    tagged=nltk.pos_tag(words)
    print(tagged)
    chunkgram= r"""Chunk: {<.*>+}
                             }<NNP.?>+{"""
    chunkParser =nltk.RegexpParser(chunkgram)
    chunked=chunkParser.parse(tagged)
    print(chunked)
    

