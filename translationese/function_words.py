"""\
We aim to replicate the results of Koppel and Ordan (2011) with this feature.
We use the same list of function words (in fact, some of them are content
words, but they are all crucial for organizing the text) and implement the same
feature. Each function word in the corpus is a feature, whose value is the
normalized frequency of its occurrences in the chunk.
"""

FUNCTION_WORDS = ['a',
                  'about',
                  'above',
                  'according',
                  'accordingly',
                  'actual',
                  'actually',
                  'after',
                  'afterward',
                  'afterwards',
                  'again',
                  'against',
                  'ago',
                  'ah',
                  "ain't",
                  'all',
                  'almost',
                  'along',
                  'already',
                  'also',
                  'although',
                  'always',
                  'am',
                  'among',
                  'an',
                  'and',
                  'another',
                  'any',
                  'anybody',
                  'anyone',
                  'anything',
                  'anywhere',
                  'are',
                  "aren't",
                  'around',
                  'art',
                  'as',
                  'aside',
                  'at',
                  'away',
                  'ay',
                  'back',
                  'be',
                  'bear',
                  'because',
                  'been',
                  'before',
                  'being',
                  'below',
                  'beneath',
                  'beside',
                  'besides',
                  'better',
                  'between',
                  'beyond',
                  'bid',
                  'billion',
                  'billionth',
                  'both',
                  'bring',
                  'but',
                  'by',
                  'came',
                  'can',
                  "can't",
                  'cannot',
                  'canst',
                  'certain',
                  'certainly',
                  'come',
                  'comes',
                  'consequently',
                  'could',
                  "couldn't",
                  'couldst',
                  'dear',
                  'definite',
                  'definitely',
                  'despite',
                  'did',
                  "didn't",
                  'do',
                  'does',
                  "doesn't",
                  'doing',
                  "don't",
                  'done',
                  'dost',
                  'doth',
                  'doubtful',
                  'doubtfully',
                  'down',
                  'due',
                  'during',
                  'e.g.',
                  'each',
                  'earlier',
                  'early',
                  'eight',
                  'eighteen',
                  'eighteenth',
                  'eighth',
                  'eighthly',
                  'eightieth',
                  'eighty',
                  'either',
                  'eleven',
                  'eleventh',
                  'else',
                  'enough',
                  'enter',
                  'ere',
                  'erst',
                  'even',
                  'eventually',
                  'ever',
                  'every',
                  'everybody',
                  'everyone',
                  'everything',
                  'everywhere',
                  'example',
                  'except',
                  'exeunt',
                  'exit',
                  'fact',
                  'fair',
                  'far',
                  'farewell',
                  'few',
                  'fewer',
                  'fifteen',
                  'fifteenth',
                  'fifth',
                  'fifthly',
                  'fiftieth',
                  'fifty',
                  'finally',
                  'first',
                  'firstly',
                  'five',
                  'for',
                  'forever',
                  'forgo',
                  'forth',
                  'fortieth',
                  'forty',
                  'four',
                  'fourteen',
                  'fourteenth',
                  'fourth',
                  'fourthly',
                  'from',
                  'furthermore',
                  'generally',
                  'get',
                  'gets',
                  'getting',
                  'give',
                  'go',
                  'good',
                  'got',
                  'had',
                  'has',
                  "hasn't",
                  'hast',
                  'hath',
                  'have',
                  "haven't",
                  'having',
                  'he',
                  "he'd",
                  "he'll",
                  "he's",
                  'hence',
                  'her',
                  'here',
                  'hers',
                  'herself',
                  'him',
                  'himself',
                  'his',
                  'hither',
                  'ho',
                  'how',
                  "how's",
                  'however',
                  'hundred',
                  'hundredth',
                  'i',
                  "i'd",
                  "i'm",
                  "i've",
                  'if',
                  'in',
                  'indeed',
                  'instance',
                  'instead',
                  'into',
                  'is',
                  "isn't",
                  'it',
                  "it'd",
                  "it'll",
                  "it's",
                  'its',
                  'itself',
                  'last',
                  'lastly',
                  'later',
                  'less',
                  'let',
                  "let's",
                  'like',
                  'likely',
                  'many',
                  'matter',
                  'may',
                  'maybe',
                  'me',
                  'might',
                  'million',
                  'millionth',
                  'mine',
                  'more',
                  'moreover',
                  'most',
                  'much',
                  'must',
                  "mustn't",
                  'my',
                  'myself',
                  'nay',
                  'near',
                  'nearby',
                  'nearly',
                  'neither',
                  'never',
                  'nevertheless',
                  'next',
                  'nine',
                  'nineteen',
                  'nineteenth',
                  'ninetieth',
                  'ninety',
                  'ninth',
                  'ninthly',
                  'no',
                  'nobody',
                  'none',
                  'noone',
                  'nor',
                  'not',
                  'nothing',
                  'now',
                  'nowhere',
                  'o',
                  'occasionally',
                  'of',
                  'off',
                  'oft',
                  'often',
                  'oh',
                  'on',
                  'once',
                  'one',
                  'only',
                  'or',
                  'order',
                  'other',
                  'others',
                  'ought',
                  'our',
                  'ours',
                  'ourselves',
                  'out',
                  'over',
                  'perhaps',
                  'possible',
                  'possibly',
                  'presumable',
                  'presumably',
                  'previous',
                  'previously',
                  'prior',
                  'probably',
                  'quite',
                  'rare',
                  'rarely',
                  'rather',
                  'result',
                  'resulting',
                  'round',
                  'said',
                  'same',
                  'say',
                  'second',
                  'secondly',
                  'seldom',
                  'seven',
                  'seventeen',
                  'seventeenth',
                  'seventh',
                  'seventhly',
                  'seventieth',
                  'seventy',
                  'shall',
                  'shalt',
                  "shan't",
                  'she',
                  "she'd",
                  "she'll",
                  "she's",
                  'should',
                  "shouldn't",
                  'shouldst',
                  'similarly',
                  'since',
                  'six',
                  'sixteen',
                  'sixteenth',
                  'sixth',
                  'sixthly',
                  'sixtieth',
                  'sixty',
                  'so',
                  'soever',
                  'some',
                  'somebody',
                  'someone',
                  'something',
                  'sometimes',
                  'somewhere',
                  'soon',
                  'still',
                  'subsequently',
                  'such',
                  'sure',
                  'tell',
                  'ten',
                  'tenth',
                  'tenthly',
                  'than',
                  'that',
                  "that's",
                  'the',
                  'thee',
                  'their',
                  'theirs',
                  'them',
                  'themselves',
                  'then',
                  'thence',
                  'there',
                  "there's",
                  'therefore',
                  'these',
                  'they',
                  "they'd",
                  "they'll",
                  "they're",
                  "they've",
                  'thine',
                  'third',
                  'thirdly',
                  'thirteen',
                  'thirteenth',
                  'thirtieth',
                  'thirty',
                  'this',
                  'thither',
                  'those',
                  'thou',
                  'though',
                  'thousand',
                  'thousandth',
                  'three',
                  'thrice',
                  'through',
                  'thus',
                  'thy',
                  'till',
                  'tis',
                  'to',
                  'today',
                  'tomorrow',
                  'too',
                  'towards',
                  'twas',
                  'twelfth',
                  'twelve',
                  'twentieth',
                  'twenty',
                  'twice',
                  'twill',
                  'two',
                  'under',
                  'undergo',
                  'underneath',
                  'undoubtedly',
                  'unless',
                  'unlikely',
                  'until',
                  'unto',
                  'unusual',
                  'unusually',
                  'up',
                  'upon',
                  'us',
                  'very',
                  'was',
                  "wasn't",
                  'wast',
                  'way',
                  'we',
                  "we'd",
                  "we'll",
                  "we're",
                  "we've",
                  'welcome',
                  'well',
                  'were',
                  "weren't",
                  'what',
                  "what's",
                  'whatever',
                  'when',
                  'whence',
                  'where',
                  "where's",
                  'whereas',
                  'wherefore',
                  'whether',
                  'which',
                  'while',
                  'whiles',
                  'whither',
                  'who',
                  "who's",
                  'whoever',
                  'whom',
                  'whose',
                  'why',
                  'wil',
                  'will',
                  'wilst',
                  'wilt',
                  'with',
                  'within',
                  'without',
                  "won't",
                  'would',
                  "wouldn't",
                  'wouldst',
                  'ye',
                  'yes',
                  'yesterday',
                  'yet',
                  'you',
                  "you'd",
                  "you'll",
                  "you're",
                  "you've",
                  'your',
                  'yours',
                  'yourself',
                  'yourselves']
