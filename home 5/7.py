#file_ = open("text_7.txt", "x")
import json
dict_ = []
with open("my_file.json", "w") as w_f:
    with open("text_7.txt", encoding="utf-8") as f:
        dict2 = {}
        for i in f:
            dict2[i.split(' ')[0]] = int(i.split(' ')[2]) - int(i.split(' ')[3])
        cash = sum([int(i) for i in dict2.values() if int(i) > 0]) / len([int(i) for i in dict2.values() if int(i) > 0])
        dict_.append(dict2)
        dict_.append({"average_profit": round(cash)})
    json.dump(dict_, w_f)