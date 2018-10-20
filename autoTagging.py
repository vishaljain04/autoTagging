import pickle, gensim, nltk, re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from gensim import corpora, models
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel

# Input text to algorithm...

text = """ """

#Condensing the post and finding its summary
stemmer = SnowballStemmer("english")
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue

    word = stemmer.stem(word)

    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues / len(sentenceValue))

summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence
#--------------------------------------------------------------------------------------------------------

example_text = [summary] #text to be tokenized
tokenizer = RegexpTokenizer(r'\w+')
en_stop = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

texts = []
tagged = []

# loop through posts
for i in example_text:
    # Tokenizing strings
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    # Stemmer tokens
    stemmed_tokens = [lemmatizer.lemmatize(i) for i in stopped_tokens]

    # #part of speech tagging
    for i in stemmed_tokens:
        words = nltk.word_tokenize(i)
        t = nltk.pos_tag(words)
        #Getting only the nouns and adjectives
        if t[0][1] == 'NN' or t[0][1] == 'NNS' or t[0][1] == 'NNP' or t[0][1] == 'NNPS' or t[0][1] == 'JJ' or t[0][1] == 'JJR' or t[0][1] == 'JJS':
            tagged.append(t[0][0])

    tagged = set(tagged)
    texts.append(tagged) #Contains cleaned, condensed and tagged text

    dictionary = Dictionary(texts)
    new_corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    lda = LdaModel(new_corpus, num_topics=10, id2word = dictionary, passes=20)
    #Store topics in generated_topic variable
    generated_topic = lda.print_topics()
    #Converting to string
    generated_topic = str(generated_topic)
    #To get all the topics from model
    token = RegexpTokenizer(r'"\w+"')
    #To renove quotation marks from topics
    token1 = RegexpTokenizer(r'\w+')
    generated_topic = token.tokenize(generated_topic)
    generated_topic = str(generated_topic)
    generated_topic = token1.tokenize(generated_topic)
    #removing duplicate topics
    generated_topic = set(generated_topic)
    output = list(generated_topic) # 'output' contains final list of topics
