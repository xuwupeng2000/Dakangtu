# ============================================================
# 大康图 - Act 1：落日和明天
# Dakangtu - Act 1: Sunset and Tomorrow
# ============================================================
# 剧本来源: plots/act1_script.md
# 背景:     game/images/backgrounds/  (3 张 1920x1080 2D anime galgame)
# 立绘:     game/images/characters/rita/  (暂用 Rita 角色图作为 LX 立绘)
# 角色定义: characters.rpy  (lx 已在该文件定义)
# ============================================================

# ============ 背景图声明 (1920x1080 全屏) ============
# 主体场景
image bg restaurant_interior  = "images/backgrounds/act1/zimage_anime_bg_scene2_private_dining_room_00001_.png"
image bg dining_table_window  = "images/backgrounds/act1/zimage_anime_bg_scene3_dining_table_window_00001_.png"
image bg bus_stop             = "images/backgrounds/act1/zimage_anime_v5_bg_scene4_bus_stop_00001_.png"

# 兼容别名 (让旧 scene bg xxx 仍能工作 / 方便后续替换图)
image bg private_dining_room  = "images/backgrounds/act1/zimage_anime_bg_scene2_private_dining_room_00001_.png"
image bg dining_table         = "images/backgrounds/act1/zimage_anime_bg_scene3_dining_table_window_00001_.png"
image bg street_corner        = "images/backgrounds/act1/zimage_anime_v5_bg_scene4_bus_stop_00001_.png"

# ============ LX 立绘声明 ============
# 注: 暂用 Rita 角色图作为 LX 立绘占位 (因 LX 角色立绘尚未生成)
# 立绘选择依据剧本描述: 姜黄色大衣 → preview_coat_yellow.png 最贴合
# 注意: image attribute 名不能用 Python 关键字, 故用 default_view 替代 default
image lx default_view = "images/characters/rita/sprite_neutral-emote_0004.png"   # 默认: 姜黄大衣版
image lx normal     = "images/characters/rita/sprite_neutral-emote_0004.png"
image lx smile      = "images/characters/rita/sprite_content-smile_0001.png"
image lx sweet_smile = "images/characters/rita/sprite_sweet-smile_0005.png"
image lx shy        = "images/characters/rita/sprite_shy-smile_0005.png"
image lx surprised  = "images/characters/rita/sprite_surprised_0002.png"
image lx radiant    = "images/characters/rita/sprite_radiant-smile_0001.png"
image lx laugh      = "images/characters/rita/sprite_laughing_0003.png"
image lx glance     = "images/characters/rita/sprite_glare-of-judgment_0001.png"
image lx back_and_smile = "images/characters/rita/sprite_sweet-smile_0006.png"
image lx back_and_surprised = "images/characters/rita/sprite_surprised_0005.png"


# 兼容别名
image lx coat_yellow = "images/characters/rita/preview_coat_yellow.png"

# ============================================================
# 半身像位置 transform (LX 偏右, 腰以上, 不要顶天立地)
# ============================================================
transform lx_position:
    xalign 0.70       # 偏右 (0.5=正中, 1.0=最右)
    yalign 0.01     # 垂直中点对齐 (全身像时腰以上露出, 脚被屏幕底截断)
    #zoom 0.75         # 缩小到 75%, 避免顶天立地

