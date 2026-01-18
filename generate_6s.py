#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate vocabulary-6s.html for Grade 6 上册 (First Semester)"""

# Word data: (Letter, [(word, pos, unit, meaning), ...])
# Note: This textbook does not include phonetics
words = [
    ("A", [
        ("about", "adv.", "U6", "大约"),
        ("activity", "n.", "U3", "活动"),
        ("advertisement", "n.", "U6", "广告"),
        ("age", "n.", "U4", "年龄"),
        ("album", "n.", "U3", "照片簿，集邮册"),
        ("almost", "adv.", "U2", "几乎"),
        ("already", "adv.", "U2", "已经"),
        ("also", "adv.", "U8", "也"),
        ("arrive", "v.", "U5", "到达"),
    ]),
    ("B", [
        ("bacon", "n.", "U8", "咸肉，熏肉"),
        ("badminton", "n.", "U1", "羽毛球"),
        ("bake", "v.", "U8", "烘烤"),
        ("bank", "n.", "U4", "银行"),
        ("barbecue", "n.", "U3", "烧烤"),
        ("bay", "n.", "U3", "海湾"),
        ("before", "conj.", "U10", "在……之前"),
        ("bitter", "adj.", "U9", "苦的"),
        ("board", "n.", "U6", "挡，板"),
        ("boil", "v.", "U8", "用沸水煮"),
    ]),
    ("C", [
        ("cabbage", "n.", "U8", "卷心菜"),
        ("centre", "n.", "U7", "中心，中央"),
        ("chase", "v.", "U7", "追赶"),
        ("chilli", "n.", "U9", "辣椒"),
        ("choir", "n.", "U5", "合唱队"),
        ("classmate", "n.", "U1", "同学"),
        ("classroom", "n.", "U5", "教室"),
        ("clerk", "n.", "U4", "职员"),
        ("club", "n.", "U5", "俱乐部"),
        ("cola", "n.", "U9", "可乐"),
        ("collect", "v.", "U3", "收集"),
        ("cost", "v. & n.", "U3", "花费"),
        ("countryside", "n.", "U10", "乡村"),
        ("craft", "n.", "U5", "工艺"),
        ("cycle", "v.", "U1", "骑自行车"),
    ]),
    ("D", [
        ("delicious", "adj.", "U9", "味道鲜美的"),
        ("dentist", "n.", "U4", "牙医"),
        ("department store", "n.", "U6", "百货商店"),
        ("diet", "n.", "U10", "（日常）饮食，（日常）食物"),
        ("discuss", "v.", "U2", "讨论"),
        ("dragon", "n.", "U3", "龙"),
        ("dumpling", "n.", "U8", "饺子"),
    ]),
    ("E", [
        ("each other", "pron.", "U2", "互相"),
        ("Earth", "n.", "U2", "地球"),
        ("eating", "n.", "U10", "吃，饮食"),
        ("else", "adv.", "U1", "别的，其他的"),
        ("enough", "adj.", "U9", "足够的"),
        ("enter", "v.", "U7", "进入"),
        ("entrance", "n.", "U5", "入口处"),
        ("environment", "n.", "U2", "环境"),
        ("escalator", "n.", "U7", "自动扶梯"),
        ("exercise", "n.", "U10", "活动，运动，锻炼"),
        ("exit", "n.", "U7", "出口"),
    ]),
    ("F", [
        ("family tree", "n.", "U1", "家谱"),
        ("ferry", "n.", "U6", "渡船"),
        ("finally", "adv.", "U5", "最后"),
        ("finish", "v.", "U4", "结束"),
        ("fireman", "n.", "U4", "消防队员"),
        ("first", "adv.", "U5", "首先"),
        ("fit", "adj.", "U10", "健康的"),
        ("fresh", "adj.", "U10", "新鲜的"),
        ("friendly", "adj.", "U2", "友好的"),
        ("frozen", "adj.", "U8", "冰冻的"),
        ("fry", "v.", "U8", "油炸，油煎，油炒"),
        ("fun", "n.", "U9", "有趣的事"),
    ]),
    ("G", [
        ("garlic", "n.", "U8", "大蒜"),
        ("granddaughter", "n.", "U1", "孙女，外孙女"),
        ("grandson", "n.", "U1", "孙子，外孙"),
        ("ground", "n.", "U5", "地，地面"),
    ]),
    ("H", [
        ("habit", "n.", "U10", "习惯"),
        ("hamburger", "n.", "U8", "汉堡包"),
        ("healthy", "adj.", "U10", "健康的"),
        ("helpful", "adj.", "U2", "有帮助的"),
        ("hotel", "n.", "U6", "旅馆"),
        ("hour", "n.", "U6", "小时"),
        ("housing estate", "n.", "U6", "居民区"),
    ]),
    ("I", [
        ("if", "conj.", "U4", "是否"),
        ("interview", "v.", "U4", "采访"),
        ("into", "prep.", "U2", "到……里面"),
        ("invitation", "n.", "U5", "请柬"),
        ("island", "n.", "U3", "岛屿"),
    ]),
    ("J", [
        ("just", "adv.", "U2", "刚才，方才"),
    ]),
    ("K", [
        ("keep", "v.", "U2", "保持"),
        ("kind", "adj.", "U2", "友好的，宽容的"),
        ("kind", "n.", "U8", "种类"),
        ("kindergarten", "n.", "U6", "幼儿园"),
        ("kite", "n.", "U3", "风筝"),
    ]),
    ("L", [
        ("land", "n.", "U2", "陆地，大地"),
        ("leave", "v.", "U2", "留下"),
        ("lemon", "n.", "U9", "柠檬"),
        ("lie", "n.", "U2", "谎言"),
        ("lift", "n.", "U7", "电梯"),
        ("light rail", "n.", "U6", "轻轨"),
        ("loudly", "adv.", "U7", "大声地"),
        ("lucky", "adj.", "U3", "好运的，幸运的"),
    ]),
    ("M", [
        ("market", "n.", "U3", "市场"),
        ("mean", "v.", "U7", "表示……的意思"),
        ("member", "n.", "U1", "成员，会员"),
        ("menu", "n.", "U8", "菜单"),
        ("middle", "n.", "U7", "中间"),
        ("minute", "n.", "U6", "分钟"),
        ("museum", "n.", "U3", "博物馆"),
    ]),
    ("N", [
        ("naughty", "adj.", "U2", "淘气的"),
        ("never", "adv.", "U2", "从不"),
        ("next", "adv.", "U5", "紧接着，随后"),
        ("noodle", "n.", "U8", "面条"),
        ("noticeboard", "n.", "U5", "布告栏"),
        ("nut", "n.", "U9", "坚果"),
    ]),
    ("O", [
        ("ocean", "n.", "U2", "洋，海洋，大海"),
        ("o'clock", "adv.", "U3", "……点钟"),
        ("only", "adv.", "U1", "仅仅"),
        ("other", "adj.", "U2", "其他的"),
    ]),
    ("P", [
        ("packet", "n.", "U8", "小包装"),
        ("parent", "n.", "U5", "父或母"),
        ("person", "n.", "U4", "人"),
        ("pilot", "n.", "U4", "飞行员"),
        ("plan", "v.", "U3", "计划"),
        ("policewoman", "n.", "U4", "女警察"),
        ("pollute", "v.", "U2", "污染"),
        ("pollution", "n.", "U2", "污染"),
        ("porridge", "n.", "U10", "粥"),
        ("postman", "n.", "U4", "邮递员"),
        ("prawn", "n.", "U8", "虾，对虾"),
        ("prepare", "v.", "U9", "使做好准备，把……预备好"),
        ("programme", "n.", "U5", "活动安排"),
        ("project", "n.", "U5", "习作项目"),
        ("promise", "v.", "U2", "承诺，保证"),
        ("promise", "n.", "U2", "承诺，诺言"),
        ("pyramid", "n.", "U10", "金字塔"),
    ]),
    ("Q", [
        ("quiz", "n.", "U10", "测试"),
    ]),
    ("R", [
        ("relative", "n.", "U1", "亲戚，亲属"),
        ("reuse", "v.", "U2", "再利用"),
        ("rubbish bin", "n.", "U2", "垃圾箱"),
        ("rule", "n.", "U7", "规则"),
    ]),
    ("S", [
        ("salt", "n.", "U10", "盐"),
        ("salty", "adj.", "U9", "咸的"),
        ("sandcastle", "n.", "U3", "沙堡"),
        ("seafood", "n.", "U8", "海鲜"),
        ("seaside", "n.", "U3", "海边，海滨"),
        ("secretary", "n.", "U4", "秘书"),
        ("section", "n.", "U8", "区域，部门"),
        ("shall", "modal v.", "U3", "将要，……好吗？"),
        ("shop", "v.", "U1", "购物"),
        ("shop assistant", "n.", "U4", "店员，售货员"),
        ("should", "modal v.", "U10", "应该"),
        ("snack", "n.", "U9", "点心，小吃"),
        ("sour", "adj.", "U9", "酸的"),
        ("space", "n.", "U3", "太空"),
        ("spend", "v.", "U3", "度过"),
        ("spicy", "adj.", "U9", "辛辣的"),
        ("spread", "v.", "U9", "抹"),
        ("stall", "n.", "U8", "摊位"),
        ("stay", "v.", "U10", "逗留"),
        ("steam", "v.", "U8", "蒸（食物）"),
        ("suggestion", "n.", "U10", "建议"),
    ]),
    ("T", [
        ("tasty", "adj.", "U9", "美味的"),
        ("teach", "v.", "U4", "教"),
        ("temple", "n.", "U6", "庙宇"),
        ("than", "conj.", "U10", "比"),
        ("travel", "v.", "U6", "行走，旅行"),
        ("trip", "n.", "U3", "旅行"),
    ]),
    ("U", [
        ("unhealthy", "adj.", "U10", "不健康的"),
        ("upstairs", "adv.", "U7", "向楼上，在楼上"),
    ]),
    ("W", [
        ("weekend", "n.", "U3", "周末"),
        ("when", "conj.", "U6", "当……的时候"),
        ("wing", "n.", "U8", "翅膀"),
    ]),
    ("Y", [
        ("yesterday", "n.", "U5", "昨天"),
        ("yet", "adv.", "U2", "尚，还，仍然"),
        ("yogurt", "n.", "U10", "酸奶"),
    ]),
]

