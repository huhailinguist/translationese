"""\
We assume that less frequent words are used more often in original texts than
in translated ones.
"""

import translationese
from translationese.word_ranks import WORD_RANKS
from translationese.word_ranks_zh import WORD_RANKS as WORD_RANKS_ZH
from translationese.punctuation import punctuation_marks_zh

DIGITS_ZH = {'０','１','２','３','４','５','６','７','８','９'}

VERY_HIGH_RANK = 5000
"""Very high rank for a word, guessed for unknown words. The highest rank
for known words is 5000."""

VARIANTS = [0, 1]
"""Possible variants for this hypothesis.

0. Words not in this list are given a unique highest rank of ``VERY_HIGH_RANK``.

1. Words not in the list are ignored altogether.
"""

def quantify_variant(analysis, variant):
    """Quantify mean word rank."""
    assert isinstance(analysis, translationese.Analysis)

    count = 0
    rank_sum = 0
    if analysis.lang == 'en':
        for word in analysis.tokens():
            if not word.isalpha():
                continue

            if word in WORD_RANKS:
                rank_sum += WORD_RANKS[word]
                count += 1
            else:
                if variant == 0:
                    rank_sum += VERY_HIGH_RANK
                    count += 1
                else: pass
        return { "mean_word_rank": float(rank_sum) / count }

    elif analysis.lang == 'zh':
        punctuation_marks_zh_set = set(punctuation_marks_zh)

        for word in analysis.tokens():
            if word in punctuation_marks_zh_set: continue

            # if word == ４０
            if any(char in DIGITS_ZH for char in word): continue

            if word in WORD_RANKS_ZH:
                rank_sum += WORD_RANKS_ZH[word]
                count += 1
            else:
                if variant == 0:
                    rank_sum += VERY_HIGH_RANK
                    count += 1
                else:
                    pass
        return {"mean_word_rank": float(rank_sum) / count}

    else:
        print('mean_word_rank not implemented for lang: {}'.format(analysis.lang))
        exit()
