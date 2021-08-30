# Information_Extraction_Basic
**Repository which contains various technologies about Information Extraction**

情報抽出に関する技術をまとめたレポジトリである。といったものの、最新の技術までカバーされているわけではない。どちらかといえば古典的なアルゴリズムによるところが大きいといえる。

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