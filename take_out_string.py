import re

with open("model_Weight.txt", "r", encoding='utf-8') as f:
    data = f.readlines()

new = open("QA_text.txt", "a", encoding="utf-8")

for i in data:
    number_result = re.findall(r'<b>(.*?)</b>', i)
    text_result = re.findall(r'<font color="#000000">(.*?) </font>', i)
    for j in number_result:
        new.write(j)
        new.write("\n")
    for k in text_result:
        new.write(k)
        new.write("\n")