#!/usr/bin/env python3
"""
get cohesive marker entropy, ttr from
../ckxx_arff3/ckxx_cohesive_markers:1.csv

Hai Hu
"""

import pandas as pd
import numpy as np
import sys, os, glob, math
from translationese import Analysis
from stanfordcorenlp import StanfordCoreNLP

def getFeats():
    # get cohesive markers
    df = pd.read_csv('../ckxx_arff3/ckxx_cohesive_markers:1.csv', index_col=0)
    # df = df.iloc[:20]
    print(df.head())

    # get num of tokens for each text
    mynlp = StanfordCoreNLP('http://localhost', port=9000, lang='en')

    totalTokens = {}

    for fn in sorted(glob.glob('../ckxx_T/*')+glob.glob('../ckxx_O_XIN/*')):
        if fn.endswith('analysis'): continue
        # if fn == '../ckxx_O_XIN/XIN_0020': break
        myAna1 = Analysis(filename=fn)
        myAna1.stanfordnlp = mynlp
        myAna1.loadcache()

        # print(os.path.basename(myAna1.filename))
        # print(len(myAna1.case_tokens()))
        totalTokens[os.path.basename(myAna1.filename)] = len(myAna1.case_tokens())

    df2 = pd.DataFrame.from_dict(data=totalTokens,
                                 orient='index')
    df2.columns = ['totalTokens']
    df2.sort_index(axis=0, inplace=True)
    print(df2.head())

    # concat two df's
    df = pd.concat([df, df2], axis=1)

    # get raw counts
    mycols = list(df.columns)
    mycols.remove('totalTokens')
    print(mycols[-5:])
    df[mycols] = df[mycols].multiply(df['totalTokens'], axis="index")
    print(df.head())

    ##############
    # get entropy
    # remove 'totalTokens'
    df_new = df.iloc[:, :-1]  # work on a copy, exclude last col = totalTokens
    # df_new.drop(['totalTokens'], axis=1, inplace=True)
    df_new['numCohMkrs'] = df_new.sum(axis=1)
    print(df_new.head())

    df_new.iloc[:, :-1] = df_new.iloc[:, :-1].div(df_new['numCohMkrs'], axis=0)
    print(df_new.head(10))

    df_new['entropy'] = \
        - df_new.iloc[:, :-1].multiply(
            np.log2(df_new.iloc[:, :-1])
        ).sum(axis=1)
    print(df_new.head(10))  # first row 3.217797

    # sanity check first row entropy:
    ps = list(df_new.iloc[0, :-2])
    en = -sum([x * math.log2(x) for x in ps if x != 0])
    print(en)  # 3.217796811598595
    # CORRECT!

    # get TTR: type / token
    # number of non-zeros in each row: type
    df_new['TTR1'] = 6 * df.astype(bool).sum(axis=1) / df['totalTokens']
    df_new['TTR2'] = 6 * np.log(df.astype(bool).sum(axis=1)) / np.log(df['totalTokens'])

    df_new['class'] = 'T'
    df_new.loc[df.index.str.contains('XIN'), 'class'] = 'O'

    print(df_new.head(10))

    # save
    df_new.iloc[:, -5:-1].to_csv('ckxx_cohesive_markers_entropy_TTR.csv')
    df_new.iloc[:, -5:].to_csv('ckxx_cohesive_markers_entropy_TTR_weka.csv', index=0)

if __name__ == '__main__':
    getFeats()


