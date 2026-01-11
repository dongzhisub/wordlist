#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate vocabulary-4s.html for Grade 4 上册"""

# Word data: (word, pos, unit, phonetic, meaning)
words = [
    ("A", [
        ("a bar of", "", "M3U3", "/ə bɑː(r) ɒv/", "一块，一条"),
        ("a bottle of", "", "M3U3", "/ə ˈbɒtl ɒv/", "一瓶……"),
        ("a bowl of", "", "M3U3", "/ə bəʊl ɒv/", "一碗……"),
        ("a loaf of (bread)", "", "M3U3", "/ə ləʊf ɒv/", "一条（面包）"),
        ("a lot of", "", "M3U3", "/ə lɒt ɒv/", "许多"),
        ("a packet of", "", "M3U3", "/ə ˈpækɪt ɒv/", "一包……"),
        ("afraid", "adj.", "M2U2", "/əˈfreɪd/", "害怕的"),
        ("always", "adv.", "M4U3", "/ˈɔːlweɪz/", "总是"),
        ("April", "n.", "M4U3", "/ˈeɪprəl/", "四月"),
        ("around", "prep.", "M3U2", "/əˈraʊnd/", "在……周围"),
        ("August", "n.", "M4U3", "/ˈɔːɡəst/", "八月"),
        ("aunt", "n.", "M4U3", "/ɑːnt/", "姑母，姨母，舅母，婶婶"),
        ("Australia", "n.", "M2U1", "/ɒˈstreɪliə/", "澳大利亚"),
        ("aviary", "n.", "M4U2", "/ˈeɪviəri/", "鸟舍"),
    ]),
    ("B", [
        ("back", "adv.", "M1U3", "/bæk/", "回来"),
        ("bakery", "n.", "M1U2", "/ˈbeɪkəri/", "面包店"),
        ("behind", "prep.", "M3U1", "/bɪˈhaɪnd/", "在……后面"),
        ("beside", "prep.", "M4U2", "/bɪˈsaɪd/", "在……旁边"),
        ("best wishes", "", "M4U3", "/best ˈwɪʃɪz/", "最好的祝愿"),
        ("between", "prep.", "M4U2", "/bɪˈtwiːn/", "在……中间"),
        ("bin", "n.", "M4U1", "/bɪn/", "垃圾箱"),
        ("bird", "n.", "M1U2", "/bɜːd/", "鸟"),
        ("biscuit", "n.", "M1U3", "/ˈbɪskɪt/", "饼干"),
        ("bite", "v.", "M2U3", "/baɪt/", "咬"),
        ("blouse", "n.", "M2U3", "/blaʊz/", "女式衬衣"),
        ("bookshelf", "n.", "M3U1", "/ˈbʊkʃelf/", "书架"),
        ("both", "det.", "M1U2", "/bəʊθ/", "两个都"),
        ("bottle", "n.", "M1U3", "/ˈbɒtl/", "瓶，瓶子"),
        ("bowl", "n.", "M3U3", "/bəʊl/", "碗"),
        ("bright", "adj.", "M1U3", "/braɪt/", "明亮的"),
        ("building", "n.", "M3U1", "/ˈbɪldɪŋ/", "大楼，建筑物"),
        ("bus", "n.", "M2U2", "/bʌs/", "公共汽车"),
        ("bus driver", "n.", "M2U2", "/bʌs ˈdraɪvə(r)/", "公交车司机"),
        ("busy", "adj.", "M3U1", "/ˈbɪzi/", "忙碌的"),
    ]),
    ("C", [
        ("camera", "n.", "M4U2", "/ˈkæmərə/", "照相机"),
        ("canteen", "n.", "M4U2", "/kænˈtiːn/", "食堂"),
        ("cap", "n.", "M4U2", "/kæp/", "（有帽舌的）帽子"),
        ("centre", "n.", "M3U2", "/ˈsentə(r)/", "中心"),
        ("China", "n.", "M4U3", "/ˈtʃaɪnə/", "中国"),
        ("chocolate", "n.", "M1U3", "/ˈtʃɒklət/", "巧克力"),
        ("Christmas", "n.", "M4U3", "/ˈkrɪsməs/", "圣诞节"),
        ("city", "n.", "M3U2", "/ˈsɪti/", "城市"),
        ("classmate", "n.", "M1U2", "/ˈklɑːsmeɪt/", "同学"),
        ("clean", "adj.", "M4U1", "/kliːn/", "干净的"),
        ("climb", "v.", "M1U2", "/klaɪm/", "爬"),
        ("cloud", "n.", "M4U2", "/klaʊd/", "云"),
        ("cloudy", "adj.", "M4U3", "/ˈklaʊdi/", "多云的"),
        ("coat", "n.", "M2U3", "/kəʊt/", "外套"),
        ("come", "v.", "M4U3", "/kʌm/", "来"),
        ("computer", "n.", "M3U1", "/kəmˈpjuːtə(r)/", "电脑，计算机"),
        ("computer lab", "", "M3U1", "/kəmˈpjuːtə læb/", "电脑房"),
        ("cook", "n.", "M1U2", "/kʊk/", "厨师"),
        ("cool", "adj.", "M4U1", "/kuːl/", "酷的，妙极的"),
        ("corn", "n.", "M2U1", "/kɔːn/", "谷物"),
        ("corner", "n.", "M2U3", "/ˈkɔːnə(r)/", "拐角，拐弯处"),
        ("cousin", "n.", "M3U1", "/ˈkʌzn/", "表兄妹，堂兄妹"),
        ("cow", "n.", "M1U1", "/kaʊ/", "母牛，奶牛"),
        ("crisp", "n.", "M1U2", "/krɪsp/", "薯片"),
        ("crow", "n.", "M1U3", "/krəʊ/", "乌鸦"),
        ("cupboard", "n.", "M3U1", "/ˈkʌbəd/", "橱柜"),
    ]),
    ("D", [
        ("dangerous", "adj.", "M2U2", "/ˈdeɪndʒərəs/", "危险的"),
        ("December", "n.", "M4U3", "/dɪˈsembə(r)/", "十二月"),
        ("desk", "n.", "M1U1", "/desk/", "课桌"),
        ("dish", "n.", "M1U2", "/dɪʃ/", "碟子"),
        ("dive", "v.", "M2U1", "/daɪv/", "跳水"),
        ("doctor", "n.", "M2U2", "/ˈdɒktə(r)/", "医生"),
        ("dolphin", "n.", "M1U2", "/ˈdɒlfɪn/", "海豚"),
        ("draw", "v.", "M1U2", "/drɔː/", "绘画"),
        ("dress", "n.", "M2U3", "/dres/", "裙子"),
        ("drink", "v.", "M1U3", "/drɪŋk/", "喝"),
        ("driver", "n.", "M2U2", "/ˈdraɪvə(r)/", "驾驶员"),
        ("dry", "adj.", "M1U3", "/draɪ/", "干燥的"),
        ("duck", "n.", "M4U1", "/dʌk/", "鸭子"),
    ]),
    ("E", [
        ("each other", "", "M1U3", "/iːtʃ ˈʌðə(r)/", "互相"),
        ("eleven", "num.", "M1U1", "/ɪˈlevn/", "十一"),
        ("e-mail", "n.", "M4U3", "/ˈiːmeɪl/", "电子邮件"),
        ("every", "det.", "M1U1", "/ˈevri/", "每一个"),
        ("everyone", "pron.", "M1U2", "/ˈevriwʌn/", "每人，大家"),
    ]),
    ("F", [
        ("fall", "v.", "M4U3", "/fɔːl/", "掉落"),
        ("far away", "", "M4U2", "/fɑː(r) əˈweɪ/", "距离远"),
        ("farm", "n.", "M4U1", "/fɑːm/", "农场"),
        ("fast", "adv.", "M1U2", "/fɑːst/", "快速"),
        ("February", "n.", "M4U3", "/ˈfebruəri/", "二月"),
        ("feed", "v.", "M4U1", "/fiːd/", "喂养"),
        ("fifteen", "num.", "M4U2", "/ˌfɪfˈtiːn/", "十五"),
        ("fire", "n.", "M4U2", "/ˈfaɪə(r)/", "火"),
        ("fire engine", "n.", "M2U2", "/ˈfaɪər ˌendʒɪn/", "消防车"),
        ("firefighter", "n.", "M2U2", "/ˈfaɪəfaɪtə(r)/", "消防员"),
        ("fire station", "n.", "M2U2", "/ˈfaɪə ˌsteɪʃn/", "消防站"),
        ("fish", "n.", "M2U1", "/fɪʃ/", "鱼"),
        ("floor", "n.", "M3U1", "/flɔː(r)/", "楼层"),
        ("fly", "v.", "M1U2", "/flaɪ/", "飞"),
        ("forest", "n.", "M3U1", "/ˈfɒrɪst/", "森林"),
        ("fountain", "n.", "M4U1", "/ˈfaʊntən/", "喷泉"),
        ("fourteen", "num.", "M1U1", "/ˌfɔːˈtiːn/", "十四"),
        ("friend", "n.", "M1U3", "/frend/", "朋友"),
        ("full", "adj.", "M1U3", "/fʊl/", "饱的"),
    ]),
    ("G", [
        ("garden", "n.", "M2U1", "/ˈɡɑːdn/", "花园"),
        ("glasses", "n.", "M3U3", "/ˈɡlɑːsɪz/", "(pl.) 眼镜"),
        ("grandpa", "n.", "", "/ˈɡrænpɑː/", "（外）祖父"),
        ("", "", "M3U1", "", "爷爷，外公"),
        ("grass", "n.", "M4U1", "/ɡrɑːs/", "草，草地"),
        ("grey", "adj.", "M2U3", "/ɡreɪ/", "灰色的"),
        ("guest", "n.", "M1U2", "/ɡest/", "嘉宾，客人"),
        ("gym", "n.", "M3U1", "/dʒɪm/", "体育馆"),
    ]),
    ("H", [
        ("happy", "adj.", "M1U3", "/ˈhæpi/", "快乐的"),
        ("have a look", "", "M4U2", "/hæv ə lʊk/", "看一看"),
        ("have lunch", "", "M4U2", "/hæv lʌntʃ/", "吃午餐"),
        ("hay", "n.", "M4U1", "/heɪ/", "干草"),
        ("hen", "n.", "M4U1", "/hen/", "母鸡"),
        ("her", "det.", "M1U1", "/hɜː(r)/", "她的"),
        ("her", "pron.", "", "/hɜː(r)/", "她（宾格）"),
        ("high", "adv.", "M1U2", "/haɪ/", "高，在高处"),
        ("his", "det.", "M1U2", "/hɪz/", "他的"),
        ("home", "adv.", "M1U2", "/həʊm/", "到家"),
        ("hop", "v.", "M1U2", "/hɒp/", "单脚跳行"),
        ("hot", "adj.", "M1U2", "/hɒt/", "热的"),
        ("hotel", "n.", "M3U2", "/həʊˈtel/", "旅馆"),
        ("hungry", "adj.", "M1U3", "/ˈhʌŋɡri/", "饿的"),
    ]),
    ("I", [
        ("idea", "n.", "M1U3", "/aɪˈdɪə/", "主意"),
        ("in front of", "prep.", "M3U1", "/ɪn frʌnt ɒv/", "在前面"),
        ("interview", "n.", "M1U2", "/ˈɪntəvjuː/", "访问，采访"),
    ]),
    ("J", [
        ("January", "n.", "M4U3", "/ˈdʒænjuəri/", "一月"),
        ("jeans", "n.", "M2U3", "/dʒiːnz/", "(pl.) 牛仔裤"),
        ("job", "n.", "M2U2", "/dʒɒb/", "工作"),
        ("July", "n.", "M4U3", "/dʒuˈlaɪ/", "七月"),
        ("jump", "v.", "M1U2", "/dʒʌmp/", "跳"),
        ("June", "n.", "M4U3", "/dʒuːn/", "六月"),
    ]),
    ("L", [
        ("lamp post", "n.", "M1U3", "/læmp pəʊst/", "路灯柱"),
        ("lesson", "n.", "M3U1", "/ˈlesn/", "课"),
        ("light", "n.", "M3U2", "/laɪt/", "（灯）光"),
        ("litter", "v.", "M4U1", "/ˈlɪtə(r)/", "乱扔（垃圾）"),
        ("live", "v.", "M1U1", "/lɪv/", "居住"),
        ("lunch", "n.", "M3U1", "/lʌntʃ/", "午餐"),
    ]),
    ("M", [
        ("magic", "adj.", "M4U3", "/ˈmædʒɪk/", "有魔力的"),
        ("make phone calls", "", "M4U3", "/meɪk fəʊn kɔːlz/", "打电话"),
        ("man", "n.", "M2U1", "/mæn/", "男子"),
        ("many", "det.", "M3U2", "/ˈmeni/", "许多"),
        ("map", "n.", "M4U2", "/mæp/", "地图"),
        ("March", "n.", "M4U3", "/mɑːtʃ/", "三月"),
        ("mask", "n.", "M1U1", "/mɑːsk/", "面具"),
        ("May", "n.", "M1U1", "/meɪ/", "五月"),
        ("meat", "n.", "M4U1", "/miːt/", "肉"),
        ("meet", "v.", "M1U1", "/miːt/", "遇见"),
        ("mole", "n.", "M3U3", "/məʊl/", "鼹鼠"),
        ("mooncake", "n.", "M2U1", "/ˈmuːnkeɪk/", "月饼"),
    ]),
    ("N", [
        ("near", "prep.", "M1U1", "/nɪə(r)/", "在……附近，靠近"),
        ("net", "n.", "M2U3", "/net/", "网"),
        ("new", "adj.", "M1U3", "/njuː/", "新的"),
        ("next to", "prep.", "M3U2", "/nekst tuː/", "紧邻，在近旁"),
        ("noodle", "n.", "M3U3", "/ˈnuːdl/", "面条"),
        ("November", "n.", "M4U3", "/nəʊˈvembə(r)/", "十一月"),
        ("number", "n.", "M1U1", "/ˈnʌmbə(r)/", "号码"),
        ("nurse", "n.", "M2U2", "/nɜːs/", "护士"),
    ]),
    ("O", [
        ("October", "n.", "M4U3", "/ɒkˈtəʊbə(r)/", "十月"),
        ("office", "n.", "M3U1", "/ˈɒfɪs/", "办公室"),
        ("other", "adj.", "M3U2", "/ˈʌðə(r)/", "其他的"),
        ("outside", "prep.", "M4U1", "/ˌaʊtˈsaɪd/", "在……外面"),
    ]),
    ("P", [
        ("paint", "v.", "M1U2", "/peɪnt/", "用颜料画画"),
        ("panda", "n.", "M4U3", "/ˈpændə/", "熊猫"),
        ("path", "n.", "M4U3", "/pɑːθ/", "小径"),
        ("pebble", "n.", "M1U3", "/ˈpebl/", "砾石，鹅卵石"),
        ("pen", "n.", "M4U1", "/pen/", "围，畜栏"),
        ("people", "n.", "M2U3", "/ˈpiːpl/", "人们"),
        ("pick", "v.", "M3U3", "/pɪk/", "采，摘"),
        ("picture", "n.", "M1U2", "/ˈpɪktʃə(r)/", "照片，图画"),
        ("pink", "adj.", "M2U3", "/pɪŋk/", "粉红色的"),
        ("pleasure", "n.", "M3U2", "/ˈpleʒə(r)/", "乐事"),
        ("police officer", "n.", "M2U1", "/pəˈliːs ˌɒfɪsə(r)/", "警察"),
        ("police station", "", "M2U1", "/pəˈliːs ˌsteɪʃn/", "警察局"),
        ("pond", "n.", "M4U1", "/pɒnd/", "池塘"),
        ("post office", "n.", "M2U3", "/pəʊst ˈɒfɪs/", "邮政局"),
        ("postcard", "n.", "M1U3", "/ˈpəʊstkɑːd/", "明信片"),
        ("postman", "n.", "M1U3", "/ˈpəʊstmən/", "邮递员"),
        ("princess", "n.", "M3U3", "/ˌprɪnˈses/", "公主"),
        ("put on", "", "M3U3", "/pʊt ɒn/", "戴上，穿上"),
    ]),
    ("R", [
        ("rabbit", "n.", "M3U1", "/ˈræbɪt/", "兔子"),
        ("rainy", "adj.", "M4U3", "/ˈreɪni/", "多雨的"),
        ("read", "v.", "M1U2", "/riːd/", "阅读"),
        ("receive", "v.", "M4U3", "/rɪˈsiːv/", "收到，接到"),
        ("restaurant", "n.", "M3U3", "/ˈrestrɒnt/", "餐馆"),
        ("riddle", "n.", "M2U1", "/ˈrɪdl/", "谜语"),
        ("right", "adj.", "M2U1", "/raɪt/", "对的，正确的"),
        ("road", "n.", "M3U2", "/rəʊd/", "道路"),
        ("rubbish", "n.", "M4U1", "/ˈrʌbɪʃ/", "垃圾"),
        ("run", "v.", "M1U3", "/rʌn/", "跑，跑步"),
    ]),
    ("S", [
        ("sad", "adj.", "M1U3", "/sæd/", "难过的"),
        ("section", "n.", "M3U3", "/ˈsekʃn/", "部分，部门"),
        ("send", "v.", "M3U2", "/send/", "寄（信等）"),
        ("September", "n.", "M4U3", "/sepˈtembə(r)/", "九月"),
        ("sharp", "adj.", "M2U3", "/ʃɑːp/", "锋利的"),
        ("shine", "v.", "M4U3", "/ʃaɪn/", "照耀"),
        ("shirt", "n.", "M2U3", "/ʃɜːt/", "衬衫"),
        ("shop", "n.", "M3U2", "/ʃɒp/", "商店"),
        ("shorts", "n.", "M2U3", "/ʃɔːts/", "(pl.) 短裤"),
        ("show", "v.", "M3U2", "/ʃəʊ/", "给……看，展示"),
        ("show ... around", "", "M3U1", "/ʃəʊ əˈraʊnd/", "带领（某人）参观"),
        ("sit", "v.", "M1U1", "/sɪt/", "坐"),
        ("sixteen", "num.", "M1U1", "/ˌsɪksˈtiːn/", "十六"),
        ("skate", "v.", "M2U3", "/skeɪt/", "滑冰，溜冰"),
        ("sketchbook", "n.", "M4U2", "/ˈsketʃbʊk/", "写生簿，素描簿"),
        ("skip", "v.", "M1U1", "/skɪp/", "跳绳"),
        ("skirt", "n.", "M2U3", "/skɜːt/", "短裙"),
        ("sleep", "v.", "M4U3", "/sliːp/", "睡觉"),
        ("slide", "n.", "M3U2", "/slaɪd/", "滑梯"),
        ("smoke", "n.", "M4U3", "/sməʊk/", "烟"),
        ("snake", "n.", "M3U2", "/sneɪk/", "蛇"),
        ("so", "adv.", "M1U3", "/səʊ/", "太"),
        ("snowy", "adj.", "M4U3", "/ˈsnəʊi/", "下雪多的"),
        ("some", "det.", "M3U2", "/sʌm/", "一些"),
        ("sometimes", "adv.", "M2U1", "/ˈsʌmtaɪmz/", "有时"),
        ("spider", "n.", "M3U3", "/ˈspaɪdə(r)/", "蜘蛛"),
        ("stay", "v.", "M3U2", "/steɪ/", "停留，待"),
        ("stone", "n.", "M4U1", "/stəʊn/", "石头"),
        ("street", "n.", "M3U2", "/striːt/", "街道"),
        ("strong", "adj.", "M2U3", "/strɒŋ/", "强壮的"),
        ("student", "n.", "M1U3", "/ˈstjuːdnt/", "学生"),
        ("subject", "n.", "M1U1", "/ˈsʌbdʒɪkt/", "主题"),
        ("sunny", "adj.", "M1U1", "/ˈsʌni/", "晴朗的"),
        ("supermarket", "n.", "M3U2", "/ˈsuːpəmɑːkɪt/", "超市"),
        ("sweater", "n.", "M2U3", "/ˈswetə(r)/", "毛衣，线衣"),
        ("swim", "v.", "M1U2", "/swɪm/", "游泳"),
        ("swing", "n.", "M4U1", "/swɪŋ/", "秋千"),
        ("swing", "v.", "", "/swɪŋ/", "摇动，摇动"),
    ]),
    ("T", [
        ("take", "v.", "M4U2", "/teɪk/", "乘坐，拍照"),
        ("teacher", "n.", "M2U2", "/ˈtiːtʃə(r)/", "教师"),
        ("tell", "v.", "M4U3", "/tel/", "告诉"),
        ("ten", "n.", "M1U1", "/ten/", "十"),
        ("then", "adv.", "M1U3", "/ðen/", "那么，既然如此"),
        ("then", "adv.", "", "/ðen/", "那时"),
        ("thing", "n.", "M1U3", "/θɪŋ/", "东西，物品"),
        ("think", "v.", "M2U3", "/θɪŋk/", "认为"),
        ("thirsty", "adj.", "M1U3", "/ˈθɜːsti/", "口渴的"),
        ("thirteen", "num.", "M1U3", "/ˌθɜːˈtiːn/", "十三"),
        ("throw", "v.", "M1U3", "/θrəʊ/", "扔"),
        ("tidy", "adj.", "M1U2", "/ˈtaɪdi/", "整洁的，整齐的"),
        ("time", "n.", "M1U2", "/taɪm/", "时间，时光"),
        ("tired", "adj.", "M1U3", "/ˈtaɪəd/", "疲倦的"),
        ("toast", "n.", "M1U3", "/təʊst/", "烤面包片"),
        ("too", "adv.", "M3U3", "/tuː/", "太"),
        ("tooth (pl. teeth)", "n.", "M2U3", "/tuːθ/", "牙齿"),
        ("try", "v.", "M3U1", "/traɪ/", "尝试"),
        ("T-shirt", "n.", "M2U3", "/ˈtiːʃɜːt/", "T恤衫"),
        ("twelve", "num.", "M1U1", "/twelv/", "十二"),
    ]),
    ("U", [
        ("uncle", "n.", "M2U1", "/ˈʌŋkl/", "叔，舅，姨父，姑父"),
    ]),
    ("V", [
        ("very", "adv.", "M1U2", "/ˈveri/", "非常，很"),
        ("visit", "n.", "M4U1", "/ˈvɪzɪt/", "游览，参观"),
        ("visit", "v.", "M3U2", "/ˈvɪzɪt/", "参观，拜访"),
    ]),
    ("W", [
        ("walk", "v.", "M1U1", "/wɔːk/", "走，步行"),
        ("warm", "adj.", "M4U3", "/wɔːm/", "暖和的"),
        ("wash", "v.", "M2U1", "/wɒʃ/", "洗"),
        ("wasp", "n.", "M1U2", "/wɒsp/", "黄蜂"),
        ("watch", "n.", "M3U2", "/wɒtʃ/", "手表"),
        ("watch", "v.", "M4U2", "/wɒtʃ/", "观看"),
        ("water", "n.", "M1U3", "/ˈwɔːtə(r)/", "水"),
        ("way", "n.", "M3U2", "/weɪ/", "路，路线"),
        ("weather", "n.", "M4U3", "/ˈweðə(r)/", "天气"),
        ("welcome", "v.", "M1U2", "/ˈwelkəm/", "欢迎"),
        ("well", "adv.", "M1U1", "/wel/", "好"),
        ("wet", "adj.", "M1U3", "/wet/", "湿的"),
        ("why", "adv.", "M4U3", "/waɪ/", "为什么"),
        ("windy", "adj.", "M4U3", "/ˈwɪndi/", "多风的"),
        ("word", "n.", "M1U3", "/wɜːd/", "单词"),
        ("worry", "v.", "M3U3", "/ˈwʌri/", "担心"),
        ("write", "v.", "M1U2", "/raɪt/", "写，写字"),
    ]),
    ("Y", [
        ("year", "n.", "M4U3", "/jɪə(r)/", "年"),
    ]),
]

