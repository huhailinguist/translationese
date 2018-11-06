"""\
Translations are known to excessively use certain cohesive markers (see list
below).
"""

import os
if os.environ.get("READTHEDOCS", None) != 'True':
    import nltk

from translationese.utils import sparse_dict_increment

VARIANTS = [0, 1, 2, 3, 4]

"""List of cohesive markers"""
COHESIVE_MARKERS = ["as for",
"as to",
"because",
"besides",
"but",
"consequently",
"despite",
"even if",
"even though",
"except",
"further",
"furthermore",
"hence",
"however",
"in addition",
"in conclusion",
"in other words",
"in spite",
"instead",
"is to say",
"maybe",
"moreover",
"nevertheless",
"on account of",
"on the contrary",
"on the other hand",
"otherwise",
"referring to",
"since",
"so",
"the former",
"the latter",
"therefore",
"this implies",
"though",
"thus",
"with reference to",
"with regard to",
"yet",
"concerning"]
# how about:
# additionally, in addition, as a consequence,
# why "this implies" is in there??

# 81 in total. 现代汉语 黄廖本 下 p27.
COHESIVE_MARKERS_ZH = sorted([
# 连接词语或分句：
"而", "而且", "并", "并且", "或者",

# 连接复句：
# 现代汉语 黄廖本 下 p128起 只包含 单用 的：
# 1 并列：
"也", "又", "同时", "同样", "另外", "而是",
# 2 顺承：
"便", "就", "再", "于是", "然后", "后来", "接着", "跟着", "继而", "终于",
# 3 解说：
# 4 选择：
"或是", "还是", "还不如", "倒不如",
# 5 递进：
"况且", "甚至", "以至", "更", "还", "甚至于", "尚且", "何况", "反而",
# 1 偏正：
"便", "就", "才", "要不然",
# 2 假设：
"那么", "就", "便", "则", "的话",
# 3 因果：
"因为", "由于", "所以", "因此", "因而", "以致", "致使", "从而", "以至于", "以至", "既然", "既", "就", "可见",
# 4 目的：
"以", "以便", "以求", "用以", "借以", "好让", "为的是", "以免", "免得", "省得", "以防",
# 5 转折：
"虽然", "但是", "但", "然而", "可是", "可", "却", "只是", "不过", "倒",

# others:
"首先", "其次", "最后",

# TODO 合用的可以用 parse tree + tregex 来找

])

# segment every marker by stanford corenlp
COHESIVE_MARKERS_ZH_SEG = [
    ['不过'], ['为的是'], ['也'], ['于是'], ['从而'], ['以'], ['以便'], ['以免'], ['以求'], ['以至'], ['以至于'], ['以致'], ['以防'], ['但'],
    ['但是'], ['何况'], ['便'], ['倒'], ['倒不如'], ['借以'], ['免得'], ['其次'], ['再'], ['况且'], ['则'], ['却'], ['又'], ['反而'], ['另外'],
    ['只是'], ['可'], ['可是'], ['可见'], ['同时'], ['同样'], ['后来'], ['因为'], ['因此'], ['因而'], ['好让'], ['尚且'], ['就'], ['并'], ['并且'],
    ['或是'], ['或者'], ['所以'], ['才'], ['接着'], ['既'], ['既然'], ['更'], ['最后'], ['然后'], ['然而'], ['甚至'], ['甚至于'], ['用以'],
    ['由于'], ['的话'], ['省得'], ['终于'], ['继而'], ['而'], ['而且'], ['而是'], ['致使'], ['虽然'], ['要不然'], ['跟着'], ['还'], ['还不如'],
    ['还是'], ['那么'], ['首先'],
]

