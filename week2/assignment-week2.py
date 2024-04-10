# -*- coding: utf-8 -*-
# Created on 2024/4/10
# @author: mengju

print("===== 1 =====")

def find_and_print(messages, current_station):
    # your code here
    mrt_lst = ["Songshan", "Nanjing Sanmin", "Taipei Arena", "Nanjing Fuxing", "Songjiang Nanjing", "Zhongshan", "Beimen", "Ximen", "Xiaonanmen", "Chiang Kai-Shek Memorial Hall", "Guting", "Taipower Building", "Gongguan", "Wanlong", "Jingmei", "Dapinglin", "Qizhang", "Xindian City Hall", "Xindian"]
    
    # 处理message，生成每个人所在站点的字典location_dict，方便后续处理
    location_dict = {}
    for friend in messages.keys():
        flag = 0 # 标志：用于确认所在站点后break，以及小碧潭的情况
        for station in mrt_lst:
            if station in messages[friend]:
                location_dict[friend] = station
                flag = 1 # 确认站点
                break
        if flag == 0 and 'Xiaobitan' in messages[friend]: # 出现小碧潭的情况
            location_dict[friend] = 'Xiaobitan'

    # 特殊处理：如果current station在小碧潭
    if current_station == 'Xiaobitan':
        # 如果有人也在小碧潭，那就直接print并结束执行
        for friend in location_dict.keys():
            if location_dict[friend] == 'Xiaobitan':
                nearest = friend
                print(nearest)
                return 0
        # 如果没有人在小碧潭，那就相当于看谁离七张最近
        current_station = 'Qizhang'

    # 看谁离最近
    current_index = mrt_lst.index(current_station)
    smallest_distance = 30
    # 获取每个人的距离
    for friend in location_dict.keys():
        if location_dict[friend] == 'Xiaobitan': # 特殊处理：有人在小碧潭
            location_index = mrt_lst.index('Qizhang')
            distance = abs(location_index - current_index) + 1
        else:
            location_index = mrt_lst.index(location_dict[friend])
            distance = abs(location_index - current_index)
        # 判断距离最近
        if distance < smallest_distance: # 因为要求里没提，暂不考虑有两个以上最近距离的情况
            smallest_distance = distance
            nearest = friend
    print(nearest)
    return 0

messages={
    "Leslie":"I'm at home near Xiaobitan station.",
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

print("===== 2 =====")

# your code here, maybe
time = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] # 长度为24，代表24小时

def book(consultants, hour, duration, criteria):
    # your code here
    # 根据criteria排序列表
    if criteria == "price":
        sorted_cons = sorted(consultants, key=lambda x: x["price"])
    elif criteria == "rate":
        sorted_cons = sorted(consultants, key=lambda x: x["rate"], reverse=True)

    # 判断是否有空
    for i in range(len(consultants)):
        flag = 0 # 标志：用于判断时间冲突
        for j in range(duration):
            if sorted_cons[i]["name"] in time[hour + j]:
                flag = 1 # 标志：时间冲突
                break # 进入下一个外循环（看下一个consultant是否有时间冲突）
        if flag == 0:
            name = sorted_cons[i]["name"]
            break # 没有时间冲突，跳出循环
    if flag == 1: # 标志：所有人都有时间冲突
        print("No Service")
        return 0
    else:
        print(name)

    # 记录已预约时间
    for i in range(duration):
        time[hour + i].append(name)
    return 0

consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
]
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John

print("===== 3 =====")

def func(*data):
    # your code here
    # 建立一个字典，格式{'中间名':[全名的列表]}
    dic = {}
    for name in data:
        middle_name = name[int(len(name) / 2)]
        if middle_name not in dic:
            dic[middle_name] = [name]
        else:
            dic[middle_name].append(name)

    # 判断并输出全名
    for mid in dic.keys():
        if len(dic[mid]) == 1:
            print(dic[mid][0])
            return 0
    print("没有") # 如果到执行到这里还没结束，表示没有len = 1的全名列表
    return 0

func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安

print("===== 4 =====")

def get_number(index):
    # your code here
    def get_num(n):
        if n == 0:
            number = 0
            return number
        elif n % 3 == 0:
            number = get_num(n - 1) - 1
            return number
        else:
            number = get_num(n - 1) + 4
            return number
    print(get_num(index))
    return 0

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70

print("===== 5 =====")

def find(spaces, stat, n):
    # your code here
    flag = 0 # 标志：用于判断有没有可用的车厢
    smallest_diff = 100 # 差值：用于判断可用的车厢里哪个最合适
    for i in range(len(stat)):
        if stat[i] == 1:
            if spaces[i] >= n:
                flag = 1
                # 判断差值最小的可用车厢
                diff = spaces[i] - n
                if diff < smallest_diff: # 因为要求中没提，这里不使用<=，则如果出现两个以上最合适车厢，默认选择最前面的一个
                    fit = i
                    smallest_diff = diff
    if flag == 0: # 没有可用的车厢
        fit = -1
    print(fit)
    return 0

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2