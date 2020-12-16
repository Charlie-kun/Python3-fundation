import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from pprint import pprint

sequence = "Don't be fooled by the dark sounding name,\
    Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."
result =  text_to_word_sequence(sequence)
print(result)

import re
text = "I was wondering if anyone out there could enlighten me on this car."
shortword = re.compile(r'\W*\b\w{1,2}\b')
print(shortword.sub('', text))

import numpy as np
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from tensorflow.keras.preprocessing.text import Tokenizer
import re

text = "A barber is a person. a barber is good person.\
        A barber is huge person. he Knew A Secret!\
        The Secret He kept is huge secret. Huge secret.\
        His barber kept his word. A barber kept his word.\
        His barber kept his secret. But keeping and keeping such a huge secret\
        to himself was driving the barber crazy.\
        The barber went up a huge mountain."

shortword = re.compile(r'\W*\b\w{1,2}\b')
text = shortword.sub('', text)
print(text)

sentences = text_to_word_sequence(text)
print(sentences)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
print(tokenizer.word_index)
print(tokenizer.word_counts)
print(sentences)
seq_sentenses = np.array(tokenizer.texts_to_sequences(sentences))
print(np.ravel(seq_sentenses))

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from pprint import pprint

sentences = [['barber', 'person'],
             ['barber', 'good', 'person'],
             ['knew', 'secret'],
             ['secret', 'kept', 'huge', 'secret'],
             ['barber', 'kept', 'word'],
             ['barber', 'kept', 'secret'],
             ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'],
             ['barber', 'went', 'huge', 'mountain']]
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
pprint(sentences)

encoded = tokenizer.texts_to_sequences(sentences)
pprint(encoded)

padded = pad_sequences(encoded, padding='post')
print(f"padded = \n{padded}")

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

text="A barber is a person. He is good person. He is huge person."
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
print(tokenizer.word_index)

sub_text = "He is good person."
encoded = tokenizer.texts_to_sequences([sub_text])
pprint(encoded[0])

one_hot = to_categorical(encoded[0])
print(f"one_hot = \n{one_hot}")
