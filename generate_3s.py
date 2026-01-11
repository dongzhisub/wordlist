#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate vocabulary-3s.html for Grade 3 上册"""

# Word data: (word, pos, unit, phonetic, meaning)
words = [
    ("A", [
        ("a", "art.", "M1U1", "/ə/", "一，一个"),
        ("after", "prep.", "M1U1", "/ˈɑːftə(r)/", "（时间）在……后"),
        ("afternoon", "n.", "M1U1", "/ˌɑːftəˈnuːn/", "下午"),
        ("an", "art.", "M3U2", "/ən/", "一，一个"),
        ("and", "conj.", "M1U1", "/ænd/", "和，与"),
        ("animal", "n.", "M2U3", "/ˈænɪml/", "动物"),
        ("ant", "n.", "M4U1", "/ænt/", "蚂蚁"),
        ("apple", "n.", "M3U2", "/ˈæpl/", "苹果"),
        ("at", "prep.", "M3U2", "/æt/", "在（某处）"),
    ]),
    ("B", [
        ("baby", "n.", "M2U1", "/ˈbeɪbi/", "婴儿"),
        ("ball", "n.", "M3U2", "/bɔːl/", "球"),
        ("balloon", "n.", "M3U2", "/bəˈluːn/", "气球"),
        ("banana", "n.", "M3U2", "/bəˈnɑːnə/", "香蕉"),
        ("beautiful", "adj.", "M4U1", "/ˈbjuːtɪfl/", "漂亮的"),
        ("bee", "n.", "M4U1", "/biː/", "蜜蜂"),
        ("bicycle", "n.", "M2U2", "/ˈbaɪsɪkl/", "自行车"),
        ("big", "adj.", "M2U3", "/bɪɡ/", "大的"),
        ("bird", "n.", "M1U3", "/bɜːd/", "鸟"),
        ("birthday", "n.", "M1U3", "/ˈbɜːθdeɪ/", "生日"),
        ("black", "adj.", "M3U3", "/blæk/", "黑色的"),
        ("blackboard", "n.", "M1U2", "/ˈblækbɔːd/", "黑板"),
        ("blow", "v.", "M1U3", "/bləʊ/", "吹"),
        ("blue", "adj.", "M3U3", "/bluː/", "蓝色的"),
        ("boat", "n.", "M3U3", "/bəʊt/", "小船"),
        ("book", "n.", "M1U2", "/bʊk/", "书"),
        ("box", "n.", "M4U3", "/bɒks/", "盒子"),
        ("boy", "n.", "M1U1", "/bɔɪ/", "男孩"),
        ("branch", "n.", "M4U3", "/brɑːntʃ/", "树枝"),
        ("brother", "n.", "M2U2", "/ˈbrʌðə(r)/", "哥，弟"),
        ("brown", "adj.", "M2U3", "/braʊn/", "棕色的"),
        ("bud", "n.", "M4U3", "/bʌd/", "芽"),
        ("but", "conj.", "M2U1", "/bʌt/", "但是"),
        ("butterfly", "n.", "M4U1", "/ˈbʌtəflaɪ/", "蝴蝶"),
        ("buy", "v.", "M3U2", "/baɪ/", "买"),
    ]),
    ("C", [
        ("can", "modal v.", "M2U1", "/kæn/", "能，能够"),
        ("cake", "n.", "M1U1", "/keɪk/", "蛋糕"),
        ("card", "n.", "M1U2", "/kɑːd/", "卡片"),
        ("cat", "n.", "M2U3", "/kæt/", "猫"),
        ("chick", "n.", "M4U2", "/tʃɪk/", "小鸡"),
        ("classroom", "n.", "M1U2", "/ˈklɑːsruːm/", "教室"),
        ("clean", "v.", "M1U2", "/kliːn/", "把……擦干净，打扫"),
        ("close", "v.", "M1U2", "/kləʊz/", "关上"),
        ("colour", "v.", "M1U1", "/ˈkʌlə(r)/", "给……涂色"),
        ("", "n.", "M3U3", "", "颜色"),
        ("come in", "", "M2U2", "/kʌm ɪn/", "进来"),
        ("cool", "adj.", "M4U3", "/kuːl/", "凉爽的"),
        ("count", "v.", "M4U2", "/kaʊnt/", "数"),
        ("cut", "v.", "M1U1", "/kʌt/", "剪，切"),
    ]),
    ("D", [
        ("dad", "n.", "M1U1", "/dæd/", "爸爸"),
        ("dance", "v.", "M3U1", "/dɑːns/", "跳舞"),
        ("day", "n.", "M4U1", "/deɪ/", "一天，一日"),
        ("dog", "n.", "M2U3", "/dɒɡ/", "狗"),
        ("door", "n.", "M1U2", "/dɔː(r)/", "门"),
        ("draw", "v.", "M1U1", "/drɔː/", "画画"),
        ("dream", "n.", "M4U2", "/driːm/", "梦"),
        ("duck", "n.", "M4U1", "/dʌk/", "鸭子"),
    ]),
    ("E", [
        ("ear", "n.", "M2U3", "/ɪə(r)/", "耳朵"),
        ("eat", "v.", "M2U2", "/iːt/", "吃"),
        ("eight", "num.", "M1U3", "/eɪt/", "八"),
        ("end", "n.", "M4U2", "/end/", "结束"),
        ("evening", "n.", "M1U1", "/ˈiːvnɪŋ/", "傍晚"),
        ("eye", "n.", "M2U3", "/aɪ/", "眼睛"),
    ]),
    ("F", [
        ("face", "n.", "M4U2", "/feɪs/", "脸，面孔"),
        ("family", "n.", "M2U2", "/ˈfæməli/", "家庭"),
        ("farm", "n.", "M4U2", "/fɑːm/", "农场"),
        ("fat", "adj.", "M2U1", "/fæt/", "胖的"),
        ("father", "n.", "M2U2", "/ˈfɑːðə(r)/", "父亲"),
        ("feel", "v.", "M4U3", "/fiːl/", "感觉"),
        ("fine", "adj.", "M1U1", "/faɪn/", "健康的"),
        ("five", "num.", "M1U3", "/faɪv/", "五"),
        ("flower", "n.", "M3U3", "/ˈflaʊə(r)/", "花"),
        ("fly", "v.", "M4U1", "/flaɪ/", "飞"),
        ("fold", "v.", "M1U2", "/fəʊld/", "折叠"),
        ("football", "n.", "M2U1", "/ˈfʊtbɔːl/", "足球"),
        ("four", "num.", "M1U3", "/fɔː(r)/", "四"),
        ("friend", "n.", "M2U1", "/frend/", "朋友"),
    ]),
    ("G", [
        ("gate", "n.", "M4U2", "/ɡeɪt/", "大门"),
        ("get", "v.", "M1U2", "/ɡet/", "拿"),
        ("girl", "n.", "M1U1", "/ɡɜːl/", "女孩"),
        ("go", "v.", "M3U2", "/ɡəʊ/", "去"),
        ("good", "adj.", "M2U2", "/ɡʊd/", "好的"),
        ("grandfather", "n.", "M2U2", "/ˈɡrænfɑːðə(r)/", "（外）祖父，爷爷，外公"),
        ("grandmother", "n.", "M2U2", "/ˈɡrænmʌðə(r)/", "（外）祖母，奶奶，外婆"),
        ("green", "adj.", "M3U3", "/ɡriːn/", "绿色的"),
        ("grow", "v.", "M4U3", "/ɡrəʊ/", "生长"),
        ("guess", "v.", "M1U3", "/ɡes/", "猜"),
    ]),
    ("H", [
        ("hair", "n.", "M2U3", "/heə(r)/", "头发"),
        ("hall", "n.", "M3U1", "/hɔːl/", "礼堂"),
        ("hand", "n.", "M1U2", "/hænd/", "手"),
        ("happy", "adj.", "M3U2", "/ˈhæpi/", "快乐的"),
        ("have", "v.", "M1U1", "/hæv/", "有，拥有"),
        ("he", "pron.", "M1U3", "/hiː/", "他"),
        ("hen", "n.", "M4U2", "/hen/", "母鸡"),
        ("here", "adv.", "M1U3", "/hɪə(r)/", "这里，在这里"),
        ("hot", "adj.", "M4U2", "/hɒt/", "炎热的"),
        ("how many", "", "M3U2", "/haʊ ˈmeni/", "多少（个）"),
        ("how much", "", "M3U2", "/haʊ mʌtʃ/", "多少（钱）"),
    ]),
    ("I", [
        ("I", "pron.", "M1U1", "/aɪ/", "我"),
        ("ice cream", "n.", "M3U2", "/ˌaɪs ˈkriːm/", "冰淇淋"),
        ("in", "prep.", "M1U1", "/ɪn/", "在……里面"),
        ("insect", "n.", "M4U1", "/ˈɪnsekt/", "昆虫"),
        ("it", "pron.", "M1U3", "/ɪt/", "它"),
    ]),
    ("J", [
        ("jam", "n.", "M1U2", "/dʒæm/", "果酱"),
    ]),
    ("K", [
        ("kite", "n.", "M2U2", "/kaɪt/", "风筝"),
    ]),
    ("L", [
        ("ladybird", "n.", "M4U1", "/ˈleɪdibɜːd/", "瓢虫"),
        ("leaf (leaves)", "n.", "M4U3", "/liːf/", "叶子"),
        ("library", "n.", "M3U1", "/ˈlaɪbrəri/", "图书馆"),
        ("like", "v.", "M2U2", "/laɪk/", "喜欢"),
        ("little", "adj.", "M2U3", "/ˈlɪtl/", "小的"),
        ("long", "adj.", "M2U3", "/lɒŋ/", "长的"),
        ("look", "v.", "M2U2", "/lʊk/", "看"),
        ("look at", "", "M1U2", "/lʊk æt/", "看……"),
    ]),
    ("M", [
        ("many", "adj.", "M3U2", "/ˈmeni/", "许多的"),
        ("may", "modal v.", "M3U2", "/meɪ/", "可以"),
        ("me", "pron.", "M2U2", "/miː/", "我"),
        ("Miss", "n.", "M1U1", "/mɪs/", "小姐"),
        ("morning", "n.", "M1U1", "/ˈmɔːnɪŋ/", "早上，上午"),
        ("mother", "n.", "M2U2", "/ˈmʌðə(r)/", "母亲"),
        ("mouse", "n.", "M2U3", "/maʊs/", "老鼠"),
        ("mouth", "n.", "M2U3", "/maʊθ/", "嘴巴"),
        ("Mr", "n.", "M1U1", "/ˈmɪstə(r)/", "先生"),
        ("Mrs", "n.", "M1U1", "/ˈmɪsɪz/", "太太"),
        ("mum", "n.", "M1U1", "/mʌm/", "妈妈"),
        ("my", "pron.", "M1U2", "/maɪ/", "我的"),
    ]),
    ("N", [
        ("name", "n.", "M1U2", "/neɪm/", "名字"),
        ("new", "adj.", "M1U1", "/njuː/", "新的"),
        ("nice", "adj.", "M3U1", "/naɪs/", "好看的，美好的"),
        ("night", "n.", "M1U1", "/naɪt/", "夜晚"),
        ("nine", "num.", "M1U3", "/naɪn/", "九"),
        ("no", "excl.", "M1U3", "/nəʊ/", "不是"),
        ("nose", "n.", "M2U3", "/nəʊz/", "鼻子"),
        ("now", "adv.", "M4U3", "/naʊ/", "现在"),
    ]),
    ("O", [
        ("only", "adv.", "M1U3", "/ˈəʊnli/", "只，仅仅"),
        ("one", "num.", "M1U3", "/wʌn/", "一"),
        ("open", "v.", "M1U2", "/ˈəʊpən/", "打开"),
        ("orange", "n.", "M3U2", "/ˈɒrɪndʒ/", "橘子"),
        ("", "adj.", "M3U3", "", "橙红色的，橙黄色的"),
        ("our", "pron.", "M3U1", "/ˈaʊə(r)/", "我们的"),
    ]),
    ("P", [
        ("park", "n.", "M3U3", "/pɑːk/", "公园"),
        ("party", "n.", "M1U3", "/ˈpɑːti/", "聚会"),
        ("peach", "n.", "M3U2", "/piːtʃ/", "桃子"),
        ("pen", "n.", "M2U1", "/pen/", "钢笔"),
        ("photo", "n.", "M3U1", "/ˈfəʊtəʊ/", "照片"),
        ("picture", "n.", "M2U2", "/ˈpɪktʃə(r)/", "照片，图画"),
        ("pig", "n.", "M2U3", "/pɪɡ/", "猪"),
        ("pink", "adj.", "M2U3", "/pɪŋk/", "粉红色的"),
        ("plant", "n.", "M4U3", "/plɑːnt/", "植物"),
        ("play basketball", "", "M3U1", "/pleɪ ˈbɑːskɪtbɔːl/", "打篮球"),
        ("play football", "", "M2U1", "/pleɪ ˈfʊtbɔːl/", "踢足球"),
        ("playground", "n.", "M3U1", "/ˈpleɪɡraʊnd/", "操场"),
        ("please", "excl.", "M1U2", "/pliːz/", "（表示客气，礼貌）请"),
        ("pupil", "n.", "M3U3", "/ˈpjuːpl/", "小学生"),
        ("purple", "adj.", "M4U1", "/ˈpɜːpl/", "紫色的"),
        ("put", "v.", "M3U2", "/pʊt/", "放"),
        ("put on", "", "M4U2", "/pʊt ɒn/", "穿上"),
    ]),
    ("R", [
        ("rabbit", "n.", "M2U3", "/ˈræbɪt/", "兔子"),
        ("rainy", "adj.", "M4U3", "/ˈreɪni/", "下雨的"),
        ("read", "v.", "M3U1", "/riːd/", "阅读"),
        ("red", "adj.", "M2U3", "/red/", "红色的"),
        ("ride", "v.", "M2U1", "/raɪd/", "骑（车）"),
        ("root", "n.", "M4U3", "/ruːt/", "根"),
        ("rose", "n.", "M3U1", "/rəʊz/", "玫瑰花"),

    ]),
    ("S", [
        ("sad", "adj.", "M4U3", "/sæd/", "悲伤的"),
        ("school", "n.", "M3U1", "/skuːl/", "学校"),
        ("see", "v.", "M3U3", "/siː/", "看见"),
        ("seed", "n.", "M4U3", "/siːd/", "种子"),
        ("seven", "num.", "M1U3", "/ˈsevn/", "七"),
        ("she", "pron.", "M1U3", "/ʃiː/", "她"),
        ("shoe", "n.", "M4U2", "/ʃuː/", "鞋子"),
        ("shop", "n.", "M3U2", "/ʃɒp/", "商店"),
        ("shopping list", "", "M3U2", "/ˈʃɒpɪŋ lɪst/", "购物单"),
        ("short", "adj.", "M2U1", "/ʃɔːt/", "矮的"),
        ("", "", "M4U3", "", "短的"),
        ("sing", "v.", "M2U1", "/sɪŋ/", "唱歌"),
        ("sister", "n.", "M2U2", "/ˈsɪstə(r)/", "姐，妹"),
        ("sit down", "", "M1U2", "/sɪt daʊn/", "坐下"),
        ("six", "num.", "M1U3", "/sɪks/", "六"),
        ("small", "adj.", "M2U3", "/smɔːl/", "小的"),
        ("some", "det.", "M3U2", "/sʌm/", "一些"),
        ("stand up", "", "M1U2", "/stænd ʌp/", "起立"),
        ("stick", "v.", "M1U1", "/stɪk/", "粘帖"),
        ("sun", "n.", "M4U1", "/sʌn/", "太阳"),
        ("sunflower", "n.", "M4U3", "/ˈsʌnflaʊə(r)/", "向日葵"),
        ("sunny", "adj.", "M4U3", "/ˈsʌni/", "晴朗的"),
        ("supermarket", "n.", "M3U2", "/ˈsuːpəmɑːkɪt/", "超市"),
        ("sure", "adv.", "M3U2", "/ʃʊə(r)/", "（表示同意）当然"),
        ("swim", "v.", "M2U1", "/swɪm/", "游泳"),
    ]),
    ("T", [
        ("table", "n.", "M1U1", "/ˈteɪbl/", "桌子"),
        ("tail", "n.", "M2U3", "/teɪl/", "尾巴"),
        ("tall", "adj.", "M2U1", "/tɔːl/", "高的"),
        ("teacher", "n.", "M1U1", "/ˈtiːtʃə(r)/", "教师"),
        ("ten", "num.", "M1U3", "/ten/", "十"),
        ("that", "pron.", "M3U1", "/ðæt/", "那，那个"),
        ("the", "art.", "M1U2", "/ðə/", "（表示特指）"),
        ("there", "adv.", "M3U1", "/ðeə(r)/", "那里"),
        ("they", "pron.", "M4U2", "/ðeɪ/", "他们"),
        ("thin", "adj.", "M2U1", "/θɪn/", "瘦的"),
        ("", "", "M4U3", "", "细的"),
        ("this", "pron.", "M1U1", "/ðɪs/", "（介绍时用）这，这个"),
        ("three", "num.", "M1U3", "/θriː/", "三"),
        ("to", "prep.", "M3U2", "/tuː/", "到，去"),
        ("today", "adv.", "M1U1", "/təˈdeɪ/", "今天"),
        ("toilet", "n.", "M3U1", "/ˈtɔɪlət/", "厕所"),
        ("too", "adv.", "M1U1", "/tuː/", "也"),
        ("toy", "n.", "M3U2", "/tɔɪ/", "玩具"),
        ("trunk", "n.", "M4U3", "/trʌŋk/", "树干"),
        ("tube", "n.", "M3U3", "/tjuːb/", "试管"),
        ("tune", "n.", "M4U3", "/tjuːn/", "曲调"),
        ("two", "num.", "M1U3", "/tuː/", "二"),
    ]),
    ("U", [
        ("under", "adv.", "M4U3", "/ˈʌndə(r)/", "在……下面"),
    ]),
    ("V", [
        ("very", "adv.", "M1U1", "/ˈveri/", "很，非常"),
    ]),
    ("W", [
        ("warm", "adj.", "M4U3", "/wɔːm/", "温暖的"),
        ("we", "pron.", "M1U1", "/wiː/", "我们"),
        ("well", "adv.", "M1U1", "/wel/", "好，对"),
        ("wet", "adj.", "M4U3", "/wet/", "湿的"),
        ("what", "pron.", "M1U2", "/wɒt/", "什么"),
        ("where", "adv.", "M3U1", "/weə(r)/", "（在）哪里"),
        ("white", "adj.", "M3U3", "/waɪt/", "白色的"),
        ("who", "pron.", "M2U1", "/huː/", "谁"),
        ("wow", "excl.", "M3U2", "/waʊ/", "（表示惊奇）哇，呀"),
        ("write", "v.", "M1U2", "/raɪt/", "写，写字"),

    ]),
    ("Y", [
        ("yellow", "adj.", "M3U3", "/ˈjeləʊ/", "黄色的"),
        ("yes", "excl.", "M1U2", "/jes/", "是的，对"),
        ("you", "pron.", "M1U1", "/juː/", "你"),
        ("your", "pron.", "M1U2", "/jɔː(r)/", "你的"),
        ("yummy", "adj.", "M1U3", "/ˈjʌmi/", "美味的"),
    ]),
]