# Phrase list data
phrases = [
    ("a few", "U6", "几个"),
    ("a little", "U10", "少量的，一些"),
    ("a lot of", "U6", "许多"),
    ("as ... as", "U10", "像……一样，如同"),
    ("find out", "U4", "查明，弄清（情况）"),
    ("go cycling", "U1", "去骑自行车"),
    ("go shopping", "U1", "去购物"),
    ("half an hour", "U6", "半小时"),
    ("in the middle", "U7", "在中间，在中央"),
    ("look after", "U2", "照顾，照看"),
    ("on the left/right", "U7", "在左/右边"),
    ("pick up", "U2", "拾起，拾起"),
    ("plenty of", "U10", "大量的，充足的"),
    ("put out", "U4", "扑灭"),
    ("wait for", "U7", "等待"),
]

# Sort all groups alphabetically
words.sort(key=lambda x: x[0])
for letter, word_list in words:
    word_list.sort(key=lambda x: x[0].lower())

html_start = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>沪教版六年级英语上册 - 单词表</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 { text-align: center; color: white; margin-bottom: 30px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); font-size: 2.5em; }
        h2 { text-align: center; color: white; margin: 30px 0 20px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); font-size: 1.8em; }
        .word-table { width: 100%; border-collapse: collapse; background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); margin-bottom: 30px; }
        .word-table th { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 15px; text-align: left; font-size: 1.1em; }
        .word-table td { padding: 12px 15px; border-bottom: 1px solid #eee; }
        .word-table tr:hover { background: linear-gradient(90deg, #f8f9ff 0%, #fff 100%); }
        .word { font-weight: bold; color: #333; font-size: 1.1em; }
        .pos { color: #667eea; font-style: italic; font-size: 0.95em; }
        .meaning { color: #555; }
        .unit { color: #f59e0b; font-size: 0.85em; font-weight: bold; }
        .letter-header { background: linear-gradient(90deg, #f0f4ff 0%, #fff 100%); font-weight: bold; font-size: 1.3em; color: #764ba2; }
        .letter-header td { padding: 10px 15px; border-left: 4px solid #764ba2; }
        .reference-section { background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 15px; margin-top: 30px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); }
        .reference-section h2 { color: #764ba2; margin-bottom: 15px; font-size: 1.8em; text-shadow: none; }
        .reference-intro { color: #666; margin-bottom: 25px; font-size: 1.1em; }
        .image-gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 25px; }
        .image-item { background: #f8f9ff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); transition: transform 0.3s ease; }
        .image-item:hover { transform: translateY(-5px); }
        .image-item img { width: 100%; height: auto; display: block; }
        .image-caption { padding: 15px; color: #555; font-size: 0.95em; }
        .image-caption strong { color: #667eea; }
        .copyright-notice { color: #888; font-size: 0.9em; text-align: center; padding-top: 20px; border-top: 1px solid #eee; }
        .speak-btn { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border: none; border-radius: 50%; width: 28px; height: 28px; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; margin-left: 8px; transition: all 0.3s ease; vertical-align: middle; box-shadow: 0 2px 5px rgba(102, 126, 234, 0.3); }
        .speak-btn:hover { transform: scale(1.15); box-shadow: 0 4px 12px rgba(102, 126, 234, 0.5); }
        .speak-btn:active { transform: scale(0.95); }
        .speak-btn.playing { animation: pulse 0.8s ease-in-out infinite; }
        @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.1); } }
        .speak-btn svg { width: 14px; height: 14px; fill: white; }
        .word-cell { display: flex; align-items: center; }
        .word-cell .word { flex: 1; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📚 沪教版六年级英语上册 单词表</h1>
        <table class="word-table">
            <thead>
                <tr>
                    <th style="width:25%">单词 Word</th>
                    <th style="width:10%">词性</th>
                    <th style="width:10%">单元</th>
                    <th style="width:55%">中文意思 Meaning</th>
                </tr>
            </thead>
            <tbody>
'''

word_rows = []
current_letter = None

for group in words:
    letter = group[0]
    word_list = group[1]
    
    if letter != current_letter:
        current_letter = letter
        word_rows.append(f'''                <tr class="letter-header">
                    <td colspan="4">{current_letter}</td>
                </tr>''')
    
    for w in word_list:
        word, pos, unit, meaning = w
        if not word:
            continue
        clean_word = word.split()[0].replace("(", "").replace(")", "").replace("'", "")
        word_rows.append(f'''                <tr>
                    <td class="word-cell"><span class="word">{word}</span><button class="speak-btn" onclick="speak('{clean_word}')" title="点击发音"><svg viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg></button></td>
                    <td class="pos">{pos if pos else "-"}</td>
                    <td class="unit">{unit if unit else "-"}</td>
                    <td class="meaning">{meaning}</td>
                </tr>''')

word_table_end = '''            </tbody>
        </table>
'''

# Phrase section
phrase_section_start = '''
        <h2>📝 常用短语 Phrase List</h2>
        <table class="word-table">
            <thead>
                <tr>
                    <th style="width:30%">短语 Phrase</th>
                    <th style="width:15%">单元</th>
                    <th style="width:55%">中文意思 Meaning</th>
                </tr>
            </thead>
            <tbody>
'''

phrase_rows = []
for phrase, unit, meaning in phrases:
    clean_phrase = phrase.split()[0].replace("(", "").replace(")", "").replace("'", "")
    phrase_rows.append(f'''                <tr>
                    <td class="word-cell"><span class="word">{phrase}</span><button class="speak-btn" onclick="speak('{clean_phrase}')" title="点击发音"><svg viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg></button></td>
                    <td class="unit">{unit}</td>
                    <td class="meaning">{meaning}</td>
                </tr>''')

phrase_section_end = '''            </tbody>
        </table>
'''

ref_section = '''
        <div class="reference-section">
            <h2>📖 原始资料引用 (Source References)</h2>
            <p class="reference-intro">以下图片为沪教版六年级英语上册（牛津上海版）电子课本单词表原始截图，仅供学习参考使用。</p>
            <div class="image-gallery">
                <div class="image-item"><img src="images6s/page-90.jpg" alt="单词表第90页"><div class="image-caption"><strong>第90页</strong></div></div>
                <div class="image-item"><img src="images6s/page-91.jpg" alt="单词表第91页"><div class="image-caption"><strong>第91页</strong></div></div>
                <div class="image-item"><img src="images6s/page-92.jpg" alt="单词表第92页"><div class="image-caption"><strong>第92页</strong></div></div>
                <div class="image-item"><img src="images6s/page-93.jpg" alt="单词表第93页"><div class="image-caption"><strong>第93页</strong></div></div>
                <div class="image-item"><img src="images6s/page-94.jpg" alt="单词表第94页"><div class="image-caption"><strong>第94页</strong></div></div>
                <div class="image-item"><img src="images6s/page-95.jpg" alt="单词表第95页"><div class="image-caption"><strong>第95页</strong></div></div>
                <div class="image-item"><img src="images6s/page-96.jpg" alt="单词表第96页"><div class="image-caption"><strong>第96页</strong></div></div>
                <div class="image-item"><img src="images6s/page-97.jpg" alt="单词表第97页"><div class="image-caption"><strong>第97页</strong></div></div>
                <div class="image-item"><img src="images6s/page-98.jpg" alt="单词表第98页"><div class="image-caption"><strong>第98页</strong></div></div>
            </div>
            <p class="copyright-notice">📌 来源: abc.pdf pages 90-98<br>本页面仅供个人学习使用。</p>
        </div>
    </div>
    <script>
        function speak(word) {
            const cleanWord = word.replace(/[^a-zA-Z\\s'-]/g, '').trim();
            if (!cleanWord) return;
            const utterance = new SpeechSynthesisUtterance(cleanWord);
            utterance.lang = 'en-US';
            utterance.rate = 0.9;
            speechSynthesis.speak(utterance);
        }
    </script>
</body>
</html>
'''

html_content = (html_start + '\n'.join(word_rows) + '\n' + word_table_end + 
                phrase_section_start + '\n'.join(phrase_rows) + '\n' + phrase_section_end +
                ref_section)

with open('vocabulary-6s.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

word_count = sum(len([w for w in g[1] if w[0]]) for g in words)
phrase_count = len(phrases)
print(f"Generated vocabulary-6s.html with {word_count} words and {phrase_count} phrases")
