import random
import numpy as np

# one-versus-rest method for multi label classification
# perceptron for one label
def train_model(data,epoch=100):
    w = np.zeros(len(data[0][-1]))
    for i in range(epoch):
        index = random.randint(0,len(data)-1)
        (y,x) = data[index]
        if y*np.dot(x,w) <= 0: w += y*x
    return lambda x: np.dot(x,w)

# if C[i,j] = 1, then label i can be followed by label j
                                #       # B_PER # I_PER # B_ORG # I_ORG # O # EOS
C = np.array([[1,0,1,0,1,1],    # BOS   #   1   #  0    #  1    #   0   # 1 #  1
              [1,0,1,0,1,1],    # O     #       #       #       #       #   #
              [1,1,1,0,1,1],    # B_PER #       #       #       #       #   #
              [1,1,1,0,1,1],    # I_PER #       #       #       #       #   #
              [1,0,1,1,1,1],    # B_ORG #       #       #       #       #   #
              [1,0,1,1,1,1]])   # I_ORG #       #       #       #       #   #

# viterbi algorithm
def viterbi(xs,ys,models,C):
    score = np.zeros((len(xs),len(ys)))
    pre = np.zeros((len(xs),len(ys)))
    sofmaxs = [lambda x : np.exp(model(x))/sum([np.exp(model(x)) for model in models]) for model in models]
    x = xs[0]
    for y in ys:
        score[0,y] = sofmaxs[y](x)*C[0,y]                                           # f(x)*C["BOS",label y]
    for i in range(1,len(xs)):
        x = xs[i]
        for y in ys:
            pre[i,y] = np.argmax([score[i-1,l]*sofmaxs[y](x)*C[l,y] for l in ys])   # find most probable previous label
            score[i,y] = score[i-1,pre[i,y]]*sofmaxs[y](x)*C[pre[i,y],y]            # calculate score according to previous label
    ne_label = [""]*len(xs)
    ns_label[-1] = np.argmax([score[len(xs),l]*C[l,-1] for l in ys])
    for i in range(len(xs)-1,1,-1):
        ne_label[i-1] = pre[i,ne_label[i]]
    return ne_label