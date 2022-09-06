# 需求：从一堆手机号码中，找出两两相似的手机号码
#      相似的定义：两两手机号码同一位置的数字相同的数量

import pandas as pd
import os

# 计算两个号码的相似数量
def getPhoneSimilar(telphone1, telphone2):
    # 相似值变量初始化
    similar = 0
    # 手机号码，数字转字符串
    telphone1 = str(telphone1)
    telphone2 = str(telphone2)
    # print("%s---%s",(telphone1, telphone2))
    # print("%s---%s",(isinstance(str(telphone1), str), isinstance(str(telphone2), str)))
    
    # 判断两手机号码是否都为11位数
    if len(telphone1)==11 and len(telphone2)==11:
        pass
    else:
        return similar
    
    # 遍历手机号码的位数
    for i in range(11):
        # 判断两个手机号码第i位的数字是否一样，如果一样，相似度加1
        if telphone1[i]==telphone2[i]:
            similar += 1
    return similar

# 获取需要判断的手机号码
data_path = os.path.join(os.path.dirname(__file__),"找出相似的手机号码.csv")
# print(data_path)
data_df = pd.read_csv(data_path)
# print(data_df.head())

# 相似度字典变量，存储结果
similar_dict = {}
i = 1
for main_tel in data_df['telephone']:
    t_dict = {}
    print("计算相似度第%s次" % i)
    for sup_tel in data_df['telephone']:
        similar = getPhoneSimilar(main_tel, sup_tel)
        # print(similar)
        # 设置输出相似数量
        if similar > 5:
            t_dict[sup_tel] = similar
        else:
            pass
        # print(t_dict)
    similar_dict[main_tel] = t_dict
    # print(similar_dict)
    i += 1

# print(similar_dict)
# 输出结果到csv文件
export_file = os.path.join(os.path.dirname(__file__),'result.csv')
# 方式一：矩阵
# pd.DataFrame(similar_dict).to_csv(export_file)

# 方式二：维表
i = 1
res_df = pd.DataFrame(columns=['main_tel', 'sup_tel', 'similar'])
for main_tel, t_dict in similar_dict.items():
    # print(main_tel, t_dict)
    print("输出结果第%s次" % i)
    for key, value in t_dict.items():
        # print(main_tel, key, value)
        dim_dict = {'main_tel':main_tel, 'sup_tel':key, 'similar':value}
        dim_df = pd.DataFrame.from_dict(dim_dict, orient= 'index').T
        res_df = pd.concat([res_df, dim_df], axis=0)
        # print(res_df.head())
    i += 1
res_df.to_csv(export_file)