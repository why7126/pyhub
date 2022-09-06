import pandas as pd

project_dict = {
    "瑞士士卓曼Straumann仿生型BLT种植体":{"brand": "士卓曼", "type": "仿生型BLT"},
    "美国皓圣HIOSSEN ET III 种植体":{"brand": "皓圣", "type":"ET III"},
    "Dentium（韩国）种植体":{"brand":"登腾","type":"登腾"},
    "瑞士士卓曼Straumann 瑞锆型种植体":{"brand":"士卓曼", "type":"瑞锆"},
    "法国安卓健 Anthogyr PX种植体":{"brand":"安卓健", "type":"PX"},
    "百康特Bioconcept BV 种植体":{"brand":"百康特", "type":"BV"},
    "法国安卓健 Anthogyr REG种植体":{"brand":"安卓健", "type":"REG"},
    "瑞士士卓曼Straumann 悦锆型种植体":{"brand":"士卓曼", "type":"悦锆"},
    "瑞典Nobel PMC 种植体":{"brand":"Nobel", "type":"PMC"},
    "瑞典Nobel CC 种植体":{"brand":"Nobel", "type":"CC"},
    "瑞典Nobel Active 种植体":{"brand":"Nobel", "type":"Active"},
    "韩国OST奥齿泰种植体":{"brand":"奥齿泰", "type":"奥齿泰"},
    "美国百康 Bicon-种植体":{"brand":"百康", "type":"百康"},
    "瑞典Nobel PCC 种植体":{"brand":"Nobel", "type":"PCC"},
    "以色列AB种植体（T）":{"brand":"以色列AB", "type":"无"},
    "美国Damon Q金属矫治器":{"brand":"Damon","type":"金属自锁"},
    "进口隐适美隐形无托槽矫治器":{"brand":"隐适美","type":"标准型"},
    "时代天使隐形无托槽矫治器":{"brand":"时代天使","type":"单膜"},
    "美国Damon Q2金属自锁矫治器":{"brand":"Damon","type":"Q2"},
    "普特金属矫治器":{"brand":"普特","type":"金属自锁"},
    "时代天使冠军版隐形无托槽矫治器":{"brand":"时代天使","type":"冠军版"},
    "进口隐适美FIRST矫治器":{"brand":"隐适美","type":"First"},
    "eBrace专利数字个性化舌侧矫治器":{"brand":"eBrace","type":"舌侧"},
    "美国Damon Clear陶瓷矫治器":{"brand":"Damon","type":"陶瓷自锁"},
    "进口Insignia数字化定制金属矫治器":{"brand":"Insignia","type":"金属自锁"},
    "SPARK精准根控隐形无托槽矫治器":{"brand":"SPARK","type":"SPARK"},
    "日本进口tomy陶瓷自锁矫治器":{"brand":"Tomy","type":"陶瓷自锁"},
    "日本进口tomy金属自锁矫治器":{"brand":"Tomy","type":"金属自锁"},
    "eBrace专利数字个性化舌侧自锁矫治器":{"brand":"eBrace","type":"舌侧"},
    "COMFOS隐形无托槽矫治器":{"brand":"时代天使","type":"comfos"},
    "进口罗慕咬合诱导矫治器":{"brand":"罗慕","type":"无"},
    "新亚金属矫治器":{"brand":"新亚","type":"金属自锁"}
}
def GetBrand(context):
    if context in project_dict:
        return project_dict[context]["brand"]
    return "None"

def GetType(context):
    if context in project_dict:
        return project_dict[context]["type"]
    return "None"

xls_files = ["/Users/why/Downloads/客户成交项目明细表-天河1.xls"
    ,"/Users/why/Downloads/客户成交项目明细表-荔湾1.xls"
    ,"/Users/why/Downloads/客户成交项目明细表-中大1.xls"
    ,"/Users/why/Downloads/客户成交项目明细表-宝岗1.xls"
    ,"/Users/why/Downloads/客户成交项目明细表-梅花园1.xls"
    ,"/Users/why/Downloads/客户成交项目明细表-黄埔1.xls"
    ,"/Users/why/Downloads/客户成交项目明细表-越秀1.xls"
    ,"/Users/why/Downloads/客户成交项目明细表-中山八1.xls"
    ,"/Users/why/Downloads/客户成交项目明细表-东圃1.xls"
]
df_array = []
is_first = 0
for t_file in xls_files:
    if is_first == 0:
        df  = pd.read_excel(t_file, sheet_name=0)
    else:
        df = pd.read_excel(t_file, sheet_name=0, header=None)
    df_array.append(df)
data_df = pd.concat(df_array)

data_df['品牌'] = data_df["成交项目"].apply(lambda x: GetBrand(x))
data_df['型号'] = data_df["成交项目"].apply(lambda x: GetType(x))
data_df['成交日'] = data_df["成交日期"].apply(lambda x: x[0:10])
# print(data_df)
data_df.to_csv("/Users/why/Downloads/汇总明细表.csv")

# 成交项目包含种植体
filter_df = data_df[data_df["成交项目"].str.contains("种植体")]
# print(filter_df)
filter_df.to_csv("/Users/why/Downloads/种植体明细.csv")

# 统计
stati_df = filter_df.groupby(["品牌","型号", "成交日"]).agg({"购买次数": [sum]}).reset_index()
print(stati_df)

stati_df.to_csv("/Users/why/Downloads/种植体.csv")


# 成交项目包含种植体
filter_df = data_df[data_df["成交项目"].str.contains("矫治器")]
filter_df['品牌'] = filter_df["成交项目"].apply(lambda x: GetBrand(x))
filter_df['型号'] = filter_df["成交项目"].apply(lambda x: GetType(x))
filter_df['成交日'] = filter_df["成交日期"].apply(lambda x: x[0:10])
# print(filter_df)

filter_df.to_csv("/Users/why/Downloads/矫治器明细.csv")

# 统计
stati_df = filter_df.groupby(["品牌","型号", "成交日"]).agg({"购买次数": [sum]}).reset_index()
print(stati_df)

stati_df.to_csv("/Users/why/Downloads/矫治器.csv")