html_start = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>沪教版三年级英语上册 - 单词表</title>
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
        <h1>📚 沪教版三年级英语上册 单词表</h1>
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
            <p class="reference-intro">以下图片为沪教版三年级英语上册（牛津上海版）电子课本单词表原始截图，仅供学习参考使用。</p>
            <div class="image-gallery">
                <div class="image-item"><img src="images3s/page1.jpg" alt="单词表第1页 A-D"><div class="image-caption"><strong>第1页</strong> - 单词 A-D</div></div>
                <div class="image-item"><img src="images3s/page2.jpg" alt="单词表第2页 E-L"><div class="image-caption"><strong>第2页</strong> - 单词 E-L</div></div>
                <div class="image-item"><img src="images3s/page3.jpg" alt="单词表第3页 L-S"><div class="image-caption"><strong>第3页</strong> - 单词 L-S</div></div>
                <div class="image-item"><img src="images3s/page4.jpg" alt="单词表第4页 S-Y"><div class="image-caption"><strong>第4页</strong> - 单词 S-Y</div></div>
            </div>
            <p class="copyright-notice">📌 来源: <a href="https://xueba5.com" target="_blank">xueba5.com</a> - 沪教版三年级英语上册单词表<br>本页面仅供个人学习使用，版权归原作者所有。</p>
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

with open('/home/panxf/antigravity/wordlist/vocabulary-3s.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

word_count = sum(len([w for w in g[1] if w[0]]) for g in words)
print(f"Generated vocabulary-3s.html with {word_count} words (with phonetics)")
