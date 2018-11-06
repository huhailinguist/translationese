# Chinese translationese 

Hai Hu, forked and modifed from https://github.com/lutzky/translationese

Documentation of the original implementation is available here: https://translationese.readthedocs.org/

## Modifications

1. Use Stanford CoreNLP instead of NLTK. CoreNLP is more accurate and also allows you to easily extend to other languages. You need to install and fire up a [CoreNLP server](https://stanfordnlp.github.io/CoreNLP/corenlp-server.html) locally and then process text data. You will also need a python wrapper for CoreNLP which is already in this folder. It is a modification of the wrapper from [here](https://github.com/Lynten/stanford-corenlp).

2. Change the code from python2 to python3.

3. New translationese features (or modules) are added, some of which specific to Chinese. The newly added modules include: ba\_structure, bei\_structure, context-free grammar rules (CFGRs.py), char\_rank, chengyu, etc. 

The original code by Lutzky and Star have suffix `_old`. 

## How to run

1. Install Stanford CoreNLP [server](https://stanfordnlp.github.io/CoreNLP/corenlp-server.html). Download their Chinese model [here](https://stanfordnlp.github.io/CoreNLP/index.html#download). Then fire up the server by opening a terminal, going to the folder where the server is installed and type `java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000`.

2. Now you can run translationese modules. You can type `python3 analyze.py -h` to see the help message. To test a module say POS unigram, use:

```
python3 analyze.py pos_n_grams:0 -d myoutput/ -o o/ -t t/
```

This will process the original texts in the directory *o* and the translated texts in *t*, and save the output in the directory *myoutput*. One test text file is provided for *o* and *t*. You can then use the file *zh_pos_n_grams:0.arff* to run the classifier in (WEKA)[https://www.cs.waikato.ac.nz/ml/weka/]. 

Note: Test file for *o* is from [Xinhua](http://www.xinhuanet.com/politics/2018-11/05/c_1123665905.htm). Test file for *t* is from [Reference News](http://www.cankaoxiaoxi.com/china/20181103/2348120.shtml).

## Comprehensive documentation

See the original [documentation](https://translationese.readthedocs.org/) for more details. 

