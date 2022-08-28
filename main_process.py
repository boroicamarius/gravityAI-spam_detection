import pandas as pd
import tensorflow as tf
import pickle
import nltk
import json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from gravityai import gravityai as grav

nltk.download('punkt')

model = tf.keras.models.load_model('model.h5')
tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(
    json.load(open('tokenizer.json')))


def process(inPath, outPath):

    input = pd.read_csv(inPath)
    print(input)
    input_to_feed = []
    print(input_to_feed)

    for index, row in input.iterrows():
        input_to_feed.append(' '.join(nltk.tokenize.word_tokenize(row[0])))

    print(input_to_feed)
    input['results'] = model.predict(pad_sequences(
        tokenizer.texts_to_sequences(input_to_feed), maxlen=200))
    output = input[['strings', 'results']]
    print(input)
    output.to_csv(outPath, index=False)


grav.wait_for_requests(process)
