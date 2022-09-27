import random
from datetime import datetime

alp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
target_num = 10
defect_num= 2
max_num = 2

def shutudai():
    target_ls = random.sample(alp, target_num)
    defect_ls = random.sample(target_ls, defect_num)
    print("対象文字列：")
    for i in target_ls:
        print(i, end=" ")
    print("\n表示文字列：")
    for i in set(target_ls) ^ set(defect_ls):
        print(i, end=" ")
    return defect_ls

def kaitou(defect_ls):
    inp_num = int(input("\n欠損文字はいくつあるでしょうか？："))
    if inp_num != defect_num:
        print("不正解です。", end="")
        return False
    else:
        print("正解です。それでは、具体的に欠損文字列を１つずつ入力してください")
        for i in range(defect_num):
            inp_str = input(f"{i + 1}つ目の文字を入力してください：")
            if inp_str in defect_ls:
                defect_ls.remove(inp_str)
                if len(defect_ls) == 0:
                    print("欠損文字も含めて完全正解です！！！")
                    return True
                    
            
        
def main():
    defect_ls = shutudai()
    #print(defect_ls)
    st = datetime.now()
    for i in range(max_num):    
        result = kaitou(defect_ls)
        if result:
            ed = datetime.now()
            print(f"タイムは{(ed-st).seconds}秒です")
            break
        else:
            if i == max_num - 1:
                print("またチャレンジしてください")

main()