# ============================================================
# Act 1: 落日和明天
# ============================================================
label act1:

    # 标记剧情进度
    $ act1_complete = False
    $ current_location = "restaurant"
    $ current_time = "night"

    # BGM: 进入 act1 开始循环播放
    play music "audio/bgm/bgm.ogg" loop fadein 2.0

    # ----------------- 标题 -----------------
    scene black
    with Pause(1.0)

    "Act 1：落日和明天"
    with Pause(1.0)

    centered "{size=+10}人的记忆是古怪的，很多感情最终只凝结成几个字，一幅画。{/size}"
    with Pause(2.0)

    # ============================================================
    # Scene 1: 推开 (包间远景)
    # ============================================================
    scene bg restaurant_interior
    with fade

    "我推开门走了进去。"
    with Pause(0.5)

    # 旁白：环境描述
    "天贵食府应该是这条街最高档的餐厅了。气派的大门，走入后一个小桥流水的布置。"
    "空气里有淡淡的茉莉香，混着葱油和糖醋的气息。"
    "话说也不知道都谁回来啊，好久没见到这些同学了，以前高中的时候每天都见面呢。"
    "我按着手机里那条短信找过去，推开了包间的门。"
    with Pause(1.0)

    # ============================================================
    # Scene 2: 相认 (餐桌近景)
    # ============================================================
    scene bg dining_table_window
    with dissolve

    # 显示 LX 立绘 (右侧)
    show lx normal at lx_position zorder 2
    with dissolve

    # 旁白：发现 LX
    "我在那一桌子喧闹里一眼扫过去，然后目光被她吸引了。"

    "是 LX。"
    "我差点没认出她来。"
    with Pause(0.5)

    "高中毕业那个暑假我去了南方的大学，毕业后没有听到过她的音讯。"
    "我们本来就是不怎么说话的同学，高中三年都没怎么讲过话，"
    "唯一的交集就是在一个教室里上课。"
    "毕业那年我们没有说过再见，没有留过电话，连QQ号都没加过。"
    with Pause(0.5)

    # 旁白：LX 远景视觉锚点
    "可她现在就坐在那里，夺走了我的目光。"
    "窗外是程庄路的车，尾灯拉成一条条红色的丝线；她坐在那片红色光晕的边上，脸被窗外那道光勾了一道暖边。"
    "她正侧着头跟旁边的人说话，嘴角弯着，笑得很淡很从容。"
    with Pause(1.0)

    "她没有戴眼镜。"
    "我站在原地，盯着她看了好几秒才确认。"
    "高三那年她鼻梁上永远架着一副圆框眼镜，金色的细边。没有留意过她的眼睛。"
    "此刻她坐在那里，鼻梁上干干净净的，什么都没架。眼睛显得比以前大了整整一圈，深褐色的瞳仁里映着浅浅的光。"
    with Pause(1.0)

    "我大概没见过她不戴眼镜的样子。"
    "LX 剪短了头发，戴着一个红色的发卡，穿了件姜黄色的大衣，里面是米白色的 V 领毛衣。"
    "姜黄，像深秋里银杏叶还没落尽时那种颜色，带着一点暖调。大衣的线条垂下来，把她的身形拉得很修长。她偶尔动一下，大衣的下摆随着动作轻轻晃。"
    with Pause(1.0)

    "我走近落座。她大概只是随意地扫了一眼门口，看看是谁来晚了。"
    "她的目光从我脸上滑过去，又滑回来，停住了。"
    "然后她笑了。"
    "嘴角轻轻往上弯，眼睛弯成两道很浅的月牙。"
    "那枚红色的发卡在她偏头的时候滑了一下，碰到耳朵上方的发丝，又停住。"
    with Pause(1.0)

    "「LX？」"
    "我先开口了。我记得她的名字，她学习很好，我印象里是年级第4。"
    "虽然我们不怎么说话但是她的名字我是知道的，"

    voice "audio/voice/lx_01.ogg"
    lx "你是武鹏吧，这几年的大学生活如何？"
    voice "audio/voice/lx_02.ogg"
    lx "你要努力学习哦，毕业我就要嫁给你了。"
    jack "哇时间穿越了啊，居然知道2年后发生的事情。"

    "她也马上回复了我，显然几年时间我还没有被淡忘成某甲。"
    with Pause(0.5)

    show lx smile at lx_position zorder 2
    with dissolve

    "我走到她的对面坐下，听着一群同学聊天。"
    "我平时都是聊天的主力，一个社牛，今天我倒是比较沉默，"
    "只是时不时的偷偷看看这位熟悉又陌生的美女。"
    "之后的同学聚会很模糊，就那几个人说那几个熟悉的话题。"
    "推杯换盏，时间过得很快。"
    with Pause(1.0)


    # ============================================================
    # Scene 3: 离去 (公交站)
    # ============================================================

    # LX 离场
    scene bg bus_stop
    with fade
    "散场的时候我特意多留了一会儿，想要找个机会和她搭讪。"
    "我这个人是没有任何技巧的，就是寒暄说她出落得好漂亮，有一双白白的大长腿。"
    "这话听起来有点轻佻，实则我是词穷而已。"
    "她听到这个话大概也是吃了一惊，但是没有特意的回避我。"
    "我还是找机会把她送到了楼下。"
    with Pause(1.0)

    show lx back_and_smile at lx_position zorder 2
    with dissolve

    "她站在路旁，暖黄灯光落在她脸上。"
    play sound "audio/sfx/wind.ogg"
    "风把大衣下摆吹动了一下，红色发卡滑了一下，碰到耳朵上方的发丝。"
    with Pause(1.0)

    "她看着我。我看着她。我们站在那几秒钟里，谁都没说话。"
    "身边有人来来去去，打车的声音、告别的声音、初冬的风声混在一起，"
    "可那几秒钟里我什么都听不见。"
    with Pause(1.0)

    # 内心独白 cue (D 项 - 增强代入感)
    "（我想……算了，就这样吧。）"
    with Pause(0.5)

    # 暧昧对话 (核心)
    "我脑子一热，话就冲出口了。"
    "「你……腿真长，还白。」"
    with Pause(1.0)

    show lx back_and_surprised at lx_position zorder 2
    with dissolve

    "话一出口我就想抽自己。这是什么鬼夸奖，轻佻得像在调戏。"
    "我尴尬地站着，不敢看她的眼睛。"
    with Pause(0.5)

    "但她没躲。她反而轻轻笑了一下，眼尾微微弯起来，"
    "声音轻轻的，带着点说不清的意味。"

    # 保留核心暧昧台词
    voice "audio/voice/lx_03.ogg"
    lx "嗯 你还是像以前一样那么奇怪。"
    voice "audio/voice/lx_04.ogg"
    lx "不过如果我知道未来的发展的话，说不定今天就和你回家过日子了。"
    jack "哇，这个人动不动就穿越了啊，会不是拿到了机器猫之类的宝物。"
    with Pause(1.0)

    "我愣住了。风从程庄路那边吹过来，她额前的碎发被吹乱了，"
    "她伸手去拢，那枚红色发卡在灯光下滑了一下。"
    "我想接话，但舌头像打了结，什么都说不出来。"
    with Pause(1.0)

    "她笑了一下，把围巾裹紧，朝我摆了摆手。"


    voice "audio/voice/lx_05.ogg"
    lx "好的，那我走了。"
    voice "audio/voice/lx_06.ogg"
    lx "你给我打完车就可以走了，记得交车费哦。话说你怎么来了也没有给我带礼物啊。你要知道现在送我礼物要比以后再送划算很多哦。"

    "「嗯。路上小心。」"
    with Pause(1.0)

    hide lx back_and_surprised

    play sound "audio/sfx/car.ogg"
    "然后她钻进车里，车门关上。"
    "车尾灯在深蓝色夜色里拉成一条红线，慢慢弯过街角，消失了。"
    with Pause(1.0)

    "我站在路边，北京十月的风吹得我耳朵发冷。真实荒诞的剧情啊。一下就被这种低级的幽默感打动了。"
    with Pause(0.8)

    "「有缘就会再见面的」"
    with Pause(0.5)

    "我小声念了一句，然后转身，朝着公交的方向慢慢走去。"
    "初冬下起了小雨。"
    with Pause(2.0)

    # 视觉锚点：路灯雨丝 + 远处公交车
    # 雨声 SFX (loop) - 在场景结束时停止
    play sound "audio/sfx/rain.ogg" loop
    "路灯把雨丝照成斜线。远处一辆公交车慢慢驶来。"

    # ============================================================
    # 结束
    # ============================================================
    scene black
    with dissolve

    centered "{size=+10}落日和明天{/size}"
    with Pause(2.0)

    "[[END OF ACT 1]]"
    with Pause(1.5)

    # BGM: act1 结束淡出
    stop music fadeout 2.0
    # 雨声 SFX: 同步淡出
    stop sound fadeout 2.0

    # 结束: 回到章节选择界面
    jump chapter_select
