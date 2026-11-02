# act2.rpy - 第二幕：相见有期
#
# 重要：以下所有 image 路径均为占位符（PLACEHOLDER）。
# 用户后续将实际图片放到 game/images/ 目录下后即可运行。
#
# 命名约定：
# - 背景：bg_xxx
# - Jack 立绘：jack_xxx
# - AMI 立绘：ami_xxx
#
# 入口：在 script.rpy 中加 `jump act2` 即可从主菜单跳转过来。
# 注意：角色定义 (jack, ami, narrator) 已移至 characters.rpy，避免重复 define 报错。

# ============================================
# 图像占位符声明
# 用户后续需要把这些图片放到 game/images/ 目录下
# ============================================

# === 场景背景 ===
image bg_park_bench_evening = "images/backgrounds/act2/bg_park_bench_evening.png"
image bg_italian_restaurant_interior = "images/backgrounds/act2/bg_italian_restaurant_interior.png"
image bg_street_evening = "images/backgrounds/act2/bg_street_evening.png"

# === AMI 立绘 ===
image ami_smile = "images/characters/ami/ami_smile.png"
image ami_curious = "images/characters/ami/ami_curious.png"
image ami_soft_smile = "images/characters/ami/ami_soft_smile.png"
image ami_nod = "images/characters/ami/ami_nod.png"
image ami_surprised = "images/characters/ami/ami_surprised.png"
image ami_shock = "images/characters/ami/ami_shock.png"
image ami_shy = "images/characters/ami/ami_shy.png"

# ============================================
# 角色定位 transform
# ============================================
transform right_pos:
    xalign 0.70       # 偏右 (0.5=正中, 1.0=最右)
    yalign 0.01     # 垂直中点对齐 (全身像时腰以上露出, 脚被屏幕底截断)

