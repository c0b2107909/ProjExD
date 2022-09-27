import random

QaA = {"サザエの旦那の名前は？":["マスオ", "ますお"],
             "カツオの妹の名前は？":["ワカメ", "わかめ"],
             "タラオはカツオから見てどんな関係？":["甥", "おい", "甥っ子", "おいっこ"]}


def shutudai():
    q, a = random.choice(list(QaA.items()))
    print(q)
    return a
    
def kaito(ls):
    inp = input("答えるんだ：")
    if inp in ls:
        print("正解！！！")
    else:
        print("出直してこい")
        
for _ in range(3):
    ls = shutudai()
    kaito(ls)
