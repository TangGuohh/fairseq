
num = 0
def write():
    with open('en2zh_datasets/.en','r',encoding='UTF-8') as en:
        with open('en2zh_datasets/.zh', 'r', encoding='UTF-8') as zh:
            with open('en2zh_datasets/en2zh.en2', 'w', encoding='UTF-8') as en2:
                with open('en2zh_datasets/en2zh.zh2', 'w', encoding='UTF-8') as zh2:
                    data_zh = zh.readlines()
                    data_en = en.readlines()
                    for (idx,item) in enumerate(data_zh):
                        if  (('�' not in item) and (' ' not in item) and ('​' not in item)):
                            en2.write(data_en[idx])
                            zh2.write(data_zh[idx])
                        # if ('��') not in item:
                        #     en2.write(data_en[idx])
                        #     zh2.write(data_zh[idx])
def write2():
    with open('en2zh_datasets/en2zh.en2', 'r', encoding='UTF-8') as en2:
        with open('en2zh_datasets/en2zh.zh2', 'r', encoding='UTF-8') as zh2:
            with open('en2zh_datasets/en2zh.en3', 'w', encoding='UTF-8') as en3:
                with open('en2zh_datasets/en2zh.zh3', 'w', encoding='UTF-8') as zh3:
                    data_zh = zh2.readlines()
                    data_en = en2.readlines()
                    for (idx, item) in enumerate(data_zh):
                        if  ('�' not in item) and (' ' not in item) and ('​' not in item) and ('�' not in data_zh[idx]) and (' ' not in data_zh[idx]) and ('​' not in data_zh[idx]):
                            en3.write(data_en[idx])
                            zh3.write(data_zh[idx])

def tongji():
    num = 0
    with open('en2zh_datasets/en2zh.zh2', 'r', encoding='UTF-8') as zh2:
        data = zh2.readlines()
        for (idx, item) in enumerate(data):
            if  ('�'  in item) or (' '  in item) or ('​'  in item):
                num +=1

    print(num)
write()
tongji()
write2()
tongji()

