import requests
import json
import pandas as pd

requests.packages.urllib3.disable_warnings()

data = pd.read_excel(r'/Users/qsmy/Downloads/result_minshi.xlsx', 'Sheet1', skiprows=352)

def fetch_and_parse_json(url, data):
    try:
        headers = {
            "Host": 'wenshu.court.gov.cn',
            "sec-ch-ua-platform": 'macOS',
            "Sec-Fetch-Site": 'same-origin',
            "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "Cookie": "wzws_sessionid=gDIyMS4xNS4yMTcuMjI2gjZmNjkwMYFhNDU1ZWKgZ3X/vw==; SESSION=d7349969-32ee-4f6b-b39d-7673fb2c58b5; wzws_cid=bd2409d542768350f4e2c4127e9f571ade1715a9767f677d692e00ba473b516b7761ab4d9a8e3f54e148865b21a9607eed0f964481ea620adda5c50b63c64cc26e5e0bb89ceb904ec659101d0d96b2d5",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "sec-ch-ua-mobile": "?0",
            "Origin": "https://wenshu.court.gov.cn",
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
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
    url = "https://wenshu.court.gov.cn/website/parse/rest.q4w"
    write_df = pd.DataFrame(columns=['success', 'code', 'secretKey', 'description', 'result'])
    for key in data.iloc[:, 5]:
    # for key in data['rowkey']:
        form_data = {
            "docId": key,
            "ciphertext": "1101001+1111010+1001111+1010111+1110100+1111000+110111+1111000+110011+1000010+1000111+1110000+1010011+1001111+1001011+1101110+1100010+110001+1001111+1001100+1111001+1111000+1101110+1000110+110010+110000+110010+110101+110000+110001+110000+110010+1010000+1110111+1010101+1101001+1110101+1110110+1010001+1111001+110110+1110011+1101010+1000011+1110000+1010000+1110101+1010100+110010+101111+1101011+1111001+1100001+1100111+111101+111101",
            "cfg": "com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@docInfoSearch",
            "__RequestVerificationToken": "Tnf1NA8I0SAtULOygOHKUHxc",
            "wh": "878",
            "ww": "1879",
            "cs": "0"
        }
        print(key)
        result = fetch_and_parse_json(url, form_data)
        print(result)
        if "权限" in result["result"]:
            return
        rows = [[
            result["success"],
            result["code"],
            result["secretKey"],
            result["description"],
            result["result"]
        ]]
        write_df = pd.concat([write_df, pd.DataFrame(rows, columns=write_df.columns)], ignore_index=True)
        write_df.to_excel("/Users/qsmy/Downloads/result_single1.xlsx", index=False)


if __name__ == "__main__":
    main()
