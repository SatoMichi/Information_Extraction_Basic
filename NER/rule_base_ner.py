import re
from janome.tokenizer import Tokenizer

# rules : {boolean function(word):label}
# txt: str
def rule_base_ner(rules,txt):
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(txt)
    history = []
    for t in tokens:
        word = t.surface
        for rule,label in rules.items():
            if rule(word) and word not in history:
                tag1 = "<"+label+">"
                tag2 = "</"+label+">"
                txt = re.sub(word,tag1+word+tag2,txt)
                break
        history.append(word)
    return txt

if __name__ == "__main__":
    rules = { lambda x: x=="男":"People",
              lambda x: x=="蟋蟀":"Organism",
              lambda x: x[-1]=="門":"Location",
              lambda x: x[-2:]=="大路":"Location",
              lambda x: x=="一" or x=="二" or x=="三":"Number",}
    
    txt = """広い門の下には、この男のほかに誰もいない。ただ、所々丹塗の剥はげた、大きな円柱に、蟋蟀が一匹とまっている。
            羅生門が、朱雀大路にある以上は、この男のほかにも、雨やみをする市女笠や揉烏帽子が、
            もう二三人はありそうなものである。それが、この男のほかには誰もいない"""
    
    result = rule_base_ner(rules,txt)

    print(txt)
    print(result)