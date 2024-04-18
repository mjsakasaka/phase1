import urllib.request as request
import json

src1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

# 获取url data
with request.urlopen(src1) as response:
    spot_data = json.load(response)
with request.urlopen(src2) as response:
    mrt_data = json.load(response)

# 格式：SpotTitle,District,Longitude,Latitude,ImageURL
# District需要获取serial_no到mrt_data里通过address获取；ImageURL需要处理格式；其他的可以直接从spot_data获取
spot_lst = spot_data["data"]["results"]
mrt_lst = mrt_data["data"]
distr_lst = ['中正區', '萬華區', '中山區', '大同區', '大安區', '松山區', '信義區', '士林區', '文山區', '北投區', '內湖區', '南港區']
spot_mrt_dic = {} # 建立{捷運站: [景點列表]}字典，用於要求二
with open("spot.csv", "w", encoding="utf-8") as file:
    for spot in spot_lst:
        # 获取district
        serial_no = spot["SERIAL_NO"]
        ## 用serial_no找到站名
        check_mrt = 0 # 用于确认是否找到捷运站
        for mrt in mrt_lst:
            if mrt["SERIAL_NO"] == serial_no:
                check_mrt = 1 # 确认找到站名
                
                ### 这里的处理是用于要求二的
                station = mrt["MRT"]
                if station not in spot_mrt_dic:
                    spot_mrt_dic[station] = [spot["stitle"]]
                else:
                    spot_mrt_dic[station].append(spot["stitle"])

                addr = mrt["address"]
                # 得到站名后，从address信息中找到地区
                check_distr = 0 # 用于确认是否找到地区
                for distr in distr_lst:
                    if distr in addr:
                        check_distr = 1
                        district = distr # 获得district
                        break
                    elif check_distr == 0:
                        district = "No Address Info"
                break
            elif check_mrt == 0: # 没找到站名的情况，方便后续处理
                district = "No MRT Info"
        # 获取image_url
        image_urls = spot["filelist"].lower()
        image_url = image_urls.split("jpg")[0] + "jpg"
        image_url = image_url.replace("\\", "")
        # 写入spot.csv
        line_lst = [spot["stitle"], district, spot["longitude"], spot["latitude"], image_url]
        file.write(','.join(line_lst) + '\n')

with open("mrt.csv", "w", encoding="utf-8") as f:
    for key in spot_mrt_dic:
        spots_lst = [key]
        for spot_name in spot_mrt_dic[key]:
            spots_lst.append(spot_name)
        f.write(','.join(spots_lst) + '\n')
