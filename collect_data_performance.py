"""Collecting performance data from specific link"""
import json

from selenium import webdriver

tempdict = {}
temparr = []
durarr = []
durarr2 = []

for i in range(10):
    driver = webdriver.Chrome()
    driver.get("https://en.wikipedia.org/wiki/Software_metric")
    performance_data = driver.execute_script("return window.performance.getEntries();")
    temparr.append(performance_data)
    driver.close()
for i in range(len(temparr)):
    for j in range(len(temparr)):
        durarr.append(temparr[i][j]['duration'])
    durarr2.append(durarr)
    durarr = []

for i in range(len(temparr)):
    tempdict[temparr[i][i]['name']] = durarr2[i]

with open("sample.json", "w", encoding='utf-8') as outfile:
    json.dump(tempdict, outfile)
    outfile.close()



with open("res.csv", 'w', encoding='utf-8') as f:
    f.write("Name, Duration \n")
    for key, value in tempdict.items():
        f.write(f"{key}, {sum(value) / len(value)}\n")
    f.close()
