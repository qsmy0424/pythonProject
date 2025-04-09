import requests
import json
import urllib3

urllib3.disable_warnings()

def fetch_and_parse_json(url, data):
    try:
        headers = {
            "Host": 'wenshu.court.gov.cn',
            "sec-ch-ua-platform": 'macOS',
            "Sec-Fetch-Site": 'same-origin',
            "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "Cookie": "wzws_sessionid=oGdzj/mANjEuNTIuMTMwLjEzMII2ZjY5MDGBMDg0NWIz; SESSION=a579a8fc-f1fd-4597-82b3-451f5c9860ab; wzws_cid=7e3596503d7731de9da8c572de64de92cb3e9785acb34be67d1ee6b42a979f62d099d500f839a7a22442202adc86e3a67fa542ff42b492348091cc95fcfcf41efc68725db278feb7bbebc81d5025a989",
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }
        response = requests.post(url, headers=headers, data=data, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"请求错误: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")
    return None

# 主函数
def main():
    # 629
    for i in range(1, 601):
        url = "https://wenshu.court.gov.cn/website/parse/rest.q4w"

        # 表单数据
        form_data = {
            "s8": "02",
            "pageId": "0.1441864187411237",
            "sortFields": "s50:desc",
            "ciphertext": "1110011 111001 1110111 1100001 1010001 1000100 1100111 1010100 110011 1000100 1010011 1011000 1100100 1101010 1111001 110001 1101000 1000110 1011000 110101 110101 110001 1110010 1001011 110010 110000 110010 110100 110001 110001 110011 110001 1001011 1100111 1010100 1110011 110011 1010011 110111 1100100 110010 1110110 110111 1111010 1010001 1100001 1010010 1000110 1010100 1000100 1011010 110111 1110100 1010001 111101 111101",
            "pageNum": 1,
            "queryCondition": '[{"key":"s8","value":"02"}]',
            "cfg": "com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@queryDoc",
            "__RequestVerificationToken": "Tg6pHQQNKSpE2T6cMs5lJr0E"
        }

        result = fetch_and_parse_json(url, form_data)

        print(result)


if __name__ == "__main__":
    main()
