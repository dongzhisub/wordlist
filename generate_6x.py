#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate vocabulary-6x.html for Grade 6 下册"""

# Word data: (word, pos, unit, phonetic, meaning)
words = [
    # Module 1 Unit 1
    ("A", [
        ("Asia", "n.", "M1U1", "/ˈeɪʒə/", "亚洲"),
    ]),
    ("B", [
        ("Bangkok", "n.", "M1U1", "/ˈbæŋkɒk/", "曼谷"),
        ("building", "n.", "M1U1", "/ˈbɪldɪŋ/", "建筑物"),
        ("broom", "n.", "M1U2", "/bruːm/", "扫帚"),
        ("by hand", "", "M1U2", "/baɪ hænd/", "用手"),
        ("brush", "n.", "M1U4", "/brʌʃ/", "刷，刷子"),
        ("bell", "n.", "M2U7", "/bel/", "钟，铃"),
        ("better and better", "", "M1U3", "/ˈbetə ənd ˈbetə/", "越来越好"),
    ]),
    ("C", [
        ("capital", "n.", "M1U1", "/ˈkæpɪtl/", "首都"),
        ("centimetre", "n.", "M1U1", "/ˈsentɪmiːtə(r)/", "厘米"),
        ("carry", "v.", "M1U3", "/ˈkæri/", "拿，提，扛"),
        ("carefully", "adv.", "M1U4", "/ˈkeəfəli/", "细致地，小心地"),
        ("Chinese ink painting", "", "M2U7", "/tʃaɪˈniːz ɪŋk ˈpeɪntɪŋ/", "中国水墨画"),
    ]),
    ("D", [
        ("danger", "n.", "M1U3", "/ˈdeɪndʒə(r)/", "危险"),
        ("dinosaur", "n.", "M1U3", "/ˈdaɪnəsɔː(r)/", "恐龙"),
        ("digital", "adj.", "M1U2", "/ˈdɪdʒɪtl/", "数码的"),
        ("drive", "v.", "M1U2", "/draɪv/", "驾驶"),
    ]),
    ("E", [
        ("exhibition", "n.", "M1U1", "/ˌeksɪˈbɪʃn/", "展览"),
        ("enjoy oneself", "", "M1U1", "/ɪnˈdʒɔɪ wʌnˈself/", "过得快活，得到乐趣"),
        ("even", "adv.", "M1U3", "/ˈiːvn/", "甚至，连，愈加"),
    ]),
    ("F", [
        ("famous", "adj.", "M1U1", "/ˈfeɪməs/", "著名的"),
        ("fantastic", "adj.", "M1U1", "/fænˈtæstɪk/", "极好的"),
        ("fan", "n.", "M1U1", "/fæn/", "迷，狂热爱好者"),
        ("film", "n.", "M1U2", "/fɪlm/", "电影"),
        ("fairy", "n.", "M1U2", "/ˈfeəri/", "仙子，小精灵"),
        ("follow", "v.", "M1U4", "/ˈfɒləʊ/", "跟随"),
    ]),
    ("G", [
        ("get ... in", "", "M1U1", "/get ... ɪn/", "收进..."),
        ("go fishing", "", "M1U1", "/ɡəʊ ˈfɪʃɪŋ/", "去钓鱼"),
        ("glue", "n.", "M2U5", "/ɡluː/", "胶水"),
        ("get lost", "", "M1U4", "/get lɒst/", "迷路"),
    ]),
    ("H", [
        ("huge", "adj.", "M1U1", "/hjuːdʒ/", "巨大的"),
        ("have a picnic", "", "M1U3", "/hæv ə ˈpɪknɪk/", "野餐"),
        ("headteacher", "n.", "M1U3", "/ˌhedˈtiːtʃə(r)/", "校长"),
    ]),
    ("I", [
        ("information", "n.", "M1U1", "/ˌɪnfəˈmeɪʃn/", "信息"),
        ("in danger", "", "M1U3", "/ɪn ˈdeɪndʒə(r)/", "处于危险中"),
        ("in a short time", "", "M1U2", "/ɪn ə ʃɔːt taɪm/", "很快"),
        ("ink", "n.", "M2U7", "/ɪŋk/", "墨水，墨汁"),
    ]),
    ("J", [
        ("Japan", "n.", "M1U1", "/dʒəˈpæn/", "日本"),
    ]),
    ("K", [
        ("kilometre", "n.", "M1U1", "/kɪˈlɒmɪtə(r)/", "千米，公里"),
        ("kilogram", "n.", "M1U1", "/ˈkɪləɡræm/", "千克，公斤"),
    ]),
    ("L", [
        ("life", "n.", "M1U2", "/laɪf/", "生活，生命"),
        ("look out", "", "M1U4", "/lʊk aʊt/", "小心，当心"),
        ("long race", "", "M1U4", "/lɒŋ reɪs/", "长跑"),
    ]),
    ("M", [
        ("million", "num.", "M1U1", "/ˈmɪljən/", "百万"),
        ("moon cake", "n.", "M1U3", "/muːn keɪk/", "月饼"),
        ("mountain", "n.", "M1U3", "/ˈmaʊntən/", "高山，山岳"),
        ("middle", "adj.", "M1U4", "/ˈmɪdl/", "中间的"),
    ]),
    ("N", [
        ("north-east", "n.", "M1U1", "/ˌnɔːθ ˈiːst/", "东北"),
        ("north-west", "n.", "M1U1", "/ˌnɔːθ ˈwest/", "西北"),
        ("neck", "n.", "M2U7", "/nek/", "脖子"),
        ("no smoking", "", "M1U4", "/nəʊ ˈsməʊkɪŋ/", "禁止吸烟"),
        ("no swimming", "", "M1U4", "/nəʊ ˈswɪmɪŋ/", "禁止游泳"),
    ]),
    ("O", [
        ("online", "adj.", "M1U3", "/ˌɒnˈlaɪn/", "在线的，联网的"),
        ("oil", "n.", "M1U4", "/ɔɪl/", "油，食用油，石油"),
        ("oil painting", "", "M2U7", "/ɔɪl ˈpeɪntɪŋ/", "油画"),
        ("on the left", "", "M1U4", "/ɒn ðə left/", "在左边"),
        ("on the right", "", "M1U4", "/ɒn ðə raɪt/", "在右边"),
        ("on the way", "", "M1U4", "/ɒn ðə weɪ/", "在路上"),
    ]),
    ("P", [
        ("palace", "n.", "M1U1", "/ˈpæləs/", "宫殿"),
        ("pudding", "n.", "M1U3", "/ˈpʊdɪŋ/", "布丁"),
        ("poor", "adj.", "M1U2", "/pɔː(r)/", "可怜的，贫穷的"),
        ("photographer", "n.", "M1U2", "/fəˈtɒɡrəfə(r)/", "摄影师"),
        ("piece", "n.", "M1U3", "/piːs/", "张，片"),
        ("powerful", "adj.", "M1U4", "/ˈpaʊəfl/", "强有力的"),
        ("pain", "n.", "M1U4", "/peɪn/", "痛苦，疼痛"),
        ("path", "n.", "M1U4", "/pɑːθ/", "小径"),
        ("paints", "n.", "M2U7", "/peɪnts/", "绘画颜料"),
        ("praise", "v.", "M2U7", "/preɪz/", "赞扬"),
        ("PS", "", "M1U3", "/ˌpiː ˈes/", "附言（信末）"),
    ]),
    ("R", [
        ("race", "n.", "M1U1", "/reɪs/", "比赛"),
        ("right away", "", "M1U2", "/raɪt əˈweɪ/", "立即，马上"),
    ]),
    ("S", [
        ("south-east", "n.", "M1U1", "/ˌsaʊθ ˈiːst/", "东南"),
        ("south-west", "n.", "M1U1", "/ˌsaʊθ ˈwest/", "西南"),
        ("sushi", "n.", "M1U1", "/ˈsuːʃi/", "寿司"),
        ("something", "pron.", "M1U1", "/ˈsʌmθɪŋ/", "某事，某物"),
        ("sweep", "v.", "M1U2", "/swiːp/", "扫，打扫"),
        ("street cleaner", "n.", "M1U2", "/striːt ˈkliːnə(r)/", "环卫工人"),
        ("space", "n.", "M1U3", "/speɪs/", "太空"),
        ("scissors", "n.", "M2U5", "/ˈsɪzəz/", "剪刀"),
        ("still", "adv.", "M2U5", "/stɪl/", "仍然"),
        ("sign", "n.", "M1U4", "/saɪn/", "标志，信号"),
        ("short race", "", "M1U4", "/ʃɔːt reɪs/", "短跑"),
        ("swimming cap", "", "M1U4", "/ˈswɪmɪŋ kæp/", "游泳帽"),
        ("swimming goggles", "", "M1U4", "/ˈswɪmɪŋ ˈɡɒɡlz/", "泳镜"),
    ]),
    ("T", [
        ("Tokyo", "n.", "M1U1", "/ˈtəʊkjəʊ/", "东京"),
        ("Thailand", "n.", "M1U1", "/ˈtaɪlænd/", "泰国"),
        ("tourist", "n.", "M1U1", "/ˈtʊərɪst/", "游客"),
        ("theatre", "n.", "M1U1", "/ˈθɪətə(r)/", "剧场"),
        ("taller", "adj.", "M1U1", "/ˈtɔːlə(r)/", "更高的"),
        ("themselves", "pron.", "M1U1", "/ðəmˈselvz/", "他/她/它们自己"),
    ]),
    ("U", [
        ("unhappy", "adj.", "M1U4", "/ʌnˈhæpi/", "不高兴的"),
    ]),
    ("W", [
        ("without", "prep.", "M1U3", "/wɪˈðaʊt/", "没有"),
        ("weigh", "v.", "M1U1", "/weɪ/", "重量是，称...的重量"),
        ("writer", "n.", "M1U2", "/ˈraɪtə(r)/", "作家"),
        ("wish", "v.", "M1U2", "/wɪʃ/", "希望"),
        ("wife", "n.", "M1U2", "/waɪf/", "妻子，太太"),
        ("warm-up", "n.", "M1U4", "/ˈwɔːm ʌp/", "准备活动"),
    ]),
]

