# Initialize logging.
import logging, os
from nltk.corpus import stopwords
from nltk import download
from time import time

from gensim.models import Word2Vec, KeyedVectors
from gensim.test.utils import get_tmpfile
# from pyemd import emd
from gensim.similarities import WmdSimilarity

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')

MODEL_FILE = "word_vectors.kv"

# Remove stopwords.
download('stopwords')  # Download stopwords list.
stop_words = stopwords.words('english')

sentence_obama = 'Obama speaks to the media in Illinois'
sentence_president = 'The president greets the press in Chicago'
sentence_obama = sentence_obama.lower().split()
sentence_president = sentence_president.lower().split()

sentence_obama = [w for w in sentence_obama if w not in stop_words]
sentence_president = [w for w in sentence_president if w not in stop_words]

start = time()
# if not os.path.exists(MODEL_FILE):
#     print(os.path.join(MODEL_FILE))
#     word_vector_model_file_path = os.path.join(MODEL_FILE)
# else:
#     raise ValueError("SKIP: Model file not found")

wordVectorModel = KeyedVectors.load(MODEL_FILE, mmap='r')

print('Cell took %.2f seconds to run.' % (time() - start))


# wordVectorModel.init_sims(replace=True)  # Normalizes the vectors in the word2vec class.
start = time()
distance = wordVectorModel.wmdistance(sentence_obama, sentence_president)  # Compute WMD as normal.

print('Distance calc took %.2f seconds to run.' %(time() - start))
print("distance: {}", distance)