# 沪教版英语单词表网页生成流程 (Vocabulary List Generation Workflow)

本文档总结了为沪教版（牛津上海版）英语教材生成单词表网页的标准流程。

## 1. 获取图片源 (Source Acquisition)

1. **访问源网站**: 前往 [xueba5.com](https://xueba5.com) 并搜索目标年级教材（例如 "沪教版英语四年级上册"）。
2. **定位单词表**: 找到包含 "Word List (单词表)" 的页面。
3. **提取图片链接**:
   - 检查页面源码或使用开发者工具找到 `alt="Word List(单词表)"` 的图片 URLs。
   - 注意分页：通常单词表分布在 3-5 个页面中（如 `_2.html`, `_3.html` 等）。
   - 收集所有页面的图片地址。

## 2. 下载高清图片 (Image Downloading)

由于源网站有防盗链机制，不能直接右键保存或简单下载。必须使用带 Headers 的 `curl` 命令。

**关键 Headers**:
- `Referer`: 必须设置为当前页面的 URL。
- `User-Agent`: 模拟真实浏览器。

**参考命令模式**:
```bash
mkdir -p images4s  # 创建对应年级的目录 (如 images4s 代表 4年级上册 semester)

curl 'https://image-url.jpg' \
  -H 'Referer: https://source-page-url.html' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
  -H 'Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
  -H 'Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Pragma: no-cache' \
  -H 'Sec-Fetch-Dest: image' \
  -H 'Sec-Fetch-Mode: no-cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'sec-ch-ua: "Chromium";v="143", "Not A(Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -b 'say=ok11; Hm_lvt_...=...; HMACCOUNT=...; Hm_lpvt_...=...' \
  -o images4s/page1.jpg
```
*Note: You may need to copy the full `curl` command (including headers and cookies) from your browser's "Copy as curl" feature in the Network tab to bypass strict anti-bot protection.*
*对每一页重复此步骤，确保下载后的文件大小正常（通常 90KB+），而非几百字节的错误文件。*

## 3. 提取词汇数据 (Data Extraction)

查看下载的高清图片，手工录入或提取以下信息到 Python 脚本的数据结构中：

- **Word (单词)**: 英文原词。
- **POS (词性)**: 如 n., v., adj. 等。
- **Unit (单元)**: 右侧标注的模块单元 (如 M1U1)。
- **Phonetic (音标)**: 图片中若包含则直接录入；若不包含（如四年级教材），需手动补充 IPA 国际音标。
- **Meaning (中文)**: 对应的中文释义。

*注意：最后一页通常包含 **Daily Expressions (日常用语)**，需单独提取。*

## 4. 自动化生成 (HTML Generation)

使用 Python 脚本将数据与 HTML 模板分离，以便维护。

**脚本结构 (`generate_grade.py`)**:
1. **数据定义**: 使用 List of Tuples 存储单词数据 `(Letter, [(Word, POS, Unit, Phonetic, Meaning), ...])`。
2. **HTML 模板**: 定义包含 CSS 样式和页面结构的字符串模板。
3. **生成逻辑**: 遍历数据，拼接 HTML 表格行 (`<tr>...</tr>`)。
4. **输出文件**: 写入对应的 HTML 文件 (如 `vocabulary-4s.html`)。

**运行生成**:
```bash
python3 generate_4s.py
```

## 5. 验证与发布 (Verify & Deploy)

1. **本地验证**: 在浏览器中打开生成的 HTML 文件，检查：
   - 单词拼写和音标显示是否正确。
   - "小喇叭" 发音功能是否工作。
   - 底部引用图片是否能正常加载。
2. **提交代码**:
   ```bash
   git add .
   git commit -m "feat: 添加[年级]单词表"
   git push origin master
   ```
3. **自动部署**: Vercel 会自动检测 push 并更新线上网站。