"""Koppel and Ordan's list of `Function Words`"""

FUNCTION_WORDS_ZH = [
    # AS:
    '了', '中', '过', '着',
    # BA:
    '将', '把',
    # CC:
    '或者', '或', '不但', '兼', '且', '而且', '及', '也', '也是', '等', '与', '比', '乃至', '而', '还是', '并且', '以及', '又', '并', '不仅', '和',
    '至', '但', '暨', '既', '到', '同', '加',
    # CS:
    '如', '虽然', '无论', '假如', '不论', '不管', '一旦', '只要', '因为', '虽', '只有', '如果', '尽管', '若', '即使', '由于',
    # DEC:
    '的', '之',
    # DEG:
    '的', '之',
    # DER:
    '得', '个',
    # DEV:
    '地',
    # DT:
    '那', '上', '此', '本', '整', '那些', '全体', '后', '该', '各', '其他', '全部', '某', '有些', '诸', '什么', '一切', '所有', '每',
    '何', '某些', '其余', '同', '其它', '这', '另', '前', '头', '这些', '全', '下', '历', '任何',
    # ETC:
    '等等', '等',
    # LB:
    '遭', '为', '被',
    # LC:
    '之中', '处', '来', '以下', '末', '上', '之内', '以外', '之间', '之前', '顶', '止', '之后', '旁', '前后', '底', '后', '以后', '以上',
    '内', '初', '侧', '外', '开始', '以来', '左右', '东', '口', '中', '在内', '的后', '之外', '时', '里', '边', '起', '间', '前', '为止', '畔',
    '之际', '以前', '以内', '下', '之初',
    # M:
    # '处', '式', '朵', '些', '例', '章', '块', '重', '平方米', '倍', '架', '立方米', '港元', '门', '顿', '年', '部分', '台', '名', '级',
    # '排排', '千伏', '员', '点', '户', '桶', '度', '马克', '类', '批', '起', '澳元', '头', '吨', '公顷', '天', '首', '尾', '周', '厘米',
    # '班', '位', '届', '秒', '瓦', '轮', '组', '罐', '项', '盘', '股', '篇', '封', '口', '日元', '摄氏度', '岁', '刻', '串', '根', '斑斑',
    # '笔', '宗', '个', '日', '颗', '站', '千瓦', '元', '锭', '界', '加元', '场', '米', '局', '目', '代', '套', '艘', '分钟', '张', '段', '公里',
    # '人份', '美元', '页', '支', '片', '只', '路', '座', '种', '系列', '辆', '对', '平方公里', '间', '枚', '所', '公斤', '株', '家', '条款', '角',
    # '桩', '分米', '幅', '层', '载', '个把', '分', '等', '人次', '亩', '期', '埃居', '次', '台套', '部', '番', '件', '幢', '里', '份', '平米', '号',
    # '步', '线', '伏', '条', '架次', '队', '本',
    # MSP:
    '来', '所', '而', '以', '去',
    # P:
    '截止', '较', '朝着', '似', '随', '像', '连同', '过', '据', '于', '自从', '通过', '傍', '当', '除', '除了', '由于', '本着', '自', '凭',
    '对于', '从', '受', '每当', '沿', '面向', '与', '给', '靠', '往', '比', '象', '应', '按', '以', '依照', '截至', '依', '向', '如', '隔',
    '继', '在', '由', '随着', '按照', '作为', '为了', '就', '因', '如同', '趁', '截止到', '隔着', '面对', '和', '用', '至', '除去', '对', '关于',
    '针对', '朝', '经过', '临', '因为', '截至到', '依据', '为', '鉴于', '沿着', '有关', '在于', '做为', '凭借', '经', '到', '同', '根据',
    # PN:
    '大家', '那', '到处', '多久', '自身', '双方', '它', '你', '这儿', '此', '那里', '这样', '他们', '她们', '相互', '您', '自己', '本人', '有些',
    '其', '彼此', '一切', '什么', '它们', '你们', '本身', '我们', '自我', '各自', '这里', '对方', '这', '一方', '谁', '他', '有的', '我', '她', '这些',
    '何时', '如此', '之',
    # SB:
    '受', '被',
    # SP:
    '了', '吧', '的话', '的', '吗', '呀', '呢',
    # VC:
    '非', '为', '是',
    # VE:
    '无', '有', '没', '没有',
]


def quantify(analysis):
    """Quantify function words"""
    freq = analysis.histogram_normalized()
    if analysis.lang == 'en':
        pairs = [(word, freq.get(word, 0.0)) for word in FUNCTION_WORDS]
    elif analysis.lang == 'zh':
        pairs = [(word, freq.get(word, 0.0)) for word in set(FUNCTION_WORDS_ZH)]
    else:
        print('language "{}" not implemented yet for function_words'.format(analysis.lang))
        exit()

    return dict(pairs)
