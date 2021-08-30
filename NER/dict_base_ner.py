import re

# dict : {word:label}
# txt: str
def dict_base_ner(dictionary,txt):
    for k,v in dictionary.items():
        tag1 = "<"+v+">"
        tag2 = "</"+v+">"
        txt = re.sub(k,tag1+k+tag2,txt)
    return txt

if __name__ == "__main__":
    dictionary = { "男":"People",
                   "蟋蟀":"Organism",
                   "羅生門":"Location",
                   "朱雀大路":"Location",
                   "一":"Number",
                   "二":"Number",
                   "三":"Number",}
    
    txt = """広い門の下には、この男のほかに誰もいない。ただ、所々丹塗の剥はげた、大きな円柱に、蟋蟀が一匹とまっている。
            羅生門が、朱雀大路にある以上は、この男のほかにも、雨やみをする市女笠や揉烏帽子が、
            もう二三人はありそうなものである。それが、この男のほかには誰もいない"""
    
    result = dict_base_ner(dictionary,txt)

    print(txt)
    print(result)