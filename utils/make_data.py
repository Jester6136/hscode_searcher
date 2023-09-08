from utils import create_father_hscode,gather_father_mota,check_max_len
import pandas as pd
import json
raw = pd.read_csv('data/__2.csv')
data_raw = []
for index, row in raw.iterrows():
    tmp_ = {
        "hscode":row["hscode"],
        "mota":row["mota"],
        "mota_xin":"",
        "deep":""
    }
    data_raw.append(tmp_)

data = []
father_0 = []
father_1 = []
father_2 = []
father_3 = []
father_4 = []
father_5 = []
count = 0

for item in data_raw[::-1]:
    if item['mota'][:check_max_len(item["mota"],'- - - - -')] == "- - - - -":
        father_5.append({
            "_hscode":item['hscode'],
            "_fatherhscode":"",
            "mota":item['mota'].replace("- ",""),
            "mota_xin":item['mota'].lower().replace("- ",""),
            "deep":"5"
        }) 
    elif item['mota'][:check_max_len(item["mota"],'- - - -')] == "- - - -":
        if father_5 !=[]:
                father_5 = create_father_hscode(father_5,item['hscode'])
                father_4.extend(father_5)
                father_4.append({
                        "_hscode":item['hscode'],
                        "_fatherhscode":"",
                        "mota":item['mota'].replace("- ",""),
                        "mota_xin":gather_father_mota(item['mota'],father_5),
                        "deep":"4"
                        })
                father_5=[]
        else:
                father_4.append({
                        "_hscode":item['hscode'],
                        "_fatherhscode":"",
                        "mota":item['mota'].replace("- ",""),
                        "mota_xin":item['mota'].lower().replace("- ",""),
                        "deep":"4"
                        })
    elif item['mota'][:check_max_len(item["mota"],'- - -')] == "- - -":
        if father_4 !=[]:
                father_4 = create_father_hscode(father_4,item['hscode'])
                father_3.extend(father_4)
                father_3.append({
                        "_hscode":item['hscode'],
                        "_fatherhscode":"",
                        "mota":item['mota'].replace("- ",""),
                        "mota_xin":gather_father_mota(item['mota'].lower(),father_4),
                        "deep":"3"
                        })
                father_4=[]
        else:
                father_3.append({
                        "_hscode":item['hscode'],
                        "_fatherhscode":"",
                        "mota":item['mota'].replace("- ",""),
                        "mota_xin":item['mota'].lower().replace("- ",""),
                        "deep":"3"
                        })
    elif item['mota'][:check_max_len(item["mota"],'- -')] == "- -":
        if father_3 !=[]:
                father_3 = create_father_hscode(father_3,item['hscode'])
                father_2.extend(father_3)
                father_2.append({
                        "_hscode":item['hscode'],
                        "_fatherhscode":"",
                        "mota":item['mota'].replace("-",""),
                        "mota_xin":gather_father_mota(item['mota'].lower(),father_3),
                        "deep":"2"
                        })
                father_3=[]
        else:
                father_2.append({
                        "_hscode":item['hscode'],
                        "_fatherhscode":"",
                        "mota":item['mota'].replace("- ",""),
                        "mota_xin":item['mota'].lower().replace("- ",""),
                        "deep":"2"
                        })
    elif item['mota'][:check_max_len(item["mota"],'-')] == "-":
        if father_2 !=[]:
                father_2 = create_father_hscode(father_2,item['hscode'])
                father_1.extend(father_2)
                father_1.append({
                        "_hscode":item['hscode'],
                        "_fatherhscode":"",
                        "mota":item['mota'].replace("-",""),
                        "mota_xin":gather_father_mota(item['mota'].lower(),father_2),
                        "deep":"1"
                        })
                father_2=[]
        else:
                father_1.append({
                        "_hscode":item['hscode'],
                        "_fatherhscode":"",
                        "mota":item['mota'].replace("- ",""),
                        "mota_xin":item['mota'].lower().replace("- ",""),
                        "deep":"1"
                        })
    else:
        if "#" in item['hscode']:
                continue
        else:
                count+=1
                if father_1 !=[]:
                        father_1 = create_father_hscode(father_1,item['hscode'])
                        father_0.extend(father_1)
                        father_0.append({
                                "_hscode":item['hscode'],
                                "_fatherhscode":"FATHER"+str(count),
                                "mota":item['mota'].replace("-",""),
                                "mota_xin":gather_father_mota(item['mota'].lower(),father_1),
                                "deep":"0"
                                })
                        father_1=[]
                else:
                        father_0.append({
                                "_hscode":item['hscode'],
                                "_fatherhscode":"FATHER"+str(count),
                                "mota":item['mota'].replace("- ",""),
                                "mota_xin":item['mota'].lower().replace("- ",""),
                                "deep":"0"
                                })
data.extend(father_0)

with open('data/output3.jsonl', 'w') as outfile:
    for entry in data:
        json.dump(entry, outfile)
        outfile.write('\n')