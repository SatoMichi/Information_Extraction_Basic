# Information_Extraction_Basic
**Repository which contains various technologies about Information Extraction**

情報抽出に関する技術をまとめたレポジトリである。といったものの、最新の技術までカバーされているわけではない。どちらかといえば古典的なアルゴリズムによるところが大きいといえる。

# Requirements
 - *janome* for Japanese language processing

# Corpus  
Basically this Information Extraction(IE) algorithm is assuming corpus or text of Japanese.
Corpus is constructed by the tool "doccano"(http://doccano.herokuapp.com/).

# Named-entity recognition(NER)

## Dictionary based NER (dict_base_ner.py)  
All the word needed to be recognized by NER is contained in the dictionary. The key of the dictionary is the word. And the value of the dictionary is the label. Extraction is storongly based on regular expression.
```
dictionary = {  "男":"People",
                "蟋蟀":"Organism",
                "羅生門":"Location",
                "朱雀大路":"Location",
                "一":"Number",
                "二":"Number",
                "三":"Number",}
```
```
広い門の下には、この男のほかに誰もいない。ただ、所々丹塗の剥はげた、大きな円柱に、蟋蟀が一匹とまっている。
羅生門が、朱雀大路にある以上は、この男のほかにも、雨やみをする市女笠や揉烏帽子が、
もう二三人はありそうなものである。それが、この男のほかには誰もいない

広い門の下には、この<People>男</People>のほかに誰もいない。ただ、所々丹塗の剥はげた、大きな円柱に、<Organism>蟋蟀</Organism>が<Number>一</Number>匹とまっている。<Location>羅生門</Location>が、<Location>朱雀大路</Location>にある以上は、この<People>男</People>のほかにも、雨やみをする市女笠や揉烏帽子が、
もう<Number>二</Number><Number>三</Number>人はありそうなものである。それが、この<People>男</People>のほかには誰もいない
```

## Rule based NER(rule_base_ner.py)  
All the word needed to be recognezed should match the rules given by user. First, text will be tokenized to list of word. To all of the words obtained, rules will be applied from head to tail, and if it matched, the word will be labeled as the value of the rule. This will depend on the accuracy of tokenization, and well formed rule with correct order.
```
rules = {   lambda x: x=="男":"People",
            lambda x: x=="蟋蟀":"Organism",
            lambda x: x[-1]=="門":"Location",
            lambda x: x[-2:]=="大路":"Location",
            lambda x: x=="一" or x=="二" or x=="三":"Number",}
```
```
広い門の下には、この男のほかに誰もいない。ただ、所々丹塗の剥はげた、大きな円柱に、蟋蟀が一匹とまっている。
羅生門が、朱雀大路にある以上は、この男のほかにも、雨やみをする市女笠や揉烏帽子が、
もう二三人はありそうなものである。それが、この男のほかには誰もいない

広い<Location>門</Location>の下には、この<People>男</People>のほかに誰もいない。ただ、所々丹塗の剥はげた、大きな円柱に、<Organism>蟋蟀</Organism>が<Number>一</Number>匹とまっている。
羅生<Location>門</Location>が、朱雀<Location>大路</Location>にある以上は、この<People>男</People>のほかにも、雨やみをする市女笠や揉烏帽子が、
もう<Number>二</Number><Number>三</Number>人はありそうなものである。それが、この<People>男</People>のほかには誰もいない
```

## Machine learning based NER(ml_base_ner.py)  
NER task is recognized as labeling(classification) problem for each word.
For example,
```
Raw text:
"羅生門が、朱雀大路にある以上は、この男のほかにも、雨やみをする市女笠や揉烏帽子が、もう二三人はありそうなものである。それが、この男のほかには誰もいない"

Labeled text:
"<B-LOC>羅生</B-LOC><I-LOC>門</I-LOC>が、<B-LOC>朱雀</B-LOC><I-LOC>大路</I-LOC>にある以上は、この<B-PER>男</b_PER>のほかにも、雨やみをする市女笠や揉烏帽子が、もう<B-NUM>二</B-NUM><B-NUM>三</B-NUM>人はありそうなものである。それが、この<B-PER>男</B-PER>のほかには誰もいない"
# this is using IOB2 representation

Tokens:
['羅生門', 'が', '、', '朱雀', '大路', 'に', 'ある', '以上', 'は', '、', 'この', '男', 'の', 'ほか', 'に', 'も', '、', '雨', 'やみ', 'を', 'する', '市', '女', '笠', 'や', '揉烏帽', '子', 'が', '、', 'もう', '二', '三', '人', 'は', 'あり', 'そう', 'な', 'もの', 'で', 'ある', '。', 'それ', 'が', '、', 'この', '男', 'の', 'ほか', 'に', 'は', '誰
', 'も', 'い', 'ない']

POS tags:
['名詞', '助詞', '記号', '名詞', '名詞', '助詞', '動詞', '名詞', '助詞', '記号', '連体詞', '名詞', '助詞', '名詞', '助詞', '助詞', '記号', '名詞', '名詞', '助詞', '動詞', '名詞', '名詞', '名詞', '助詞', '名詞', '名詞', '助詞', '記号', '副詞', '名詞', '名詞', '名詞', '助詞', '動詞', '名詞', '助動詞', '名詞', '助動詞', '助動詞', '記号', '名詞', '助詞', '記号', '連体詞', '名詞', '助詞', '名詞', '助詞', '助詞', '名詞', '助詞', '動詞', '助動詞']
```
then we can represent a word with its features and context's features.
```
word: x[i] = '大路'
context(win_size=1): [x[i-1],x[i+1]] = ['朱雀', 'に']
features: [x[i],x[i].POS,x[i-1],x[i-1].POS,x[i+1],x[i+1].POS] = ['大路','名詞','朱雀','名詞','に','助詞']
correct label: I_LOC
```
Features should be represented as vector for training model (one-hot vector could be one of the option).
So, model's input will be feature of the word(vector), output will be label of the word.  
NER process will be
 1. tokenize text into [words]
 2. convert each words into feature vector **v**
 3. label the word with output of the model which input is **v**
 4. extract word with relevant lables

Method used in the training model is called "one-versus-rest", which train binary classifier for each label.
For exapmle, if there is 3 labels, the train three binary classifer (perceptron).  
In addition, to remove non-resonable sequence of labels, Viterbi algorithm can be used.  
For example, these are non-reasonable labels sequence.
 - O -> I_PER
 - I_ORG -> I_PER

## Linear Structured Learning based NER()  
