"""\
We hypothesize that different grammatical structures used
in the different source languages interfere with the translations; and
that translations have unique grammatical structure. We model this
assumption by defining as features unigrams, bigrams and trigrams of
POS tags.
"""

from translationese.utils import output_filter_ngram, sparse_dict_increment

import os
import sys
if os.environ.get("READTHEDOCS", None) != 'True':
    from nltk.util import ngrams

VARIANTS = [0, 1, 2, 3] #: Possible variants (unigrams, bigrams, trigrams)
# 3: customized

MY_POS = {
"NN NN NN",
"NN NR NT",
"NR NR NT",
"ETC CD M",
"SP PU AD",
"NN NN PU",
"NR NT NT",
"NN NN CD",
"NN PU CS",
"DEG NN AD",
"NN CD M",
"PU AD PU",
"DT NN SP",
"PU P CS",
"AD AD VV",
"NN PU VV",
"NR NT P",
"NT P PN",
"VC DT DEG",
"PU VV NN",
}

def quantify_variant(analysis, variant):
    """Quantify POS n-grams"""
    if variant <= 2:
        n = variant + 1

        d = {}

        all_pos_tags = [ pos for (_, pos) in analysis.pos_tags() ]

        for ngram in ngrams(all_pos_tags, n):
            sparse_dict_increment(d, ngram)

        return {output_filter_ngram(k): v for (k, v) in d.items()}  # unnormalized counts
    elif variant == 3:
        n = 3
        d = {}
        all_pos_tags = [pos for (_, pos) in analysis.pos_tags()]
        for ngram in ngrams(all_pos_tags, n):
            sparse_dict_increment(d, ngram)
        return {output_filter_ngram(k): v for (k, v) in d.items() \
                if output_filter_ngram(k) in MY_POS}  # unnormalized counts

