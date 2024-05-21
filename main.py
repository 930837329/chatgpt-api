import sys
sys.path.append(r'd:\program files\workon_home\frida\lib\site-packages')

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




url = "https://api.binjie.fun/api/generateStream?refer__1360=eqRhiKBKD5GIvDBqDTCmKwK0IP7I%3DNUox"

payload = json.dumps({
  "prompt": "有关碳足迹的内容",
  "userId": "#/chat/1711468353364",
  "network": True,
  "system": "",
  "withoutContext": False,
  "stream": False
})

headers = {
  'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/json",
  'sec-ch-ua': "\"Microsoft Edge\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
  'sec-ch-ua-mobile': "?0",
  'sec-ch-ua-platform': "\"Windows\"",
  'origin': "https://chat18.aichatos.xyz",
  'sec-fetch-site': "cross-site",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://chat18.aichatos.xyz/",
  'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}

response = requests.post(url, data=payload, headers=headers,verify=False)
while True:
    if response.status_code != 200:
        print('请求失败:', response.status_code)
        break
    print('请求成功:',response.text.encode('latin1').decode('utf-8'))
    break

