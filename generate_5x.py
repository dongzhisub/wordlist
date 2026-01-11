#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate vocabulary-5x.html from extracted word data"""

# Complete word data extracted from the 5 images
words = [
    # Page 1: A-D
    ("A", [
        ("adult", "n.", "M2U2", "成年人"),
        ("ago", "adv.", "M3U2", "以前，以往"),
        ("another", "pron.", "M1U3", "又一，再一，另一（事物或人）"),
        ("Art", "n.", "M2U3", "（学科）美术"),
        ("art museum", "", "M4U1", "美术博物馆"),
        ("at last", "", "M4U3", "终于，最终"),
    ]),
    ("B", [
        ("bean", "n.", "M2U1", "豆，菜豆，豆类"),
        ("beautifully", "adv.", "", "漂亮地，优美地"),
        ("become", "v.", "M4U1", "成为，变成"),
        ("bed", "n.", "M3U3", "床"),
        ("beef", "n.", "M4U1", "牛肉"),
        ("Beijing Opera", "n.", "M4U1", "京剧"),
        ("bookshelf", "n.", "M1U2", "书架"),
        ("(be) born", "v.", "M1U2", "出生"),
        ("bought", "", "M4U1", "buy的过去式"),
        ("break", "n.", "M2U3", "间歇，休息"),
        ("break down", "", "M4U3", "倒塌，损坏"),
        ("brush", "n.", "M1U1", "毛笔，画笔"),
        ("bug", "n.", "M4U1", "小虫虫，昆虫"),
        ("build", "v.", "M4U1", "建造"),
        ("built", "", "M3U2", "build的过去式/过去分词"),
    ]),
    ("C", [
        ("cabbage", "n.", "M2U1", "卷心菜"),
        ("candle", "n.", "M4U2", "蜡烛"),
        ("car museum", "", "M4U1", "汽车博物馆"),
        ("carefully", "adv.", "M2U3", "仔细地，小心地"),
        ("carrot", "n.", "M2U1", "胡萝卜"),
        ("castle", "n.", "M4U3", "城堡"),
        ("caterpillar", "n.", "M1U2", "毛虫"),
        ("chicken", "n.", "M1U2", "鸡"),
        ("", "", "M2U1", "鸡肉"),
        ("Chinese", "n.", "M2U3", "（学科）语文"),
        ("Christmas", "n.", "M4U2", "圣诞节"),
        ("class", "n.", "M1U3", "班级，课程"),
        ("clock", "n.", "M1U3", "钟"),
        ("cloud", "n.", "M3U2", "云"),
        ("cocoon", "n.", "M1U2", "茧"),
        ("colour", "v.", "M2U3", "给……着色，涂色"),
        ("comfortable", "adj.", "M3U2", "舒服的，安逸的"),
        ("country", "n.", "M1U1", "国，国家"),
        ("crayon", "n.", "M1U1", "蜡笔"),
        ("culture", "n.", "M4U1", "文化，文明"),
        ("cupboard", "n.", "M1U2", "橱柜，衣柜"),
        ("cushion", "n.", "M3U3", "坐垫，靠垫"),
        ("cut", "", "M4U1", "cut的过去式"),
    ]),
    ("D", [
        ("dance", "v.", "M4U1", "跳舞"),
        ("degree", "n.", "M3U2", "度，度数（温度单位）"),
        ("did", "", "M2U1", "do的过去式"),
        ("dot", "n.", "M1U1", "点，小圆点"),
        ("drill", "n.", "M4U2", "钻机，钻头"),
        ("drink", "n.", "M2U1", "饮料"),
    ]),
    # Page 2: D-H
    ("D2", [
        ("drop", "v.", "M3U1", "（使意）使落下"),
        ("duckling", "n.", "M1U2", "小鸭"),
        ("dwarf", "n.", "M2U2", "小矮人"),
    ]),
    ("E", [
        ("Easter", "n.", "M4U2", "复活节"),
        ("eat", "v.", "M2U1", "吃"),
        ("egg", "n.", "M1U2", "卵，蛋"),
        ("English", "n.", "M1U3", "（学科）英语"),
        ("enjoy", "v.", "M1U3", "享受……的乐趣"),
        ("enjoy oneself", "", "M3U2", "过得快活，得到乐趣"),
        ("entrance", "n.", "M2U2", "大门（口），入门（处）"),
        ("ever", "adv.", "M4U3", "永远，曾经"),
        ("everything", "pron.", "M1U3", "所有事物，一切"),
        ("exit", "n.", "M2U2", "出口"),
    ]),
    ("F", [
        ("fair", "adj.", "M2U2", "美丽的"),
        ("fall asleep", "", "M2U2", "入睡"),
        ("fall onto...", "", "M1U1", "掉到……上面"),
        ("famous", "adj.", "M4U1", "著名的"),
        ("fancy-dress party", "", "M4U2", "化装舞会"),
        ("fast", "adj.", "M2U1", "快的，迅速的"),
        ("film", "n.", "M2U2", "电影，影片"),
        ("find", "v.", "M1U2", "找到，发现"),
        ("find out", "", "M2U2", "找出，发现"),
        ("fish", "n.", "M2U1", "鱼，鱼肉"),
        ("fisherman", "n.", "M1U2", "渔民，渔夫"),
        ("fly", "n.", "M1U2", "苍蝇"),
        ("fly", "v.", "", "飞，飞翔，飞行"),
        ("fog", "n.", "M3U2", "雾"),
        ("foggy", "adj.", "M3U2", "有雾的"),
        ("follow", "v.", "M3U1", "跟随"),
        ("forever", "adv.", "M4U3", "永远，永久"),
        ("from then on", "", "M4U3", "从那时起"),
        ("fruit", "n.", "M2U1", "水果"),
        ("funny", "adj.", "M2U2", "有趣的"),
        ("furniture", "n.", "M3U3", "家具"),
    ]),
    ("G", [
        ("giant", "n.", "M1U3", "巨人"),
        ("give", "v.", "M3U3", "给"),
        ("glue", "n.", "M1U1", "胶水"),
        ("go trick-or-treating", "", "M4U2", "玩'不给糖就捣蛋'（万圣节习俗）"),
        ("grow", "v.", "M3U2", "生长，成长"),
        ("grew", "", "M2U1", "grow的过去式"),
        ("guess", "v.", "M1U3", "猜测，猜中"),
    ]),
    ("H", [
        ("had", "", "M2U1", "have, has的过去式"),
        ("Halloween", "n.", "M4U2", "万圣节"),
        ("happen", "v.", "M3U1", "发生，出现"),
        ("have a good time", "", "M4U3", "玩得愉快"),
        ("healthy", "adj.", "M2U1", "健康的"),
        ("heard", "", "M4U2", "hear的过去式"),
        ("hers", "pron.", "M1U1", "她的"),
        ("hide", "v.", "M4U2", "藏，隐藏"),
        ("his", "pron.", "", "他的"),
        ("history", "n.", "M3U3", "历史"),
        ("history museum", "", "M4U1", "历史博物馆"),
        ("holiday", "n.", "M4U1", "节日，假日"),
        ("human", "n.", "M4U2", "人，人类"),
        ("hunt", "n.", "M4U1", "寻找"),
    ]),
    # Page 3: I-P
    ("I", [
        ("in the middle of", "", "M3U1", "在……中间"),
        ("insect museum", "", "M4U1", "昆虫博物馆"),
        ("IT", "n.", "M2U3", "（学科）信息技术"),
    ]),
    ("J", [
        ("jack-o'-lantern", "n.", "M4U2", "南瓜灯"),
    ]),
    ("K", [
        ("keep ... away", "", "M2U1", "不让接近某人（或某物）"),
        ("kill", "v.", "M2U1", "杀死"),
        ("kingdom", "n.", "M1U3", "王国"),
    ]),
    ("L", [
        ("lamp", "n.", "M3U3", "灯"),
        ("later", "adv.", "M3U3", "以后，随后"),
        ("lay eggs", "", "M1U2", "下蛋，产卵"),
        ("learnt", "", "M4U1", "learn的过去式"),
        ("leave", "v.", "", "把（某物或人）留在"),
        ("留在（原处），留下", "", "M3U1", ""),
        ("line", "n.", "M2U3", "线，线条"),
        ("listen", "v.", "M2U1", "听从，听信"),
        ("lorry", "n.", "M1U3", "卡车"),
        ("lost", "adj.", "M3U1", "迷路的"),
        ("loudly", "adv.", "M1U3", "大声地，响亮地"),
        ("love", "v.", "M4U1", "喜欢，喜爱"),
        ("lunch break", "", "M2U3", "午休"),
    ]),
    ("M", [
        ("magnet", "n.", "M1U1", "磁铁"),
        ("make", "v.", "M3U2", "使，让"),
        ("Maths", "n.", "M2U3", "（学科）数学"),
        ("maybe", "adv.", "M2U1", "也许"),
        ("mean", "v.", "M3U1", "意指，意味着"),
        ("meat", "n.", "M2U1", "肉，肉类"),
        ("mess", "n.", "M1U1", "杂乱，不整洁"),
        ("milk", "n.", "M2U1", "牛奶"),
        ("mine", "pron.", "M1U1", "我的"),
        ("minute", "n.", "", "分钟"),
        ("mirror", "n.", "M3U3", "镜子"),
        ("Mona Lisa", "", "M3U3", "《蒙娜丽莎》（画名）"),
        ("monster", "n.", "M1U2", "怪物，妖怪"),
        ("moth", "n.", "M1U2", "蛾"),
        ("motorbike", "n.", "M1U3", "摩托车"),
        ("move", "v.", "M3U1", "改变位置，移动"),
        ("Music", "n.", "M2U3", "（学科）音乐"),
    ]),
    ("N", [
        ("nail", "n.", "M1U1", "钉子"),
        ("next", "adj.", "M3U3", "紧随其后的，下一个的"),
        ("noise", "n.", "M3U3", "噪音"),
        ("notebook", "n.", "M1U1", "笔记本"),
        ("nothing", "pron.", "", "没有什么"),
        ("没有一件东西", "", "M2U3", ""),
    ]),
    ("O", [
        ("on", "adv.", "M1U1", "（电影、电视节目）正在放映/正在播出"),
        ("ours", "pron.", "M1U1", "我们的"),
        ("outside", "adv.", "M1U3", "外面"),
    ]),
    ("P", [
        ("paints", "n.", "M1U1", "绘画颜料"),
        ("painting", "n.", "", "画，油画"),
        ("Paris", "n.", "M4U4", "巴黎"),
        ("park keeper", "", "M2U1", "公园管理员"),
    ]),
    # Page 4: P-T
    ("P2", [
        ("PE", "n.", "M2U3", "（学科）体育"),
        ("perform", "v.", "M4U1", "表演"),
        ("play a trick", "", "M4U2", "搞恶作剧"),
        ("pop group", "", "M1U3", "流行音乐团体"),
        ("pork", "n.", "M2U1", "猪肉"),
        ("potato", "n.", "M2U1", "土豆，马铃薯"),
        ("present", "n.", "M4U2", "礼物"),
        ("prince", "n.", "M4U1", "王子"),
        ("princess", "n.", "M2U2", "公主"),
        ("pumpkin", "n.", "M4U2", "南瓜"),
        ("puppy", "n.", "M1U2", "小狗"),
        ("put", "v.", "M1U1", "放，安置"),
        ("put up", "", "M4U3", "张贴"),
    ]),
    ("Q", [
        ("quick", "adj.", "M2U2", "快的，迅速的"),
        ("quietly", "adv.", "M1U3", "安静地"),
    ]),
    ("R", [
        ("railway museum", "", "M4U1", "铁路博物馆"),
        ("rain", "n.", "M3U2", "雨"),
        ("really", "adv.", "M4U1", "非常，根本"),
        ("rice", "n.", "M2U1", "米饭"),
        ("run away", "", "M2U2", "逃跑"),
    ]),
    ("S", [
        ("safe", "adj.", "M2U1", "安全的"),
        ("sat", "", "M1U3", "sit的过去式"),
        ("saw", "", "M4U1", "see的过去式"),
        ("school bag", "n.", "M1U1", "书包"),
        ("science museum", "", "M4U1", "科学博物馆"),
        ("seat", "n.", "M4U1", "座位，席位"),
        ("see a film", "", "M4U1", "看电影"),
        ("shelf", "n.", "M3U3", "架子"),
        ("shout", "v.", "M1U3", "叫喊，呼喊"),
        ("sign", "n.", "M3U1", "标志，指示牌，标牌"),
        ("silk", "n.", "M1U2", "（蚕）丝，丝绸"),
        ("silkworm", "n.", "", "蚕"),
        ("sleep", "v.", "M2U2", "睡觉"),
        ("smoking", "n.", "M3U1", "吸烟"),
        ("snow", "n.", "M3U2", "雪，雪花"),
        ("Snow White", "", "M4U1", "《白雪公主》（电影名）"),
        ("snowy", "adj.", "M2U2", "下雪多的"),
        ("sofa", "n.", "M1U2", "沙发"),
        ("start", "v.", "M3U1", "开始"),
        ("stepmother", "n.", "M3U1", "继母"),
        ("stick to", "", "", "粘住，粘贴"),
        ("storm", "n.", "M1U1", "暴风雨"),
        ("stormy", "adj.", "M2U2", "有暴风雨的"),
        ("subject", "n.", "M2U3", "科目"),
        ("surprise", "n.", "", "惊喜"),
        ("surprised", "adj.", "M3U3", "惊讶的"),
        ("swimming", "n.", "M3U1", "游泳"),
    ]),
    ("T", [
        ("tape", "n.", "M1U1", "胶带"),
        ("telephone", "n.", "M3U1", "电话，电话机"),
        ("temperature", "n.", "M3U2", "温度"),
        ("Thanksgiving", "n.", "M4U2", "感恩节"),
        ("The Louvre (Museum)", "", "", "卢浮宫（博物馆）"),
        ("theirs", "pron.", "M4U1", "他们的"),
        ("think", "v.", "M1U1", "想，认为"),
        ("thousand", "num.", "", "千"),
        ("ticket", "n.", "M2U2", "票，入场券"),
        ("ticket office", "", "M1U1", "售票处"),
        ("tidy up", "", "M1U1", "收拾，整理"),
    ]),
    # Page 5: T-Y
    ("T2", [
        ("timetable", "n.", "M2U3", "时间表，课程表"),
        ("tomato", "n.", "M2U1", "番茄，西红柿"),
        ("tomorrow", "adv.", "M3U2", "（在）明天"),
        ("tonight", "adv.", "M3U2", "（在）今晚"),
        ("town", "n.", "M3U3", "镇，城镇"),
        ("Toy Story", "", "M2U2", "《玩具总动员》（电影名）"),
        ("trip", "n.", "M4U1", "旅行，旅程"),
        ("turkey", "n.", "M4U2", "火鸡"),
        ("typhoon", "n.", "M3U2", "台风"),
    ]),
    ("U", [
        ("ugly", "adj.", "M4U1", "丑陋的，难看的"),
        ("unhealthy", "adj.", "M2U1", "不健康的，有害健康的"),
        ("useful", "adj.", "M4U1", "有用的"),
    ]),
    ("V", [
        ("vegetable", "n.", "M2U1", "蔬菜"),
        ("village", "n.", "M3U3", "乡村，村庄"),
    ]),
    ("W", [
        ("wake up", "", "M2U2", "唤醒，弄醒"),
        ("walk", "v.", "M1U3", "牵着（动物）走，遛"),
        ("wall", "n.", "M3U3", "墙，墙壁"),
        ("was", "", "M1U2", "am, is的过去式"),
        ("weather", "n.", "M3U2", "天气，气象"),
        ("were", "", "M1U2", "are的过去式"),
        ("window", "n.", "M3U3", "窗，窗户"),
        ("wing", "n.", "M1U2", "翅膀"),
        ("window", "n.", "", "窗户"),
        ("workshop", "n.", "M4U1", "车间，工场"),
        ("world", "n.", "M1U3", "世界"),
    ]),
    ("Y", [
        ("yesterday", "adv.", "M3U2", "（在）昨天"),
        ("yours", "pron.", "M1U1", "你的，你们的"),
    ]),
]

