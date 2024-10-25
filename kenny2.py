def word_frequencies(sentence):
    words=sentence.split()
    frq_dict={}
    for word in words:
        if word in frq_dict:
            frq_dict[word]+=1
        else:
            frq_dict[word]=1
    return frq_dict
sentence="this is a test and this only test"
print(word_frequencies(sentence))