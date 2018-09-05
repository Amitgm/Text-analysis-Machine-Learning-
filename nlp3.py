from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer()
doc1="hi how are are you"
doc2="today is a very pleasant day ans we can have fun fun  fun"
doc3="this was an amazing experience"
list1=[doc1,doc2,doc3]
bag_of_words=vectorizer.fit(list1)
bag_of_words=vectorizer.transform(list1)
print(vectorizer.vocabulary_.get('an'))
print(type(bag_of_words))
