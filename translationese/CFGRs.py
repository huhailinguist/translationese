"""
normalized context-free grammar (CFG) rule counts as features
"""

__author__ = "Hai Hu"
__email__ = "huhai@indiana.edu"

VARIANTS = [0, 1, 2, 3, 4, 5, 6, 7] #: Possible variants
# 0: all
# 1: count >= 3
# 2: count >= 10
# 3: count >= 20
# 4: top 100 based on GainRatio feat selection
# 5: top 50 based on GainRatio feat selection
# 6: top 20 based on GainRatio feat selection
# 7: all NP rules
# 8: top 30 NP rules

TOP = [
"VP -> VV NP QP",
"VP -> NP PP VP",
"ADVP -> AD",
"VP -> VP PU VP PU VP",
"NP -> NN PU NN",
"ROOT -> FRAG",
"NP -> NN NN NN NN",
"ADVP -> CS",
"NP -> NP NP",
"CP -> ADVP IP",
"CP -> IP SP",
"NP -> NP QP NP",
"NP -> NP PU NP",
"ROOT -> CP",
"VP -> VC VP",
"NP -> NP NP NP",
"NP -> DNP NP",
"VP -> VP PU VP PU VP PU VP",
"NP -> NP ADJP NP",
"VP -> VV VP",
"NP -> NP QP ADJP NP",
"NP -> NP NP ADJP NP",
"NP -> NN PU NN PU NN",
"CP -> IP SP PU",
"VCD -> VV VV",
"VP -> ADVP ADVP ADVP VP",
"NP -> NN NN NN",
"IP -> ADVP NP VP PU",
"NP -> NN PU NN NN",
"VP -> VC PU IP",
"IP -> ADVP PU NP VP",
"NP -> PN PN",
"IP -> ADVP NP VP",
"VP -> VV NP NP",
"PP -> P QP",
"IP -> IP PU IP PU IP PU IP PU",
"VP -> MSP VP",
"DNP -> ADJP DEG",
"IP -> IP PU IP PU IP",
"NP -> CP",
"VP -> ADVP ADVP VP",
"VP -> VC PP",
"NP -> NN NN",
"ROOT -> IP",
"VP -> VC NP",
"IP -> IP PU IP PU IP PU IP PU IP PU",
"ADJP -> ADVP ADJP",
"NP -> PN",
"VP -> VP PU VP",
"IP -> ADVP PU NP VP PU",
"VP -> VP PU VP PU IP",
"NP -> NR PRN",
"VP -> QP",
"NP -> QP DNP NP",
"VRD -> VV VA",
"IP -> PP NP VP",
"ROOT -> PRN",
"NP -> NN NN CC NN NN",
"IP -> IP PU VP",
"CP -> ADVP CP",
"VP -> ADVP PP PP VP",
"IP -> NP PU VP",
"IP -> ADVP PU VP PU",
"IP -> ADVP VP PU",
"IP -> CP PU ADVP NP VP",
"VP -> VCD",
"VP -> LCP PU VP",
"VP -> VSB",
"IP -> VP PU",
"VP -> VV PU CP",
"IP -> PP PU IP PU",
"NP -> NP NP NP NP",
"DNP -> NP DEG",
"ADJP -> NN",
"NP -> IP NP",
"VP -> LST VP",
"IP -> IP PU IP PU IP PU IP",
"VSB -> VV VV",
"IP -> CP PU NP VP PU",
"IP -> IP PU IP",
"NP -> QP CP NP",
"IP -> LCP PU NP VP",
"QP -> QP QP QP",
"DVP -> VP DEV",
"NP -> NP PU NP ETC",
"CLP -> ADJP CLP",
"VP -> PP PU PP VP",
"VP -> PP ADVP VP",
"PRN -> PU IP",
"IP -> NP VP PU PP PU",
"LCP -> LCP LC",
"IP -> ADVP PU PP PU NP VP PU",
"VP -> DVP VP",
"VP -> VV AS",
"NP -> NN NN PU NN",
"NP -> NR PU NR PU NR",
"NP -> CP QP ADJP NP",
"NP -> PU NP PU",
"NP -> NN NN NN NN NN NN",
"NP -> DP CP NP"
]

TOP_NP = [
"NP -> NN PU NN",
"NP -> NN NN NN NN",
"NP -> NP NP",
"NP -> NP QP NP",
"NP -> NP PU NP",
"NP -> NP NP NP",
"NP -> DNP NP",
"NP -> NP ADJP NP",
"NP -> NP QP ADJP NP",
"NP -> NP NP ADJP NP",
"NP -> NN PU NN PU NN",
"NP -> NN NN NN",
"NP -> NN PU NN NN",
"NP -> PN PN",
"NP -> CP",
"NP -> NN NN",
"NP -> PN",
"NP -> NR PRN",
"NP -> QP DNP NP",
"NP -> NN NN CC NN NN",
"NP -> NP NP NP NP",
"NP -> IP NP",
"NP -> QP CP NP",
"NP -> NP PU NP ETC",
"NP -> NN NN PU NN",
"NP -> NR PU NR PU NR",
"NP -> CP QP ADJP NP",
"NP -> PU NP PU",
"NP -> NN NN NN NN NN NN",
"NP -> DP CP NP"
]

class CFGRQuantifier:
    def __init__(self, variant):
        self.k = variant

    def quantify(self, analysis):
        """Quantify CFGRs."""
        # print(analysis.CFGRs())
        # print(Counter(analysis.CFGRs()))
        # exit()
        numCFGRtotal = sum(analysis.CFGRs().values())
        if self.k == 0:
            return { rule : count/numCFGRtotal for rule, count \
                     in analysis.CFGRs().items() }
        elif self.k == 1:
            return { rule : count/numCFGRtotal for rule, count \
                     in analysis.CFGRs().items() if count >= 3}
        elif self.k == 2:
            return { rule : count/numCFGRtotal for rule, count \
                     in analysis.CFGRs().items() if count >= 10}
        elif self.k == 3:
            return { rule : count/numCFGRtotal for rule, count \
                     in analysis.CFGRs().items() if count >= 20}
        elif self.k == 4:
            return { rule : count/numCFGRtotal for rule, count \
                     in analysis.CFGRs().items() if rule in TOP}
        elif self.k == 5:
            return { rule : count/numCFGRtotal for rule, count \
                     in analysis.CFGRs().items() if rule in TOP[:50]}
        elif self.k == 6:
            return { rule : count/numCFGRtotal for rule, count \
                     in analysis.CFGRs().items() if rule in TOP[:20]}
        elif self.k == 7:
            NP_CFGR_total = sum( [analysis.CFGRs()[rule] for rule in analysis.CFGRs().keys() \
                                  if rule.startswith('NP ')] )
            return { rule : count/NP_CFGR_total for rule, count \
                     in analysis.CFGRs().items() if rule.startswith('NP ') }
        elif self.k == 8:
            NP_CFGR_total = sum( [analysis.CFGRs()[rule] for rule in analysis.CFGRs().keys() \
                                  if rule.startswith('NP ')] )
            print(NP_CFGR_total)
            return { rule : count/NP_CFGR_total for rule, count \
                     in analysis.CFGRs().items() if rule in TOP_NP }

def quantify_variant(analysis, variant):
    """Quantify CFGRs """
    quantifier = CFGRQuantifier(variant)
    return quantifier.quantify(analysis)
