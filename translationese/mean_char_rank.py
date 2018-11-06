"""\
ONLY FOR CHINESE

We assume that less frequent characters are used more often in original texts than
in translated ones.
"""

import translationese
from translationese.char_ranks import CHAR_RANKS

__author__ = "Hai Hu"
__email__ = "huhai@indiana.edu"

VERY_HIGH_RANK = 5000
"""Very high rank for a word, guessed for unknown words. The highest rank
for known words is 5000."""

VARIANTS = [0, 1]
"""Possible variants for this hypothesis.

0. Words not in this list are given a unique highest rank of ``VERY_HIGH_RANK``.

1. Words not in the list are ignored altogether.
"""

NUMS_PUNCS_LETTERS = {
    "１", "２", "３", "４", "５", "６", "７", "８", "９", "０",
    "Ａ", "Ｂ", "Ｃ", "Ｄ", "Ｅ", "Ｆ", "Ｇ", "Ｈ", "Ｉ", "Ｊ", "Ｋ", "Ｌ", "Ｍ", "Ｎ",
    "Ｏ", "Ｐ", "Ｑ", "Ｒ", "Ｓ", "Ｔ", "Ｕ", "Ｖ", "Ｗ", "Ｘ", "Ｙ", "Ｚ",
    "ａ", "ｂ", "ｃ", "ｄ", "ｅ", "ｆ", "ｇ", "ｈ", "ｉ", "ｊ", "ｋ", "ｌ", "ｍ", "ｎ",
    "ｏ", "ｐ", "ｑ", "ｒ", "ｓ", "ｔ", "ｕ", "ｖ", "ｗ", "ｘ", "ｙ", "ｚ",
    "＃", "￥", "％", "＆", r"\\", "/", "？", "！", "：", "；", "——", "—",
    "（", "）", "【", "】", "‘", "’", "“", "”", "、", "，", "。", "《", "》", "……", "…",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f",
    "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H",
    "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
    "W", "X", "Y", "Z", "?", "!", ":", ";", "-", "(", ")", "{", "}", "[",
    "]", ",", ".", "\"", "'",
                      }
"""
numbers, punctuations and letters in Chinese, full-width
"""

def quantify_variant(analysis, variant):
    """Quantify mean word rank."""
    assert isinstance(analysis, translationese.Analysis)

    count = 0
    rank_sum = 0

    for char in analysis.chars():
        # ignore numbers and punctuations
        if char in NUMS_PUNCS_LETTERS:
            continue

        if char in CHAR_RANKS:
            rank_sum += CHAR_RANKS[char]
            count += 1
        else:
            if variant == 0:
                rank_sum += VERY_HIGH_RANK
                count += 1
            else:
                pass

    return { "mean_word_rank": float(rank_sum) / count }
