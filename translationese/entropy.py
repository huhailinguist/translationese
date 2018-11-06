"""
entropy of CFGR

1. CFGR entropy for each phrasal tag: 28 features.
2. CFGR types
2. CFGR entropy + types
3. subtree entropy? (look into TSG code)
4. subtree entropy + types?
5. depTriple entropy

"""

__author__ = 'Hai Hu'
__email__ = 'huhai@indiana.edu'

import math

VARIANTS = [0, 1, 2, 3, 4, 5]
# 0: CFGR entropies
# 1: CFGR types
# 2: CFGR entropies + types
# 3: depTriple1 entropies
# 4: depTriple1 types
# 5: depTriple1 entropies + types

ph_tags = ['ADJP', 'ADVP', 'CLP', 'CP', 'DFL', 'DNP', 'DP', 'DVP',
           'FLR', 'FRAG', 'INC', 'INTJ', 'IP', 'LCP', 'LST', 'NP',
           'PP', 'PRN', 'QP', 'ROOT', 'UCP', 'VCD', 'VCP', 'VNV',
           'VP', 'VPT', 'VRD', 'VSB']  # 28 tags in total

POS_tags = ['AD', 'AS', 'BA', 'CC', 'CD', 'CS', 'DEC', 'DEG', 'DER', 'DEV',
              'DT', 'ETC', 'FW', 'IJ', 'JJ', 'LB', 'LC', 'M', 'MSP', 'NN', 'NR', 'NT', 'OD', 'ON',
              'P', 'PN', 'PU', 'SB', 'SP', 'VA', 'VC', 'VE', 'VV']  # 33 tags in total

class EntropyQuantifier:
    def __init__(self, variant):
        self.k = variant

    def quantify(self, analysis):

        # ------------
        # CFGR entropy
        if self.k in [0,1,2]:
            res = {}
            # print(analysis.CFGRs())
            # {'ADVP -> AD': 75, 'VP -> ADVP QP VP': 1 ...}
            for ph_tag in ph_tags:
                # the count of each rule starting with ph_tag
                counts = [analysis.CFGRs()[key] for key in analysis.CFGRs().keys() \
                                 if key.split()[0] == ph_tag]
                sumCounts = sum( counts )
                entropy = - sum( [ count/sumCounts * math.log2(count/sumCounts) \
                               for count in counts] )
                # print(ph_tag, sumCounts, entropy)
                if self.k in [0, 2]:
                    res[ph_tag+'_entropy'] = entropy
                if self.k in [1, 2]:
                    res[ph_tag + '_types'] = 0  # number of CFGR that start with ph_tag
                    res[ph_tag + '_types'] = sum( [1 for key in analysis.CFGRs().keys() \
                                 if key.split()[0] == ph_tag ] )
                    # for rule in analysis.CFGRs().keys():
                    #     if rule.split()[0] == ph_tag:
                    #         res[ph_tag + '_types'] += 1

            # get alltag_entropy and alltag_types
            if self.k in [1, 2]:
                res['alltag_types'] = len(analysis.CFGRs().keys())
            if self.k in [0, 2]:
                # sumCounts = sum( analysis.CFGRs().values() )
                # res['alltag_entropy'] = - sum( [ count / sumCounts * math.log2(count/sumCounts) \
                #                    for count in analysis.CFGRs().values()] )
                # sum entropies
                res['alltag_entropy'] = sum( [res[key] for key in res.keys() if key.endswith('_entropy')] )
            return res

        # ----------------
        # depTriple
        else:
            res = {}
            triples = {}  # {nsubj: {VV_nsubj_NR: 10, ...} ...

            depParses = analysis.depParses()

            assert len(analysis.pos_tags_by_sentence()) == len(depParses)
            for idx in range(len(depParses)):
                pos_tags = analysis.pos_tags_by_sentence()[idx]
                depParse = analysis.depParses()[idx]
                assert len(pos_tags) == len(depParse)

                for i in range(len(depParse)):
                    # pos_tags: [('张三', 'NR'), ('买', 'VV'), ('了', 'AS'), ... ]
                    # depTriple: [('ROOT', 0, 2), ('nsubj', 2, 1), ('aux:asp', 2, 3),  ... ]
                    depTriple = depParse[i]  # ('nsubj', 2, 1)
                    head = pos_tags[depTriple[1] - 1]  # ('买', 'VV')
                    dependent = pos_tags[depTriple[2] - 1]  # ('张三', 'NR')
                    relation = depTriple[0]  # nsubj

                    depTriple1 = '_'.join([head[1], relation, dependent[1]])
                    # depTriple1: VV_nsubj_NR
                    head_pos = head[1]
                    if head_pos not in triples: triples[head_pos] = {}
                    triples[head_pos][depTriple1] = triples[head_pos].get(depTriple1, 0) + 1

            # calculate entropy
            # according to chen et al 2009, Using entropy to evaluate child language performance, CUNY
            # H(G) = sum_i sum_j ( P(rule_j|head_i) * log(P(rule_j|head_i))  )

            Hs = {}  # H for each relation
            for head_pos in triples.keys():  # relation = rule
                sum_head = sum( triples[head_pos].values() )
                Hs[head_pos] = - sum( triples[head_pos][depTriple1] / sum_head * \
                                      math.log2( triples[head_pos][depTriple1] / sum_head ) \
                                      for depTriple1 in triples[head_pos].keys() )
                # print('H for {} is {}'.format(head_pos, Hs[head_pos]))
                if self.k in [3, 5]:
                    res[head_pos+'_dep_entropy'] = Hs[head_pos]
                if self.k in [4, 5]:
                    res[head_pos+'_dep_type'] = len(triples[head_pos].keys())

            # compute H(G)
            if self.k in [3, 5]:
                res['allhead_entropy'] = sum(Hs.values())
            if self.k in [4, 5]:
                res['allhead_type'] = sum([ len(triples[head_pos].keys()) for head_pos in triples.keys() ])

            return res

def quantify_variant(analysis, variant):
    """ Quantify entropy. """
    quantifier = EntropyQuantifier(variant)
    return quantifier.quantify(analysis)