html_start = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>沪教版四年级英语上册 - 单词表</title>
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
        <h1>📚 沪教版四年级英语上册 单词表</h1>
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
            <p class="reference-intro">以下图片为沪教版四年级英语上册（牛津上海版）电子课本单词表原始截图，仅供学习参考使用。</p>
            <div class="image-gallery">
                <div class="image-item"><img src="images4s/page1.jpg" alt="单词表第1页 A-C"><div class="image-caption"><strong>第1页</strong> - 单词 A-C</div></div>
                <div class="image-item"><img src="images4s/page2.jpg" alt="单词表第2页 C-H"><div class="image-caption"><strong>第2页</strong> - 单词 C-H</div></div>
                <div class="image-item"><img src="images4s/page3.jpg" alt="单词表第3页 H-P"><div class="image-caption"><strong>第3页</strong> - 单词 H-P</div></div>
                <div class="image-item"><img src="images4s/page4.jpg" alt="单词表第4页 R-T"><div class="image-caption"><strong>第4页</strong> - 单词 R-T</div></div>
                <div class="image-item"><img src="images4s/page5.jpg" alt="单词表第5页 T-Y"><div class="image-caption"><strong>第5页</strong> - 单词 T-Y</div></div>
            </div>
            <p class="copyright-notice">📌 来源: <a href="https://xueba5.com" target="_blank">xueba5.com</a> - 沪教版四年级英语上册单词表<br>本页面仅供个人学习使用，版权归原作者所有。</p>
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

with open('/home/panxf/antigravity/wordlist/vocabulary-4s.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

word_count = sum(len([w for w in g[1] if w[0]]) for g in words)
print(f"Generated vocabulary-4s.html with {word_count} words (with phonetics)")
