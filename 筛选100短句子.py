import os
path = "en2zh_datasets" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
list = []
zh_list = []
en_list = []
path_datasets = "en2zh_datasets"

with open(path_datasets+"/"+'train.en','r',encoding='UTF-8') as en:#打开文件
    with open(path_datasets + "/" + "1.en", 'w', encoding='UTF-8') as en_data:
        data = en.readlines()
        for (idx,item) in enumerate(data):
            if len(item)< 110 and len(item) > 30:
                en_data.write(item)
                list.append(idx)


with open(path_datasets + "/" + 'train.vi', 'r', encoding='UTF-8') as zh:
    data_zh = zh.readlines()
    with open(path_datasets + "/"  + "1.zh", 'w',encoding='UTF-8') as zh_data:
        for i in list:
            zh_data.write(data_zh[i])