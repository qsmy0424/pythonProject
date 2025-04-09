import requests
import json
import os


def fetch_and_parse_json(url, token, request_id):
    try:
        headers = {"token": token, "request-id": request_id}
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"请求错误: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")
    return None


def extract_image_paths(data):
    try:
        products = data["respData"]["products"]
        return [
            product["productImagePath"]
            for product in products
            if "productImagePath" in product
        ]
    except KeyError:
        print("JSON结构不符合预期")
        return []


def download_image(url, folder):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        filename = os.path.join(folder, url.split("/")[-1])
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"成功下载: {filename}")
    except Exception as e:
        print(f"下载图片 {url} 时发生错误: {e}")


# 主函数
def main():

    channel_ids = [708, 712, 711, 703, 709, 681, 710, 690, 665, 700, 672, 669, 684, 652]
    for channel_id in channel_ids:
        url = (
            "https://bat.fmswift.net/com/business/1/2/get-product-detail-info?mallId=1&channelId="
            + str(channel_id)
        )  # 替换为实际URL
        token = "NDFDNTcyMjk3Q0U1NEUyODlBQTZCNkY0MTVFRTA0OEUuMTc0MjgwMDIxNzUwOQ=="  # 替换为实际token
        request_id = "914654bd-84b8-4d68-9d0b-93f2e2753fca"  # 替换为唯一的request-id

        print(f"正在处理 {channel_id}")
        result = fetch_and_parse_json(url, token, request_id)

        if result:
            image_paths = extract_image_paths(result)
            if image_paths:
                download_folder = "downloaded_images"
                os.makedirs(download_folder, exist_ok=True)
                for path in image_paths:
                    download_image(path, download_folder)
            else:
                print("未找到图片路径")
        else:
            print("获取或解析数据失败")


if __name__ == "__main__":
    main()