# 160 in total. cohesive markers from Chen 2006 pp. 395 ECPC-CN.
COHESIVE_MARKERS_CHEN_2006 = [
"而",
"如果",
"但",
"因为",
"但是",
"就是",
"因此",
"而且",
"由于",
"并",
"那么",
"所以",
"尽管",
"然而",
"并且",
"于是",
"即使",
"而是",
"可是",
"的话",
"不过",
"虽然",
"只要",
"无论",
"不仅",
"既",
"一旦",
"假如",
"那",
"结果",
"因",
"不管",
"只有",
"从而",
"之所以",
"要么",
"另外",
"即便",
"以",
"另一方面",
"以便",
"否则",
"此外",
"若",
"且",
"因而",
"要是",
"也就是说",
"除非",
"只是",
"便是",
"既然",
"不论",
"以致",
"换句话说",
"如",
"连",
"一方面",
"尽管",
"反而",
"以至于",
"如果说",
"不但",
"其次",
"虽",
"就是说",
"就算",
"进而",
"无论如何",
"以至",
"据说",
"以致于",
"为之",
"反之",
"总之",
"加上",
"故",
"还不如",
"以免",
"不用说",
"换言之",
"不如",
"一般来说",
"反过来",
"起见",
"倘若",
"万一",
"同理",
"相反地",
"这样一来",
"鉴于",
"假使",
"假若",
"再者",
"反倒",
"固然",
"借以",
"虽说",
"相形之下",
"除此之外",
"乃至",
"要不是",
"总的来说",
"不然",
"以防",
"其一",
"因之",
"更何况",
"况且",
"非但",
"总而言之",
"其二",
"另",
"若要",
"据信",
"于此",
"有鉴于此",
"归根到底",
"由此可见",
"简言之",
"二来",
"故而",
"若是",
"要不",
"一般而言",
"一言以蔽之",
"俗话说",
"如此一来",
"想不到",
"简而言之",
"话说回来",
"除此以外",
"不独",
"倘使",
"倘然",
"再就是",
"凡",
"凡是",
"加之",
"即令",
"即或",
"哪是",
"唯独",
"如若",
"故此",
"毋宁",
"甚而",
"与其",
"要不然",
"那怕",
"反过来说",
"可想而知",
"曾几何时",
"有道是",
"归根结底",
"总的来看",
"总的说来",
"老实说",
"话说",
"说到底",
"说真的"
]

ADVERSATIVES = {
"但",
"但是",
"然而",
"可是",
"不过"
}

class CohesiveMarkerQuantifier:
    def __init__(self, variant):
        self.k = variant

    def quantify(self, analysis):
        """Quantify usage of cohesive markers."""
        result = {}

        if analysis.lang == 'en':
            tokenized_markers = [(marker,nltk.word_tokenize(marker)) for marker in COHESIVE_MARKERS]
            text = analysis.tokens()

            for i, _ in enumerate(text):
                for (marker,tokenized) in tokenized_markers:
                    if (tokenized == text[i:i+len(tokenized)]):
                        sparse_dict_increment(result, marker)

        elif analysis.lang == 'zh':
            if self.k == 0:
                markers = COHESIVE_MARKERS_ZH
            elif self.k == 1:
                markers = COHESIVE_MARKERS_CHEN_2006
            elif self.k == 2:
                markers = ["即", "也就是说"]
            elif self.k == 3:  # top 5 from Chen's list, using GainRatio from weka.
                markers = ["但是", "因为", "据说", "那么", "如果"]
            elif self.k == 4:  # adversative markers 转折词
                markers = ADVERSATIVES

            text = analysis.tokens()

            for i, _ in enumerate(text):
                for marker in markers: # marker = '不过'
                    # marker can be segmented to at most len(marker) parts
                    # for j in range(1, len(marker)+1):
                    # But we assume marker can be segmented to at most 3 parts
                    for j in range(1, min( len(marker)+1, 4)):
                        if (marker == ''.join(text[i:i+j])):
                            sparse_dict_increment(result, marker)

            ''' # old
            assert len(COHESIVE_MARKERS_ZH) == len(COHESIVE_MARKERS_ZH_SEG)

            # [('不过', ['不过']), ... ]
            tokenized_markers = \
                [(COHESIVE_MARKERS_ZH[i], COHESIVE_MARKERS_ZH_SEG[i]) \
                for i in range(len(COHESIVE_MARKERS_ZH))]

            for i, _ in enumerate(text):
                for (marker, tokenized) in tokenized_markers:
                    if (tokenized == text[i:i + len(tokenized)]):
                        sparse_dict_increment(result, marker)
            '''

        else:
            print('language "{}" not implemented yet for cohesive_markers'.format(analysis.lang))
            exit()

        pairs = [ (marker, float(result[marker]) / len(text)) for marker in result.keys()]

        return dict(pairs)

def quantify_variant(analysis, variant):
    """Quantify cohesive markers."""
    quantifier = CohesiveMarkerQuantifier(variant)
    return quantifier.quantify(analysis)