"""\
word n-grams
"""

from translationese.utils import output_filter_ngram, sparse_dict_increment

import os
import sys
if os.environ.get("READTHEDOCS", None) != 'True':
    from nltk.util import ngrams

VARIANTS = [0, 1, 2] #: Possible variants (unigrams, bigrams, trigrams)

def quantify_variant(analysis, variant):
    """Quantify word n-grams"""
    n = variant + 1

    d = {}

    all_words = [ word for (word, _) in analysis.pos_tags() ]

    for ngram in ngrams(all_words, n):
        sparse_dict_increment(d, ngram)

    return {output_filter_ngram(k): v for (k, v) in d.items()}  # unnormalized counts
