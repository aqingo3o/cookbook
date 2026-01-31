import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel

'''# 自製嵌入函式
從分割自然語言到嵌入到池化到正規化都能做喔
theItem (str) :
    要轉成 embedding 的東西, 應該是一個詞或是一個句子 (NL)
need_normalize (bool) :
    輸出的 sentence embedding 要不要正規化, 
    預設是要
LMName (str) :
    語言處理的模型, 
    預設是 'sentence-transformers/all-MiniLM-L6-v2'
'''

def qingsEmbedder(theItem, need_normalize=True, LMName='sentence-transformers/all-MiniLM-L6-v2',):
    tokenizer = AutoTokenizer.from_pretrained(LMName)
    ebModel = AutoModel.from_pretrained(LMName)

    torch.set_grad_enabled(False)
    inp = tokenizer(theItem, return_tensors="pt")
    out = ebModel(**inp)
    token_emb = out.last_hidden_state
    atMaskP1d = inp['attention_mask'].unsqueeze(-1).expand(token_emb.shape).float()
    sentenceEmbedding = torch.sum(token_emb * atMaskP1d, dim=1) / torch.clamp(atMaskP1d.sum(dim=1), min=1e-9)
    if need_normalize == True:
        sentenceEmbedding = torch.nn.functional.normalize(sentenceEmbedding, p=2, dim=1)
    elif need_normalize == False:
        pass
    else :
        print("'need_normalize' should be a boolean value.")
    torch.set_grad_enabled(True)
    return sentenceEmbedding