# Sort all groups alphabetically by letter just in case
words.sort(key=lambda x: x[0])
for letter, word_list in words:
    word_list.sort(key=lambda x: x[0].lower())  # Sort words alphabetically

html_start = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>沪教版六年级英语下册 - 单词表</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 { text-align: center; color: white; margin-bottom: 30px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); font-size: 2.5em; }
        .word-table { width: 100%; border-collapse: collapse; background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); margin-bottom: 30px; }
        .word-table th { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 15px; text-align: left; font-size: 1.1em; }
        .word-table td { padding: 12px 15px; border-bottom: 1px solid #eee; }
        .word-table tr:hover { background: linear-gradient(90deg, #f8f9ff 0%, #fff 100%); }
        .word { font-weight: bold; color: #333; font-size: 1.1em; }
        .pos { color: #667eea; font-style: italic; font-size: 0.95em; }
        .phonetic { color: #888; font-family: 'Lucida Sans Unicode', sans-serif; }
        .meaning { color: #555; }
        .unit { color: #f59e0b; font-size: 0.85em; font-weight: bold; }
        .letter-header { background: linear-gradient(90deg, #f0f4ff 0%, #fff 100%); font-weight: bold; font-size: 1.3em; color: #764ba2; }
        .letter-header td { padding: 10px 15px; border-left: 4px solid #764ba2; }
        .reference-section { background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 15px; margin-top: 30px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); }
        .reference-section h2 { color: #764ba2; margin-bottom: 15px; font-size: 1.8em; }
        .reference-intro { color: #666; margin-bottom: 25px; font-size: 1.1em; }
        .image-gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 25px; }
        .image-item { background: #f8f9ff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); transition: transform 0.3s ease; }
        .image-item:hover { transform: translateY(-5px); }
        .image-item img { width: 100%; height: auto; display: block; }
        .image-caption { padding: 15px; color: #555; font-size: 0.95em; }
        .image-caption strong { color: #667eea; }
        .copyright-notice { color: #888; font-size: 0.9em; text-align: center; padding-top: 20px; border-top: 1px solid #eee; }
        .copyright-notice a { color: #667eea; text-decoration: none; }
        .copyright-notice a:hover { text-decoration: underline; }
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
        <h1>📚 沪教版六年级英语下册 单词表</h1>
        <table class="word-table">
            <thead>
                <tr>
                    <th style="width:22%">单词 Word</th>
                    <th style="width:8%">词性</th>
                    <th style="width:18%">音标 Phonetic</th>
                    <th style="width:8%">单元</th>
                    <th style="width:44%">中文意思 Meaning</th>
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
                    <td colspan="5">{current_letter}</td>
                </tr>''')
    
    for w in word_list:
        word, pos, unit, phonetic, meaning = w
        if not word:
            continue
        clean_word = word.split()[0].replace("(", "").replace(")", "")
        word_rows.append(f'''                <tr>
                    <td class="word-cell"><span class="word">{word}</span><button class="speak-btn" onclick="speak('{clean_word}')" title="点击发音"><svg viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg></button></td>
                    <td class="pos">{pos if pos else "-"}</td>
                    <td class="phonetic">{phonetic if phonetic else "-"}</td>
                    <td class="unit">{unit if unit else "-"}</td>
                    <td class="meaning">{meaning}</td>
                </tr>''')

word_table_end = '''            </tbody>
        </table>
'''

ref_section = '''
        <div class="reference-section">
            <h2>📖 原始资料引用 (Source References)</h2>
            <p class="reference-intro">以下图片为沪教版六年级英语下册（牛津上海版）电子课本单词表原始截图，仅供学习参考使用。</p>
            <div class="image-gallery">
                <div class="image-item"><img src="images6x/page1.jpg" alt="单词表第1页"><div class="image-caption"><strong>第1页</strong></div></div>
                <div class="image-item"><img src="images6x/page2.jpg" alt="单词表第2页"><div class="image-caption"><strong>第2页</strong></div></div>
                <div class="image-item"><img src="images6x/page3.jpg" alt="单词表第3页"><div class="image-caption"><strong>第3页</strong></div></div>
                <div class="image-item"><img src="images6x/page4.jpg" alt="单词表第4页"><div class="image-caption"><strong>第4页</strong></div></div>
                <div class="image-item"><img src="images6x/page5.jpg" alt="单词表第5页"><div class="image-caption"><strong>第5页</strong></div></div>
                <div class="image-item"><img src="images6x/page6.jpg" alt="单词表第6页"><div class="image-caption"><strong>第6页</strong></div></div>
                <div class="image-item"><img src="images6x/page7.jpg" alt="单词表第7页"><div class="image-caption"><strong>第7页</strong></div></div>
                <div class="image-item"><img src="images6x/page8.jpg" alt="单词表第8页"><div class="image-caption"><strong>第8页</strong></div></div>
                <div class="image-item"><img src="images6x/page9.jpg" alt="单词表第9页"><div class="image-caption"><strong>第9页</strong></div></div>
                <div class="image-item"><img src="images6x/page10.jpg" alt="单词表第10页"><div class="image-caption"><strong>第10页</strong></div></div>
            </div>
            <p class="copyright-notice">📌 来源: <a href="https://xueba5.com" target="_blank">xueba5.com</a> - 沪教版六年级英语下册单词表<br>本页面仅供个人学习使用，版权归原作者所有。</p>
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

html_content = html_start + '\n'.join(word_rows) + '\n' + word_table_end + ref_section

with open('/home/panxf/antigravity/wordlist/vocabulary-6x.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

word_count = sum(len([w for w in g[1] if w[0]]) for g in words)
print(f"Generated vocabulary-6x.html with {word_count} words")