# Daily expressions from Page 5
daily_expressions = [
    ("What a mess!", "真乱啊！", "M1U1"),
    ("What should I do?", "我该怎么办？", "M1U1"),
    ("Not at all.", "一点儿也不。", "M1U3"),
    ("Here we are.", "我们到了。", "M2U2"),
    ("Can I have ..., please?", "请给我……，好吗？", "M2U2"),
    ("That's ... yuan, please.", "请付……元。", "M2U2"),
    ("Be quick.", "快点。", "M2U2"),
    ("Sounds fun.", "听起来很有趣。", "M3U3"),
    ("Yes, let's do that.", "好的，我们就那样做吧。", "M3U3"),
    ("You're right.", "你说对了。", "M3U3"),
    ("Sure.", "当然。", "M4U1"),
    ("That's all.", "就这些。", "M4U1"),
    ("Welcome to...", "欢迎来到……", "M4U1"),
    ("Here we are.", "我们到了。", "M4U1"),
    ("Right!", "正确！", "M3U3"),
    ("What else?", "还有呢？", ""),
    ("I'm great, thanks.", "我很好，谢谢。", "M4U4"),
    ("Get out!", "出去！", "M4U3"),
]

# Read the original HTML template
with open('/home/panxf/antigravity/wordlist/vocabulary-5x.html', 'r', encoding='utf-8') as f:
    original = f.read()

