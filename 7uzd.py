from gensim.models import Word2Vec


sentences = [["māja", "ir", "balta"], ["dzīvoklis", "ir", "mazs"], ["jūra", "ir", "zilā"]]
model = Word2Vec(sentences, vector_size=50, min_count=1)

print("Vārdu 'māja' un 'dzīvoklis' līdzība:", model.wv.similarity("māja", "dzīvoklis"))
print("Vārdu 'māja' un 'jūra' līdzība:", model.wv.similarity("māja", "jūra"))
