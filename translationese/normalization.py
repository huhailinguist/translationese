"""
Normalization, from Baker 1996

``Normalisation (or conservatism) is a tendency to exaggerate features of the
target language and to conform to its typical patterns.

Normalisation is most evident in the use of typical grammatical
structures, punctuation and collocational patterns or clichés.''
"""

__author__ = "Hai Hu"

from collections import Counter

# Possible variants (
# 0: ZH_ASPECT_MARKERS, 1: ZH_MEASURE_WORDS, 2: ZH_SENT_FINAL_PARTICLE
# 3: counts of measure words in total
VARIANTS = [0, 1, 2, 3]

# pos = AS
ZH_ASPECT_MARKERS = [
    "着", "了", "过",
]

# pos = M
# already cleaned
ZH_MEASURE_WORDS = [
    "个", "张", '处', '式', '朵', '些', '例', '章',
    '块', '重', '倍', '架', '门', '顿', '年', '部分', '台', '名', '级',
    '排排', '千伏', '员', '点', '户', '桶', '度', '类', '批',
    '起', '头', '天', '首', '尾', '周',
    '班', '位', '届', '秒', '瓦', '轮',
    '组', '罐', '项', '盘', '股', '篇', '封', '口', '岁', '刻', '串', '根', '斑斑',
    '笔', '宗', '个', '日', '颗', '站', '千瓦', '锭', '界', '场', '局', '目',
    '代', '套', '艘', '分钟', '张', '段',
    '人份', '页', '支', '片', '只', '路',
    '座', '种', '系列', '辆', '对', '间',
    '枚', '所', '株', '家', '条款', '角',
    '桩', '幅', '层', '载', '个把', '分', '等',
    '人次', '期', '埃居', '次', '台套', '部', '番',
    '件', '幢', '里', '份', '平米', '号',
    '步', '线', '伏', '条', '架次', '队', '本',
]

# Huang Liao textbook  part II, pp 31
# pos = SP
ZH_SENT_FINAL_PARTICLE = [
    "吧", "呢", "啊", "嘛", "呗", "罢了", "也罢", "也好", "啦", "嘞", "喽", "着呢",
    "吗", "呐", "么", "呀", "哇"
]

class NormalizationQuantifier:
    def __init__(self, variant):
        self.k = variant

    def quantify(self, analysis):
        # [('粮农', 'JJ'), ('组织', 'NN'), ('的', 'DEG'), ('负责人', 'NN'), ... ]
        pos_tags = analysis.pos_tags()
        # token_pos = ['粮农_JJ', '组织_NN' ... ]
        token_pos = [pos_tag[0] + "_" + pos_tag[1] for pos_tag in pos_tags]
        poss = [pos_tag[1] for pos_tag in pos_tags]

        # get a frequency dictionary
        freq = Counter(token_pos)

        text = analysis.tokens()
        mil = 1000000  # we want # token per million word

        if analysis.lang == 'zh':
            if self.k == 0:  # ZH_ASPECT_MARKERS
                ZH_ASPECT_MARKERS_w_pos = [word + "_" + "AS" for word in ZH_ASPECT_MARKERS]
                pairs = [(word, freq.get(word, 0.0) / len(text) * mil) for word in ZH_ASPECT_MARKERS_w_pos]

            elif self.k == 1:  # ZH_MEASURE_WORDS
                ZH_MEASURE_WORDS_w_pos = [word + "_" + "M" for word in ZH_MEASURE_WORDS]
                pairs = [(word, freq.get(word, 0.0) / len(text) * mil) for word in ZH_MEASURE_WORDS_w_pos]

            elif self.k == 2:  # ZH_SENT_FINAL_PARTICLE
                ZH_SENT_FINAL_PARTICLE_w_pos = [word + "_" + "SP" for word in ZH_SENT_FINAL_PARTICLE]
                pairs = [(word, freq.get(word, 0.0) / len(text) * mil) for word in ZH_SENT_FINAL_PARTICLE_w_pos]

            elif self.k == 3:  # total counts of measure words
                return {'measure_word_total_counts': poss.count('M')}

        else:
            print('normalization for lang {} not implemented yet!'.format(analysis.lang))
            exit()

        return dict(pairs)

def quantify_variant(analysis, variant):
    """Quantify normalization."""
    quantifier = NormalizationQuantifier(variant)
    return quantifier.quantify(analysis)