# Extract CSS and structure
html_start = '''<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>沪教版五年级英语下册 - 单词表</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        h1 {
            text-align: center;
            color: white;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            font-size: 2.5em;
        }

        .word-table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            margin-bottom: 30px;
        }

        .word-table th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-size: 1.1em;
        }

        .word-table td {
            padding: 12px 15px;
            border-bottom: 1px solid #eee;
        }

        .word-table tr:hover {
            background: linear-gradient(90deg, #f8f9ff 0%, #fff 100%);
        }

        .word {
            font-weight: bold;
            color: #333;
            font-size: 1.1em;
        }

        .pos {
            color: #667eea;
            font-style: italic;
            font-size: 0.95em;
        }

        .phonetic {
            color: #888;
            font-family: 'Lucida Sans Unicode', sans-serif;
        }

        .meaning {
            color: #555;
        }

        .unit {
            color: #f59e0b;
            font-size: 0.85em;
            font-weight: bold;
        }

        .letter-header {
            background: linear-gradient(90deg, #f0f4ff 0%, #fff 100%);
            font-weight: bold;
            font-size: 1.3em;
            color: #764ba2;
        }

        .letter-header td {
            padding: 10px 15px;
            border-left: 4px solid #764ba2;
        }

        /* Daily Expressions Styles */
        .daily-expressions-section {
            background: rgba(255, 255, 255, 0.95);
            padding: 30px;
            border-radius: 15px;
            margin-top: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }

        .daily-expressions-section h2 {
            color: #764ba2;
            margin-bottom: 25px;
            font-size: 1.8em;
            border-bottom: 2px solid #f59e0b;
            padding-bottom: 10px;
        }

        .expr-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }

        .expr-item {
            display: flex;
            align-items: center;
            background: #fffbeb;
            padding: 12px 15px;
            border-radius: 8px;
            border-left: 4px solid #f59e0b;
            transition: transform 0.2s ease;
        }

        .expr-item:hover {
            transform: translateX(5px);
            background: #fef3c7;
        }

        .expr-text {
            flex: 1;
            font-weight: bold;
            color: #333;
            font-size: 1em;
        }

        .expr-cn {
            flex: 1;
            color: #666;
            font-size: 0.95em;
        }

        .expr-unit {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 4px 10px;
            border-radius: 15px;
            font-size: 0.8em;
            font-weight: bold;
            min-width: 50px;
            text-align: center;
        }

        @media (max-width: 768px) {
            .expr-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Reference Section */
        .reference-section {
            background: rgba(255, 255, 255, 0.95);
            padding: 30px;
            border-radius: 15px;
            margin-top: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }

        .reference-section h2 {
            color: #764ba2;
            margin-bottom: 15px;
            font-size: 1.8em;
        }

        .reference-intro {
            color: #666;
            margin-bottom: 25px;
            font-size: 1.1em;
        }

        .image-gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 25px;
        }

        .image-item {
            background: #f8f9ff;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .image-item:hover {
            transform: translateY(-5px);
        }

        .image-item img {
            width: 100%;
            height: auto;
            display: block;
        }

        .image-caption {
            padding: 15px;
            color: #555;
            font-size: 0.95em;
        }

        .image-caption strong {
            color: #667eea;
        }

        .copyright-notice {
            color: #888;
            font-size: 0.9em;
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid #eee;
        }

        .copyright-notice a {
            color: #667eea;
            text-decoration: none;
        }

        .copyright-notice a:hover {
            text-decoration: underline;
        }

        /* 发音按钮样式 */
        .speak-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            border-radius: 50%;
            width: 28px;
            height: 28px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            margin-left: 8px;
            transition: all 0.3s ease;
            vertical-align: middle;
            box-shadow: 0 2px 5px rgba(102, 126, 234, 0.3);
        }

        .speak-btn:hover {
            transform: scale(1.15);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.5);
        }

        .speak-btn:active {
            transform: scale(0.95);
        }

        .speak-btn.playing {
            animation: pulse 0.8s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
                box-shadow: 0 2px 5px rgba(102, 126, 234, 0.3);
            }
            50% {
                transform: scale(1.1);
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.6);
            }
        }

        .speak-btn svg {
            width: 14px;
            height: 14px;
            fill: white;
        }

        .word-cell {
            display: flex;
            align-items: center;
        }

        .word-cell .word {
            flex: 1;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>📚 沪教版五年级英语下册 单词表</h1>

        <table class="word-table">
            <thead>
                <tr>
                    <th style="width:25%">单词 Word</th>
                    <th style="width:10%">词性 POS</th>
                    <th style="width:10%">单元 Unit</th>
                    <th style="width:55%">中文意思 Meaning</th>
                </tr>
            </thead>
            <tbody>
'''