# ============================================
# 第二幕主标签
# ============================================
label act2:

    # BGM: 进入 act2 开始循环播放
    play music "audio/bgm/bgm_act2_1.ogg" loop fadein 2.0

    scene black
    with Pause(1.0)

    "Act 2：穿越时空的见面"
    with Pause(1.0)

    centered "{size=+10}一见如故旧，丝麟酌流霞。{/size}"
    with Pause(2.0)

    # ======================================
    # 场景一：公园长椅
    # ======================================
    scene bg_park_bench_evening
    with dissolve

    "长椅上的凉咖啡。街口传来一点若有若无的雨后湿气。"

    "我坐在长椅上，手里的咖啡已经凉了。"

    "2019 年的雨天叠在 2024 年的秋日里。"

    "西区的这条街我认得的。五年前离开的时候也是秋天，临走前一天我来这家意大利餐厅吃了一顿饭，畅想了很久未来，那是2019。那天外面也下了一点雨，雨丝细细的，打在窗玻璃上像谁用很软的笔在写字。"

    "离开新西兰五年了。"

    "我忽然有点恍惚。五年里我换了城市，换了工作，换了3部手机，搬了5次家。可这个地方好像什么都没变。那棵餐厅门口的树还在，叶子黄了大半，黄绿相间地挤在枝头，跟记忆里的画面叠在一起。像是有人把这五年按了暂停键，等我回来了才继续播放。"

    "杯口上一圈干掉的咖啡印。"

    "我把凉掉的咖啡放在长椅扶手上，盯着那家意大利餐厅的窗户，忽然不知道自己在等什么。"

    "玻璃里面烛光在晃，酒瓶折出彩色的光斑。"

    "典型的新西兰意大利餐厅的样子，现代建筑，大玻璃窗，原色木头桌子，和琳琅满目的酒摆满了酒柜。虽然没有去过意大利但是我始终设想真正在意大利的餐厅不是这样子的。"

    "回忆像一张被水泡过的旧照片，从边缘洇开。"

    "我们怎么认识的，我实在记不清了。"

    "好像是2013年的时候，homestay里奇怪的女孩介绍的。又好像是我自己在某个论坛上翻帖子翻到的，她回了一段话，末尾加了一个小小的笑脸符号。我被那个笑脸打动了，鬼使神差地私信了她。"

    "中间这一段是空白的。像一张被水泡过的照片，边缘都洇了，中间的人脸也看不太清。我只记得后来加了wx，她的名字一直没变过，在那里放了十多年。"

    "有一次我喝了几杯酒，很得意和她聊过天，又有一次喝了几杯酒很难过，和她聊了好久。有时候我想翻翻我们到底聊过什么，可怎么都搜不到。就像一个做了很久的梦，醒来只记得梦里有人在说话，声音很好听，但说了什么全忘了。"

    "我从来没想过会见到她。"

    with Pause(1.5)

    # ======================================
    # 场景二：餐厅内
    # ======================================
    scene bg_italian_restaurant_interior
    with dissolve

    "门推开，带进来一点外面的凉风。 和这个鬼屋一样的场景很搭配。"

    "差不多到时间了我就走进了餐厅在里面等待，点了一杯酒，琢磨着和她这个即陌生又熟悉的人见面说什么。有什么精彩的故事可以分享。我一面担心我当初和她说了什么，一面又后悔没要一张照片，如果认不出彼此岂不是很尴尬。"

    "门又开了一次。这次进来的是个看起来有百宝袋的机器猫。"

    show ami_smile at right_pos
    with dissolve

    "Ami 推门进来那一刻眼睛就在找，看到我后眉头轻轻松开，嘴角翘起，笑着叫了一声。"
    "她走了进来一眼就认出了我。心里默默的感谢上帝让我避免了尴尬。"

    "视线从下往上扫，最后停在她的脸上。"

    "她的形象和我想的一样，我猜我是因为看过朋友圈才知道的，我其实也搞不懂这个印象是哪里来的。还是那么高，到我肩膀多一点，白白的脸上一双水汪汪的大眼睛。额前那层碎发被风撩起来又落下，露出下面那片饱满明亮的额头。她穿了一件绿色的上衣，低胸，看起来好年轻。"

    hide ami_smile

    show ami_shock at right_pos
    with dissolve

    voice "audio/voice/ami_01.ogg"
    ami "Jack。这个地方好像鬼屋哎。你确定这里没有阿飘么？"

    "声音和电话里的不同，但是和我曾经的想象的一样。"

    hide ami_shock

    show ami_smile at right_pos
    with dissolve
    voice "audio/voice/ami_02.ogg"
    ami "你到了多久了？"

    "Ami 在我对面拉开椅子，把包随手放在椅背上"
    jack "一会儿。"

    hide ami_smile
    show ami_surprised at right_pos
    with dissolve
    "Ami 顺着我的视线看向窗外那棵树"
    voice "audio/voice/ami_03.ogg"
    ami "你来过这个地方么？这里好有密室逃脱的风格啊，我最喜欢这类地方了。"

    "我咽下酒，想了想。"
    jack "是么？我最喜欢密室逃脱了。另外我还喜欢吃披萨。"


    hide ami_surprised
    show ami_smile at right_pos
    voice "audio/voice/ami_04.ogg"
    ami "嗯，那么巧么？我也喜欢披萨，奥克兰有三个我最喜欢的披萨店，这里是其中之一！"
    with dissolve

    "听她说她喜欢这地方我还很开心的。这个地方刚好离我很近。"

    "坐下，碰了一下杯。酒是甜的，喝了可以直接增长体重1KG。"

    "我们坐下聊了工作，和这些年的生活，主要是关于对于彼此在威灵顿那个阶段生活的猜想。我也是第一次和一个认识了10年却未谋面的女孩聊天。大概是酒的缘故，我之后就吹嘘起了自己创业的故事。"

    hide ami_smile
    show ami_nod at right_pos
    with dissolve
    "Ami 手肘撑在桌上，下巴微微抬起，眼睛里有一丝认真的光。"
    voice "audio/voice/ami_05.ogg"
    ami "我也没有想到会有一天真的见到你，毕竟是10年都没有发过信息的人呢。"

    "我看着她的眼睛，发现她真的在听。"
    jack "不过你和我设想的一模一样。"
    hide ami_nod

    show ami_smile at right_pos
    with dissolve
    "Ami 挑了挑眉，半信半疑地笑。"
    voice "audio/voice/ami_06.ogg"
    ami "真的么？"

    jack "嗯。"
    "我低下了头目光落在了她绿色的衣服上。我怕她看出我的不安。她要是问起来——你记不记得我们那年聊过什么？你记不记得你跟我说过什么？——我大概接不上，只能含糊地笑一下。"
    "我声音放轻了一点，自己也没察觉。"
    jack "就是觉得，好像曾经见过。"
    "她的笑又开了一点。"
    jack "我很惊讶你记得我这个人，没删我的联系方式呢。"
    "我说完，她笑得更开了，眼睛弯成两道月牙，额头微微皱起来。"

    "话题被轻轻挪开。"
    "然后我们就聊起了职场的故事。"

    hide ami_smile

    show ami_soft_smile at right_pos
    with dissolve
    "Ami 低头笑了一下，声音软下来。"
    voice "audio/voice/ami_07.ogg"
    ami "你给我打电话我是很惊讶的，那天刚好有空，聊到了很晚呢。"

    "我用我的手举起酒杯作投降状。"
    jack "真是抱歉。这不是请你吃饭赔罪了么？再说你是机器猫，你怎么能和我这个凡人计较呢？"

    "她笑的很灿烂，好像猜到了其实我记不住我说了什么。"

    "时间像酒一样，被一口一口喝掉。"
    "推杯换盏间，时光飞逝如白驹过隙，转眼几个小时过去了。"

    "我站起身来看了一眼手表，又看了一眼窗外的夜色。"
    jack "差不多该走了，我送你吧。"


    hide ami_soft_smile
    show ami_nod at right_pos
    with dissolve
    "Ami 摇摇头，指了指门口。"
    voice "audio/voice/ami_08.ogg"
    ami "我是开车来的，就停在路边。"

    "我站起来拿外套。"
    jack "那就把你送到车边，你能开车吧？"
    voice "audio/voice/ami_09.ogg"
    ami "没问题。"
    hide ami_nod
    with Pause(1.0)

    # ======================================
    # 场景三：路旁
    # ======================================
    scene bg_street_evening
    with dissolve

    "走出门去，外面天已经黑了，一副日本恐怖片的气氛。"
    "到了说再见的时候了，以后还会见面么？"
    "谁有几个12年呢。谁又能保证下一个12年不删除一个只有一面之缘的人呢。想到这里，一股伤感涌上心头。"
    play sound "audio/sfx/wind.ogg"
    "虽然现在是秋天，但还是挺热的，风吹过，树叶沙沙的响起。"

    show ami_soft_smile at right_pos
    with dissolve
    "开门声空气里响了一下。"
    "她打开车门，从百宝袋里拿出了一个纸袋，袋子里放了一瓶白葡萄酒。真巧，在这么黑的街道里都能拿出白葡萄酒来，真是厉害的啊！我可是什么都看不到了呢。"
    "Ami 把纸袋递过来，眼神里带着一点小小的仪式感。"
    voice "audio/voice/ami_10.ogg"
    ami "给你的。我喜欢的酒。"

    "我有点惊讶，赶忙接过来。看着她的脸。"
    jack "你是怎么把车停到这么日式的街道来的，难道你会穿越么？认真的要说再见了呢，有机会再见。比如下一个12年的某天。不过，下次我一定在日本和你见面，或者宇宙里。绝对不能是新西兰的意大利餐厅这么难找的素材里。"

    hide ami_soft_smile
    show ami_shy at right_pos
    with dissolve
    "Ami 点点头，笑得比刚才淡一点，眼睛却没离开我。"
    voice "audio/voice/ami_11.ogg"
    ami "好的。"


    play sound "audio/sfx/car.ogg"
    "她钻进车里，车门关上，引擎低低地响了一声。我握着那瓶酒站在路边，看她倒车，调头，尾灯在街角亮了一下，然后拐弯消失了。"

    hide ami_shy
    "我在原地站了一会儿，有点意犹未尽。从来没有见过长得像机器猫，还自带日本背景的人物。"

    "忽然有点伤感，我想，大概是不会再见到了，但是起码不再是一个从未谋面的陌生人。"

    "一片云从海那边漂过来, 给刚刚晴朗的天就填上了一抹阴霾。"


    scene black
    with dissolve
    centered "{size=+10}一见如故旧，丝麟酌流霞。{/size}"
    with Pause(2.0)

    "[[END OF ACT 2]]"
    with Pause(1.5)

    # BGM: act2 结束淡出
    stop music fadeout 2.0

    return