import os
import subprocess

urls = [
    "https://xueba5.com/d/file/p/2021/08-19/0e7fccc3c4d3994764edc3ba9ecdd69a.jpg",
    "https://xueba5.com/d/file/p/2021/08-19/62624dd48567f42177fe0f863c2fc0a8.jpg",
    "https://xueba5.com/d/file/p/2021/08-19/886cccdcf5edce5a367c7bd2ec1819ec.jpg",
    "https://xueba5.com/d/file/p/2021/08-19/ecca81c7e9c464fc02b7aa6085115856.jpg",
    "https://xueba5.com/d/file/p/2021/08-19/52961d22028c6d5942dccc819e0a3904.jpg",
    "https://xueba5.com/d/file/p/2021/08-19/580da0a15a1b1df4203a6f0f31049788.jpg",
    "https://xueba5.com/d/file/p/2021/08-19/2a5a92e0c3c498e55d4bda7615a23897.jpg",
    "https://xueba5.com/d/file/p/2021/08-19/5f9107dfbcd05c2bb778e0c482d170cd.jpg",
    "https://xueba5.com/d/file/p/2021/08-19/786a2fdcc37f75cb347017ac7fb520ca.jpg",
    "https://xueba5.com/d/file/p/2021/08-19/a93448b497654e04101e72c4cb6be6f8.jpg"
]

output_dir = "images6x"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Headers and cookies from user request
headers = [
    "-H", 'Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    "-H", 'Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    "-H", 'Cache-Control: no-cache',
    "-H", 'Connection: keep-alive',
    "-b", 'say=ok11; Hm_lvt_d444c442dfb17b1de0915d44711524d5=1768100435; HMACCOUNT=BB20B0AD68926508; Hm_lvt_b292870d3634eae5dcee6516b429d328=1768100440; Hm_lpvt_d444c442dfb17b1de0915d44711524d5=1768371211; Hm_lpvt_b292870d3634eae5dcee6516b429d328=1768371217',
    "-H", 'Pragma: no-cache',
    "-H", 'Referer: https://xueba5.com/hujiaoban/yingyux6x_54sh/133764.html',
    "-H", 'Sec-Fetch-Dest: image',
    "-H", 'Sec-Fetch-Mode: no-cors',
    "-H", 'Sec-Fetch-Site: same-origin',
    "-H", 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    "-H", 'sec-ch-ua: "Chromium";v="143", "Not A(Brand";v="24"',
    "-H", 'sec-ch-ua-mobile: ?0',
    "-H", 'sec-ch-ua-platform: "Linux"'
]

for i, url in enumerate(urls):
    filename = f"page{i+1}.jpg"
    filepath = os.path.join(output_dir, filename)
    print(f"Downloading {filename}...")
    
    # Construct command
    cmd = ["curl", "-L", url] + headers + ["-o", filepath, "-s"]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Downloaded {filename}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download {filename}: {e}")