# Generate word rows
word_rows = []
current_letter = None

for group in words:
    letter = group[0]
    word_list = group[1]
    
    # Skip if just a continuation (like D2)
    display_letter = letter[0] if len(letter) > 1 and letter[1].isdigit() else letter
    
    # Add letter header if new letter
    if display_letter != current_letter and not letter[-1].isdigit():
        current_letter = display_letter
        word_rows.append(f'''                <!-- {current_letter} -->
                <tr class="letter-header">
                    <td colspan="4">{current_letter}</td>
                </tr>''')
    
    for w in word_list:
        word, pos, unit, meaning = w
        if not word:  # Skip empty words
            continue
        word_rows.append(f'''                <tr>
                    <td class="word-cell"><span class="word">{word}</span><button class="speak-btn" onclick="speak('{word.split()[0]}')" title="点击发音"><svg viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg></button></td>
                    <td class="pos">{pos if pos else "-"}</td>
                    <td class="unit">{unit if unit else "-"}</td>
                    <td class="meaning">{meaning}</td>
                </tr>''')

word_table_end = '''            </tbody>
        </table>
'''

# Generate daily expressions section
expr_section = '''        <!-- 日常用语 Daily Expressions -->
        <div class="daily-expressions-section">
            <h2>🗣️ 日常用语 Daily Expressions</h2>
            <div class="expr-grid">
'''

