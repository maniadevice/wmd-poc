import logging
import os
from gensim.models import Word2Vec, KeyedVectors
from gensim.test.utils import get_tmpfile

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
FILE_NAME = "GoogleNews-vectors-negative300.bin.gz"
VECTOR_LIMIT = None

if not os.path.exists(FILE_NAME):
    raise ValueError("SKIP: File not found")

start = time()
wordVectorModel = KeyedVectors.load_word2vec_format(FILE_NAME, binary=True, limit=VECTOR_LIMIT)
# wordVectorModel.init_sims(replace=True)  # Normalizes the vectors in the word2vec class.
vector_file = get_tmpfile("word_vectors.kv")
wordVectorModel.save(vector_file)

print("Cell took %.2f seconds to run." % (time() - start))