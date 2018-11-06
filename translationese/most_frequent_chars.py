"""\
ONLY FOR CHINESE
The normalized frequencies of the `N` most frequent chars in the corpus.
Punctuation marks are excluded.
"""
import translationese
from translationese import char_ranks

__author__ = "Hai Hu"
__email__ = "huhai@indiana.edu"

VARIANTS = [0, 1, 2, 3]
"""Possible variants.

0. `N` = 5
1. `N` = 10
2. `N` = 50
3. `N` = 2 的 是
"""

def quantify_variant(analysis, variant):
    """Quantify most frequent words"""
    assert isinstance(analysis, translationese.Analysis)

    num_top_words = [5, 10, 50]
    d = {}

    if variant == 3:
        d = {'的': 0, '是': 0}
    else:
        for word in char_ranks.TOP_CHARS[:num_top_words[variant]]:
            d[word] = 0

    for token in analysis.tokens():
        if token in d:
            d[token] += 1

    return {k: float(v) / len(analysis.tokens()) for (k, v) in d.items()}