for eng, cn, unit in daily_expressions:
    expr_section += f'''                <div class="expr-item">
                    <span class="expr-text">{eng}</span>
                    <span class="expr-cn">{cn}</span>
                    <span class="expr-unit">{unit if unit else "-"}</span>
                </div>
'''

expr_section += '''            </div>
        </div>
'''

# Reference section
ref_section = '''
        <!-- 原始资料引用 (Source References) -->
        <div class="reference-section">
            <h2>📖 原始资料引用 (Source References)</h2>
            <p class="reference-intro">以下图片为沪教版五年级英语下册（牛津上海版）电子课本单词表原始截图，仅供学习参考使用。</p>
            <div class="image-gallery">
                <div class="image-item">
                    <img src="images5x/page1.jpg" alt="单词表第1页 A-D">
                    <div class="image-caption"><strong>第1页</strong> - 单词 A-D</div>
                </div>
                <div class="image-item">
                    <img src="images5x/page2.jpg" alt="单词表第2页 D-H">
                    <div class="image-caption"><strong>第2页</strong> - 单词 D-H</div>
                </div>
                <div class="image-item">
                    <img src="images5x/page3.jpg" alt="单词表第3页 I-P">
                    <div class="image-caption"><strong>第3页</strong> - 单词 I-P</div>
                </div>
                <div class="image-item">
                    <img src="images5x/page4.jpg" alt="单词表第4页 P-T">
                    <div class="image-caption"><strong>第4页</strong> - 单词 P-T</div>
                </div>
                <div class="image-item">
                    <img src="images5x/page5.jpg" alt="单词表第5页 T-Y + Daily Expressions">
                    <div class="image-caption"><strong>第5页</strong> - 单词 T-Y + Daily Expressions 日常用语</div>
                </div>
            </div>
            <p class="copyright-notice">📌 来源: <a href="https://xueba5.com" target="_blank">xueba5.com</a> - 沪教版五年级英语下册单词表<br>
            本页面仅供个人学习使用，版权归原作者所有。</p>
        </div>
    </div>

    <script>
        function speak(word) {
            // Clean up the word for better pronunciation
            const cleanWord = word.replace(/[^a-zA-Z\s'-]/g, '').trim();
            if (!cleanWord) return;
            
            const utterance = new SpeechSynthesisUtterance(cleanWord);
            utterance.lang = 'en-US';
            utterance.rate = 0.9;
            
            // Find the button and add playing class
            const buttons = document.querySelectorAll('.speak-btn');
            buttons.forEach(btn => {
                if (btn.onclick.toString().includes(word)) {
                    btn.classList.add('playing');
                    utterance.onend = () => btn.classList.remove('playing');
                }
            });
            
            speechSynthesis.speak(utterance);
        }
    </script>
</body>
</html>
'''

# Combine all parts
html_content = html_start + '\n'.join(word_rows) + '\n' + word_table_end + expr_section + ref_section

# Write the final HTML
with open('/home/panxf/antigravity/wordlist/vocabulary-5x.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated vocabulary-5x.html with {len([w for g in words for w in g[1] if w[0]])} words")
print(f"Daily expressions: {len(daily_expressions)}")
