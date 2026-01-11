#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate vocabulary-3x.html for Grade 3 下册"""

# Word data: (word, pos, unit, phonetic, meaning)
words = [
    ("A", [
        ("aeroplane", "n.", "M1U1", "/ˈeərəpleɪn/", "飞机"),
        ("afraid", "adj.", "M4U3", "/əˈfreɪd/", "害怕的"),
        ("angry", "adj.", "M2U1", "/ˈæŋɡri/", "生气的"),
        ("arm", "n.", "M4U1", "/ɑːm/", "手臂"),
        ("autumn", "n.", "M3U2", "/ˈɔːtəm/", "秋天"),
    ]),
    ("B", [
        ("bad", "adj.", "M4U3", "/bæd/", "坏的"),
        ("bag", "n.", "M1U2", "/bæɡ/", "包"),
        ("beach", "n.", "M3U3", "/biːtʃ/", "海滩"),
        ("bitter", "adj.", "M1U3", "/ˈbɪtə(r)/", "苦的"),
        ("body", "n.", "M4U1", "/ˈbɒdi/", "身体；躯干"),
        ("boil", "v.", "M4U3", "/bɔɪl/", "煮沸"),
        ("bread", "n.", "M1U2", "/bred/", "面包"),
        ("bus", "n.", "M1U1", "/bʌs/", "公共汽车"),
        ("busy", "adj.", "M3U2", "/ˈbɪzi/", "忙碌的"),
        ("by", "prep.", "M1U1", "/baɪ/", "在……旁边"),
    ]),
    ("C", [
        ("car", "n.", "M1U1", "/kɑː(r)/", "小汽车"),
        ("chair", "n.", "M1U1", "/tʃeə(r)/", "椅子"),
        ("children", "n.", "M1U1", "/ˈtʃɪldrən/", "（复数）儿童，小孩"),
        ("Children's Day", "", "M4U2", "/ˈtʃɪldrənz deɪ/", "儿童节"),
        ("China", "", "M4U2", "/ˈtʃaɪnə/", "中国"),
        ("cinema", "n.", "M4U2", "/ˈsɪnəmə/", "电影院"),
        ("circle", "n.", "M3U1", "/ˈsɜːkl/", "圆形"),
        ("clever", "adj.", "M2U1", "/ˈklevə(r)/", "聪明的"),
        ("clock", "n.", "M2U1", "/klɒk/", "钟"),
        ("clothes", "n.", "M2U3", "/kləʊðz/", "衣服"),
        ("coffee", "n.", "M1U3", "/ˈkɒfi/", "咖啡"),
        ("cold", "adj.", "M3U2", "/kəʊld/", "冷的"),
    ]),
    ("D", [
        ("do", "aux. v.", "M1U2", "/duː/", "（助动词）"),
        ("does", "aux. v.", "M1U2", "/dʌz/", "（助动词）"),
        ("doll", "n.", "M2U2", "/dɒl/", "玩具娃娃"),
    ]),
    ("E", [
        ("easy", "adj.", "M4U1", "/ˈiːzi/", "简单的；容易的"),
        ("elephant", "n.", "M2U1", "/ˈelɪfənt/", "大象"),
        ("else", "adv.", "M1U1", "/els/", "其他的，别的"),
        ("English", "n.", "M2U3", "/ˈɪŋɡlɪʃ/", "英语"),
    ]),
    ("F", [
        ("fifth", "num.", "M4U2", "/fɪfθ/", "第五"),
        ("finally", "adv.", "M2U1", "/ˈfaɪnəli/", "最后，终于"),
        ("finger", "n.", "M4U1", "/ˈfɪŋɡə(r)/", "手指"),
        ("first", "num.", "M4U2", "/fɜːst/", "第一"),
        ("food", "n.", "M1U2", "/fuːd/", "食物"),
        ("foot (feet)", "n.", "M4U1", "/fʊt/", "脚"),
        ("for", "prep.", "M4U2", "/fɔː(r)/", "给，对，为"),
        ("fourteenth", "num.", "M4U2", "/ˌfɔːˈtiːnθ/", "第十四"),
        ("fruit", "n.", "M1U3", "/fruːt/", "水果"),
        ("fun", "n.", "M2U2", "/fʌn/", "乐趣"),
        ("funny", "adj.", "M4U1", "/ˈfʌni/", "有趣的，滑稽的"),
    ]),
    ("G", [
        ("glass", "n.", "M1U2", "/ɡlɑːs/", "玻璃杯"),
        ("", "", "M2U3", "", "玻璃"),
        ("glove", "n.", "M2U3", "/ɡlʌv/", "手套"),
        ("go away", "", "M4U3", "/ɡəʊ əˈweɪ/", "离开"),
        ("go fishing", "", "M4U3", "/ɡəʊ ˈfɪʃɪŋ/", "去钓鱼"),
        ("grass", "n.", "M3U2", "/ɡrɑːs/", "草"),
        ("grasshopper", "n.", "M3U2", "/ˈɡrɑːshɒpə(r)/", "蚱蜢"),
        ("great", "adj.", "M2U3", "/ɡreɪt/", "好极的"),
    ]),
    ("H", [
        ("hard", "adj.", "M1U2", "/hɑːd/", "硬的"),
        ("has", "v.", "M2U1", "/hæz/", "有，拥有（第三人称单数）"),
        ("hat", "n.", "M2U1", "/hæt/", "帽子"),
        ("head", "n.", "M4U1", "/hed/", "头"),
        ("hear", "v.", "M1U1", "/hɪə(r)/", "听见"),
        ("help", "v.", "M1U3", "/help/", "帮助"),
        ("here", "adv.", "M2U1", "/hɪə(r)/", "这里，在这里"),
        ("his", "pron.", "M2U3", "/hɪz/", "他的"),
        ("home", "adv.", "M3U1", "/həʊm/", "到家，在家"),
        ("", "n.", "M3U2", "", "家"),
        ("horse", "n.", "M2U3", "/hɔːs/", "马"),
        ("house", "n.", "M3U1", "/haʊs/", "房子"),
        ("how", "adv.", "M1U2", "/haʊ/", "怎样，如何，多么"),
        ("hungry", "adj.", "M1U2", "/ˈhʌŋɡri/", "饿的"),
    ]),
    ("I", [
        ("ice-skate", "v.", "M3U3", "/ˈaɪs skeɪt/", "滑冰"),
        ("into", "prep.", "M2U1", "/ˈɪntuː/", "到……里面"),
    ]),
    ("J", [
        ("jacket", "n.", "M2U3", "/ˈdʒækɪt/", "夹克衫"),
        ("January", "n.", "M4U2", "/ˈdʒænjuəri/", "一月"),
        ("Japan", "", "M4U2", "/dʒəˈpæn/", "日本"),
        ("July", "n.", "M4U2", "/dʒuˈlaɪ/", "七月"),
        ("jump", "v.", "M2U1", "/dʒʌmp/", "跳"),
        ("June", "n.", "M4U2", "/dʒuːn/", "六月"),
    ]),
    ("K", [
        ("knee", "n.", "M4U1", "/niː/", "膝盖"),
    ]),
    ("L", [
        ("leg", "n.", "M4U1", "/leɡ/", "腿"),
        ("lemon", "n.", "M1U3", "/ˈlemən/", "柠檬"),
        ("lion", "n.", "M2U1", "/ˈlaɪən/", "狮子"),
        ("listen", "v.", "M1U1", "/ˈlɪsn/", "听"),
        ("lovely", "adj.", "M2U2", "/ˈlʌvli/", "可爱的"),
    ]),
    ("M", [
        ("make", "v.", "M2U3", "/meɪk/", "做"),
        ("March", "n.", "M4U2", "/mɑːtʃ/", "三月"),
        ("May", "n.", "M4U2", "/meɪ/", "五月"),
        ("monkey", "n.", "M2U1", "/ˈmʌŋki/", "猴子"),
        ("the Moon", "n.", "M1U2", "/ðə muːn/", "月球，月亮"),
        ("mountain", "n.", "M3U2", "/ˈmaʊntən/", "山"),
        ("myself", "pron.", "M4U1", "/maɪˈself/", "我自己"),
    ]),
    ("O", [
        ("October", "n.", "M4U2", "/ɒkˈtəʊbə(r)/", "十月"),
        ("on", "prep.", "M1U2", "/ɒn/", "在……上"),
        ("outside", "adv.", "M3U2", "/ˌaʊtˈsaɪd/", "在外面"),
        ("over there", "", "M4U3", "/ˈəʊvə(r) ðeə(r)/", "在那里"),
        ("own", "adj.", "M4U3", "/əʊn/", "自己的"),
    ]),
    ("P", [
        ("pair", "n.", "M2U3", "/peə(r)/", "一双，一对"),
        ("a pair of", "", "M2U3", "/ə peə(r) ɒv/", "一双，一对"),
        ("panda", "n.", "M2U1", "/ˈpændə/", "熊猫"),
        ("parent", "n.", "M4U2", "/ˈpeərənt/", "父亲（或母亲）"),
        ("park", "n.", "M3U3", "/pɑːk/", "公园"),
        ("photograph", "n.", "M4U2", "/ˈfəʊtəɡrɑːf/", "照片"),
        ("picnic", "n.", "M3U3", "/ˈpɪknɪk/", "野餐"),
        ("pie", "n.", "M1U2", "/paɪ/", "果馅饼"),
        ("pineapple", "n.", "M1U2", "/ˈpaɪnæpl/", "菠萝"),
        ("plant", "v.", "M3U3", "/plɑːnt/", "种植"),
        ("play", "v.", "M2U2", "/pleɪ/", "玩"),
    ]),
    ("R", [
        ("rectangle", "n.", "M3U1", "/ˈrektæŋɡl/", "长方形，矩形"),
        ("river", "n.", "M3U2", "/ˈrɪvə(r)/", "河流"),
        ("robot", "n.", "M2U2", "/ˈrəʊbɒt/", "机器人"),
        ("rock", "n.", "M2U1", "/rɒk/", "岩石"),
        ("rough", "adj.", "M1U2", "/rʌf/", "粗糙的"),
    ]),
    ("S", [
        ("salt", "n.", "M1U3", "/sɔːlt/", "盐"),
        ("salty", "adj.", "M1U3", "/ˈsɔːlti/", "咸的"),
        ("sandcastle", "n.", "M3U3", "/ˈsændkɑːsl/", "沙堡"),
        ("Saturday", "n.", "M4U2", "/ˈsætədeɪ/", "星期六"),
        ("scarf", "n.", "M2U3", "/skɑːf/", "围巾"),
        ("sea", "n.", "M3U2", "/siː/", "海"),
        ("season", "n.", "M3U3", "/ˈsiːzn/", "季节"),
        ("second", "num.", "M4U2", "/ˈsekənd/", "第二"),
        ("shape", "n.", "M3U1", "/ʃeɪp/", "形状"),
        ("ship", "n.", "M1U1", "/ʃɪp/", "（大）船，舰"),
        ("shoulder", "n.", "M4U1", "/ˈʃəʊldə(r)/", "肩膀"),
        ("Singapore", "", "M4U2", "/ˌsɪŋɡəˈpɔː(r)/", "新加坡"),
        ("skateboard", "n.", "M2U2", "/ˈskeɪtbɔːd/", "滑板"),
        ("ski", "v.", "M3U3", "/skiː/", "滑雪"),
        ("sky", "n.", "M3U2", "/skaɪ/", "天空"),
        ("sleep", "v.", "M3U2", "/sliːp/", "睡觉"),
        ("slowly", "adv.", "M3U3", "/ˈsləʊli/", "缓慢地"),
        ("smell", "v.", "M1U3", "/smel/", "闻，有……气味"),
        ("smooth", "adj.", "M1U2", "/smuːð/", "平滑的"),
        ("snow", "n.", "M3U2", "/snəʊ/", "雪"),
        ("so", "adv.", "M2U1", "/səʊ/", "那么；如此"),
        ("sock", "n.", "M2U3", "/sɒk/", "短袜"),
        ("soft", "adj.", "M1U2", "/sɒft/", "柔软的"),
        ("song", "n.", "M4U2", "/sɒŋ/", "歌曲"),
        ("sour", "adj.", "M1U3", "/ˈsaʊə(r)/", "酸的"),
        ("spring", "n.", "M3U2", "/sprɪŋ/", "春天"),
        ("square", "n.", "M3U1", "/skweə(r)/", "正方形"),
        ("star", "n.", "M3U1", "/stɑː(r)/", "（五角）星形"),
        ("stop", "v.", "M4U3", "/stɒp/", "停止"),
        ("story", "n.", "M4U3", "/ˈstɔːri/", "故事"),
        ("strong", "adj.", "M2U1", "/strɒŋ/", "强壮的"),
        ("summer", "n.", "M2U1", "/ˈsʌmə(r)/", "夏天"),
        ("super", "n.", "M2U2", "/ˈsuːpə(r)/", "超级的"),
        ("sweet", "n.", "M1U3", "/swiːt/", "糖果"),
        ("", "adj.", "M1U3", "", "甜的"),
    ]),
    ("T", [
        ("take", "v.", "M2U1", "/teɪk/", "拿；获得"),
        ("take a photograph", "", "M4U2", "/teɪk ə ˈfəʊtəɡrɑːf/", "拍照"),
        ("take a rest", "", "M2U1", "/teɪk ə rest/", "休息"),
        ("take off", "", "M3U1", "/teɪk ɒf/", "脱下（衣服）"),
        ("taste", "v.", "M1U3", "/teɪst/", "尝；有……味道"),
        ("Thailand", "", "M4U2", "/ˈtaɪlænd/", "泰国"),
        ("them", "pron.", "M1U1", "/ðem/", "他们，它们"),
        ("these", "pron.", "M2U3", "/ðiːz/", "这些"),
        ("third", "num.", "M4U2", "/θɜːd/", "第三"),
        ("those", "pron.", "M2U3", "/ðəʊz/", "那些"),
        ("tiger", "n.", "M2U1", "/ˈtaɪɡə(r)/", "老虎"),
        ("time", "n.", "M4U3", "/taɪm/", "时间"),
        ("together", "adv.", "M2U2", "/təˈɡeðə(r)/", "一起"),
        ("touch", "v.", "M1U2", "/tʌtʃ/", "触摸；碰"),
        ("train", "n.", "M2U2", "/treɪn/", "火车"),
        ("tree", "n.", "M2U1", "/triː/", "树"),
        ("triangle", "n.", "M3U1", "/ˈtraɪæŋɡl/", "三角形"),
        ("trousers", "n.", "M2U3", "/ˈtraʊzəz/", "裤子"),
        ("turn off", "", "M3U1", "/tɜːn ɒf/", "关掉（开关等）"),
    ]),
    ("U", [
        ("the UK", "", "M4U2", "/ðə ˌjuː ˈkeɪ/", "英国"),
        ("uncle", "n.", "M2U1", "/ˈʌŋkl/", "叔；舅"),
    ]),
    ("W", [
        ("walk", "v.", "M2U2", "/wɔːk/", "行走"),
        ("wall", "n.", "M2U2", "/wɔːl/", "墙"),
        ("water", "n.", "M4U3", "/ˈwɔːtə(r)/", "水"),
        ("whale", "n.", "M1U3", "/weɪl/", "鲸鱼"),
        ("window", "n.", "M1U1", "/ˈwɪndəʊ/", "窗，窗户"),
        ("winter", "n.", "M3U2", "/ˈwɪntə(r)/", "冬天"),
        ("with", "prep.", "M4U2", "/wɪð/", "和……一起"),
        ("wolf", "n.", "M4U3", "/wʊlf/", "狼"),
        ("word", "n.", "M2U3", "/wɜːd/", "单词"),
    ]),
    ("Y", [
        ("yourself", "pron.", "M4U1", "/jɔːˈself/", "你自己"),
        ("yuan", "n.", "M1U2", "/juˈæn/", "（人民币）元"),
    ]),
    ("Z", [
        ("zebra", "n.", "M2U3", "/ˈzebrə/", "斑马"),
        ("zoo", "n.", "M4U2", "/zuː/", "动物园"),
    ]),
]

