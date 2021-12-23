import os
path = "en2zh_datasets" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
list = []
zh_list = []
en_list = []
path_datasets = "en2zh_datasets"
# for file in files: #遍历文件夹
#      if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
#           with open(path+"/"+file,'r',encoding='UTF-8') as f:#打开文件
#               en_zh_data = f.readlines()
#
#               with open(path_datasets+"/"+".en",'w',encoding='UTF-8') as en_data:
#                   with open(path_datasets + "/"  + ".zh", 'w',encoding='UTF-8') as zh_data:
#                       for idx,item in enumerate(en_list):
#                           #如果是中文
#                           #print(item)
#                           if (len(item) > 10) and (len(item < 50)):
#                               en_data.writelines(item+"\n")
#                               zh_data.writelines(zh_list[idx]+"\n")

with open(path_datasets+"/"+'news-commentary-v13.zh-en.en','r',encoding='UTF-8') as en:#打开文件
    with open(path_datasets + "/" + ".en", 'w', encoding='UTF-8') as en_data:
        data = en.readlines()
        for (idx,item) in enumerate(data):
            if(len(item)< 100 and len(item)> 40):
                en_data.write(item)
                list.append(idx)


with open(path_datasets + "/" + 'news-commentary-v13.zh-en.zh', 'r', encoding='UTF-8') as zh:
    data_zh = zh.readlines()
    with open(path_datasets + "/"  + ".zh", 'w',encoding='UTF-8') as zh_data:
        for i in list:
            zh_data.write(data_zh[i])