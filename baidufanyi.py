import requests

url = "https://fanyi.baidu.com/sug"
word = input("请输入你要翻译的英文单词: ")
dat = {"kw": word}

res = requests.post(url, data=dat)
result = res.json()

if result['errno'] == 0:
    print("翻译结果:")
    for item in result['data']:
        print(f"{item['k']}: {item['v']}")
else:
    print("请求失败，请重试")
