import spacy
nlp  = spacy.load("en_core_web_md")
nlp_sm = spacy.load("en_core_web_sm")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2)) # 0.593 similarity, this makes sence because both cat and monkey are animals
print(word3.similarity(word2)) # 0.404 similarity, woule be bcause Bananas are eaten by monkies
print(word3.similarity(word1)) # 0.224 similarity, low match because both banana and cat are organic, but cats dont eat bananas

print("\n") # adding a gap between two printouts

word4 = nlp("chicken")
word5 = nlp("peacock")
word6 = nlp("dinner")

# added examples

print(word4.similarity(word5)) # 0.410 chickens and peacocks are both birds.
print(word6.similarity(word5)) # 0.151 people dont tend to eat peacocks
print(word6.similarity(word4)) # 0.428 chicken is a common dinner staple

print("\n") # adding a gap between two printouts

tokens = nlp("cat apple monkey banana")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("\n") # adding a gap between two printouts

sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f"{sentence} - {similarity}")


# Adding "en_core_web_sm" to compare sections of the code.

word7 = nlp_sm("chicken")
word8 = nlp_sm("dinner")

print("\n") # adding a gap between two printouts

print(word7.similarity(word8)) # 0.701 with "en_core_web_sm" insted of "en_core_web_md"s 0.428

tokens = nlp_sm("cat apple monkey banana") # "en_core_web_sm" comparisons
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

"""
when running with "en_core_web_sm"
There is a print that states ...small models, e.g. `en_core_web_sm`, don't ship with word vectors and only use context-sensitive tensorsand all the results are compleatly different.
Taking comparing "cat" to "apple" MD shows 0.204 and SM shows 0.696. These similarities are wildly different.
This shows that using the correct language model is vital to get a correct comparrison.
"""