daily_expressions = [
    ("How much?", "多少钱？", "M1U2"),
    ("Me too.", "我也是。", "M1U2"),
    ("I'm sorry.", "对不起。", "M2U2"),
    ("Are you OK?", "你还好吗？", "M2U2"),
    ("That's all right.", "没关系。", "M2U2"),
    ("I see.", "我明白了。", "M2U3"),
    ("May I have a try?", "我可以试试吗？", "M2U3"),
    ("How are you today?", "你今天好吗？", "M3U1"),
    ("Very well.", "很好。", "M3U1"),
    ("Of course.", "当然。", "M4U1"),
    ("Happy Children's Day!", "儿童节快乐！", "M4U2"),
    ("Great!", "太棒了！", "M4U2"),
    ("Hooray!", "好哇！", "M4U3"),
    ("Help!", "救命！", "M4U3"),
    ("Stop!", "站住！", "M4U3"),
]

html_start = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>沪教版三年级英语下册 - 单词表</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif; background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); min-height: 100vh; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 { text-align: center; color: white; margin-bottom: 30px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); font-size: 2.5em; }
        .word-table { width: 100%; border-collapse: collapse; background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); margin-bottom: 30px; }
        .word-table th { background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); color: white; padding: 15px; text-align: left; font-size: 1.1em; }
        .word-table td { padding: 12px 15px; border-bottom: 1px solid #eee; }
        .word-table tr:hover { background: linear-gradient(90deg, #fff9f0 0%, #fff 100%); }
        .word { font-weight: bold; color: #333; font-size: 1.1em; }
        .pos { color: #f6d365; font-style: italic; font-size: 0.95em; }
        .phonetic { color: #888; font-family: 'Lucida Sans Unicode', sans-serif; }
        .meaning { color: #555; }
        .unit { color: #f59e0b; font-size: 0.85em; font-weight: bold; }
        .letter-header { background: linear-gradient(90deg, #fff5e6 0%, #fff 100%); font-weight: bold; font-size: 1.3em; color: #e67e22; }
        .letter-header td { padding: 10px 15px; border-left: 4px solid #e67e22; }
        .reference-section { background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 15px; margin-top: 30px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); }
        .reference-section h2 { color: #e67e22; margin-bottom: 15px; font-size: 1.8em; }
        .reference-intro { color: #666; margin-bottom: 25px; font-size: 1.1em; }
        .image-gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 25px; }
        .image-item { background: #fffcf5; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); transition: transform 0.3s ease; }
        .image-item:hover { transform: translateY(-5px); }
        .image-item img { width: 100%; height: auto; display: block; }
        .image-caption { padding: 15px; color: #555; font-size: 0.95em; }
        .image-caption strong { color: #f39c12; }
        .copyright-notice { color: #888; font-size: 0.9em; text-align: center; padding-top: 20px; border-top: 1px solid #eee; }
        .copyright-notice a { color: #e67e22; text-decoration: none; }
        .copyright-notice a:hover { text-decoration: underline; }
        .speak-btn { background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); border: none; border-radius: 50%; width: 28px; height: 28px; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; margin-left: 8px; transition: all 0.3s ease; vertical-align: middle; box-shadow: 0 2px 5px rgba(243, 156, 18, 0.3); }
        .speak-btn:hover { transform: scale(1.15); box-shadow: 0 4px 12px rgba(243, 156, 18, 0.5); }
        .speak-btn:active { transform: scale(0.95); }
        .speak-btn.playing { animation: pulse 0.8s ease-in-out infinite; }
        @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.1); } }
        .speak-btn svg { width: 14px; height: 14px; fill: white; }
        .word-cell { display: flex; align-items: center; }
        .word-cell .word { flex: 1; }
        
        .daily-section { margin-top: 40px; margin-bottom: 30px; }
        .daily-title { text-align: center; color: #e67e22; margin-bottom: 20px; font-size: 2em; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); }
        .daily-table { width: 100%; border-collapse: collapse; background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2); }
        .daily-table th { background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); color: white; padding: 15px; text-align: left; }
        .daily-table td { padding: 15px; border-bottom: 1px solid #eee; font-size: 1.1em; }
        .daily-table tr:hover { background-color: #fff9f0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📚 沪教版三年级英语下册 单词表</h1>
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

daily_html = '''            </tbody>
        </table>

        <div class="daily-section">
            <h2 class="daily-title">🌟 Daily Expressions (日常用语)</h2>
            <table class="daily-table">
                <thead>
                    <tr>
                        <th style="width:40%">英语 Expression</th>
                        <th style="width:10%">单元</th>
                        <th style="width:50%">中文意思 Meaning</th>
                    </tr>
                </thead>
                <tbody>
'''

for expr in daily_expressions:
    en, cn, unit = expr
    clean_en = en.replace("!", "").replace("?", "").replace(".", "")
    daily_html += f'''                    <tr>
                        <td class="word-cell"><span class="word">{en}</span><button class="speak-btn" onclick="speak('{clean_en}')" title="点击发音"><svg viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg></button></td>
                        <td class="unit">{unit}</td>
                        <td class="meaning">{cn}</td>
                    </tr>
'''

daily_html += '''                </tbody>
            </table>
        </div>
'''

ref_section = '''
        <div class="reference-section">
            <h2>📖 原始资料引用 (Source References)</h2>
            <p class="reference-intro">以下图片为沪教版三年级英语下册（牛津上海版）电子课本单词表原始截图，仅供学习参考使用。</p>
            <div class="image-gallery">
                <div class="image-item"><img src="images3x/page1.jpg" alt="单词表第1页 A-G"><div class="image-caption"><strong>第1页</strong> - 单词 A-G</div></div>
                <div class="image-item"><img src="images3x/page2.jpg" alt="单词表第2页 G-P"><div class="image-caption"><strong>第2页</strong> - 单词 G-P</div></div>
                <div class="image-item"><img src="images3x/page3.jpg" alt="单词表第3页 R-U"><div class="image-caption"><strong>第3页</strong> - 单词 R-U</div></div>
                <div class="image-item"><img src="images3x/page4.jpg" alt="单词表第4页 W-Z"><div class="image-caption"><strong>第4页</strong> - 单词 W-Z</div></div>
            </div>
            <p class="copyright-notice">📌 来源: <a href="https://xueba5.com" target="_blank">xueba5.com</a> - 沪教版三年级英语下册单词表<br>本页面仅供个人学习使用，版权归原作者所有。</p>
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

html_content = html_start + '\n'.join(word_rows) + '\n' + daily_html + ref_section

with open('/home/panxf/antigravity/wordlist/vocabulary-3x.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

word_count = sum(len([w for w in g[1] if w[0]]) for g in words)
print(f"Generated vocabulary-3x.html with {word_count} words (with phonetics) and {len(daily_expressions)} daily expressions")
