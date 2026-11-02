# act3.rpy - 第三幕：雨落星河
#
# 立绘用现成半身。车里不换图，把半身放大并顶到画面上沿，
# 脖子以下被对话框挡住。后座里 Ami 在左边，Jack 在右边。
# 湿身和围巾差分还没有，这两处先用原来的表情。
# 循环的雨走 amb，短音效走 sound / hit，避免互相掐掉。

init python:
    renpy.music.register_channel("amb", mixer="sfx", loop=True, tight=True)
    renpy.music.register_channel("hit", mixer="sfx", loop=False)

# === 背景 ===
image bg act3 bedroom = "images/backgrounds/act3/bg_bedroom_night.png"
image bg act3 eden = "images/backgrounds/act3/bg_eden_night.png"
image bg act3 crater = "images/backgrounds/act3/bg_crater_stars.png"
image bg act3 storm = "images/backgrounds/act3/bg_crater_storm.png"
image bg act3 cliff = "images/backgrounds/act3/bg_cliff_rain.png"
image bg act3 car_rain = "images/backgrounds/act3/bg_car_rain.png"
image bg act3 car_stars = "images/backgrounds/act3/bg_car_stars.png"
image bg act3 door = "images/backgrounds/act3/bg_door_night.png"

# === 事件图 ===
image cg act3 cross = "images/cg/act3/cg_southern_cross.png"
image cg act3 phone = "images/cg/act3/cg_phone_grass.png"
image cg act3 kneel = "images/cg/act3/cg_kneel_rain.png"
image cg act3 kiss = "images/cg/act3/cg_kiss_car_rain.png"
image act3 flash = Solid("#ffffff")

# === Jack。tag 是 jack，换表情会换掉上一张。 ===
image jack smile = "images/characters/jack/jack_smile.png"
image jack grin = "images/characters/jack/jack_grin.png"
image jack curious = "images/characters/jack/jack_curious.png"
image jack gentle = "images/characters/jack/jack_gentle.png"
image jack serious = "images/characters/jack/jack_serious.png"
image jack blush = "images/characters/jack/jack_blush.png"
image jack tender = "images/characters/jack/jack_tender.png"
image jack sad = "images/characters/jack/jack_sad.png"
image jack surprised = "images/characters/jack/jack_surprised.png"
# 湿发、摘围巾还没有单独的图。
image jack wet = "images/characters/jack/jack_surprised.png"
image jack wet_smile = "images/characters/jack/jack_smile.png"
image jack noscarf_blush = "images/characters/jack/jack_blush.png"
image jack noscarf_smile = "images/characters/jack/jack_smile.png"

# === Ami 成人装。和 act2 的 ami_smile 不是同一个名字。 ===
image ami adult smile = "images/characters/ami_adult/ami_smile.png"
image ami adult soft_smile = "images/characters/ami_adult/ami_soft_smile.png"
image ami adult shy = "images/characters/ami_adult/ami_shy.png"
image ami adult curious = "images/characters/ami_adult/ami_curious.png"
image ami adult nod = "images/characters/ami_adult/ami_nod.png"
image ami adult pout = "images/characters/ami_adult/ami_pout.png"
image ami adult blush = "images/characters/ami_adult/ami_blush.png"
image ami adult surprised = "images/characters/ami_adult/ami_surprised.png"
image ami adult shock = "images/characters/ami_adult/ami_shock.png"
image ami adult teary = "images/characters/ami_adult/ami_teary.png"

# === Ami 淋湿。下山以后用这套。 ===
image ami soaked smile = "images/characters/ami_soaked/ami_smile.png"
image ami soaked soft_smile = "images/characters/ami_soaked/ami_soft_smile.png"
image ami soaked shy = "images/characters/ami_soaked/ami_shy.png"
image ami soaked nod = "images/characters/ami_soaked/ami_nod.png"
image ami soaked blush = "images/characters/ami_soaked/ami_blush.png"
image ami soaked teary = "images/characters/ami_soaked/ami_teary.png"
image ami soaked shock = "images/characters/ami_soaked/ami_shock.png"

# 山路、火山口：Ami 再小一档，头顶大约到 Jack 下巴，矮一头。
transform half_left:
    zoom 0.85
    xanchor 0.5
    yanchor 0.0
    xpos 500
    ypos 206

transform half_right:
    zoom 0.869
    xanchor 0.5
    yanchor 0.0
    xpos 1420
    ypos 105

transform car_left:
    zoom 1.35
    xalign 0.0
    yalign 0.0
    ypos 85

transform car_right:
    zoom 1.35
    xalign 1.0
    yalign 0.0
    ypos 35

transform act3_poem_roll:
    xalign 0.5
    yanchor 0.0
    ypos 1120
    linear 46.0 ypos -820

init python:
    def act3_return_menu():
        for channel in ("music", "sound", "amb", "hit"):
            renpy.music.stop(channel=channel, fadeout=0.4)
        renpy.full_restart()

    def act3_poem_music():
        if renpy.music.get_playing(channel="music") != "audio/bgm/bgm_act3.ogg":
            renpy.music.play("audio/bgm/bgm_act3.ogg", channel="music", loop=True, fadein=2.0)
        # 诗滚动时没有对白，把完美结局的曲子轻轻托起来。滑条已经调高过就不动。
        if _preferences.get_volume("music") <= 0.55:
            renpy.music.set_volume(2.6, delay=3.0, channel="music")

screen act3_poem():
    modal True
    default show_button = False
    add Solid("#000000")
    frame:
        background None
        padding (40, 0)
        xalign 0.5
        xmaximum 1600
        at act3_poem_roll
        vbox:
            spacing 22
            xalign 0.5
            text "雨落星河" size 52 xalign 0.5 color "#f6f0e4"
            null height 48
            text "雨停了" size 36 xalign 0.5 color "#efe8dc"
            text "玻璃上还挂着昨晚的雨滴" size 36 xalign 0.5 color "#efe8dc"
            text "它没有急着落下" size 36 xalign 0.5 color "#efe8dc"
            text "像是也想再见到你" size 36 xalign 0.5 color "#efe8dc"
            null height 40
            text "南十字还在南边" size 36 xalign 0.5 color "#efe8dc"
            text "你指过的那四颗" size 36 xalign 0.5 color "#efe8dc"
            text "把长夜轻轻折成一段路" size 36 xalign 0.5 color "#efe8dc"
            null height 40
            text "这一夜很短" size 36 xalign 0.5 color "#efe8dc"
            text "短得刚刚好" size 36 xalign 0.5 color "#efe8dc"
            text "好到我舍不得把它讲完" size 36 xalign 0.5 color "#efe8dc"
            null height 40
            text "山还在" size 36 xalign 0.5 color "#efe8dc"
            text "雨还会来" size 36 xalign 0.5 color "#efe8dc"
            text "陡坡上也会再有松动的石台" size 36 xalign 0.5 color "#efe8dc"
            null height 40
            text "只要我还记得你的温柔 就能够走到下一次见面" size 32 xalign 0.5 color "#efe8dc"
            text "当夜晚降临 如果月亮还是又大又圆 我便永远把你的名字放在心上" size 32 xalign 0.5 color "#efe8dc"
            text "我们在来时的路上 把重逢约在同一颗星星下" size 32 xalign 0.5 color "#efe8dc"
            null height 160
    if show_button:
        button:
            xalign 0.5
            yalign 0.86
            background Solid("#6b3a3a")
            hover_background Solid("#8a4a4a")
            padding (40, 16)
            action Function(act3_return_menu)
            text "生日快乐" size 40 color "#fff6e8" xalign 0.5
    if not show_button:
        key "dismiss" action NullAction()
    timer 46.0 action SetScreenVariable("show_button", True)

screen act3_birthday(caption, title=""):
    modal True
    add Solid("#000000")
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 56
        if title:
            text title size 40 xalign 0.5 color "#efe8dc"
        button:
            xalign 0.5
            background Solid("#6b3a3a")
            hover_background Solid("#8a4a4a")
            padding (40, 18)
            action Function(act3_return_menu)
            text caption size 42 color "#fff6e8" xalign 0.5


label act3:

    $ act3_love = 0
    stop amb fadeout 0.2
    stop hit fadeout 0.2

    play music "audio/bgm/bgm_act3_2.ogg" loop fadein 2.0

    scene black
    with Pause(1.0)

    "Act 3：雨落星河"
    with Pause(1.0)

    centered "{size=+10}一夜星雨秋已沉。{/size}"
    with Pause(2.0)

    scene bg act3 bedroom
    with dissolve

    "距上次dating，已经一个星期了。"

    "这一个星期里，我把那晚的聊天记录翻了很多遍。他最后说的那句玩笑话，我看一次笑一次。「有缘就会再见面的。」"

    show ami adult shy at half_left
    with dissolve

    "对话框里，我打了一行字，删掉。又打了一行，又删掉。主动约一个人，原来是这么难的事。"

    "万一他只是客气呢？"

    hide ami
    with dissolve

    ami "你去过伊甸山顶么？那里有很多蘑菇。"

    play sound "audio/sfx/act3_msg_send.wav"

    "按下发送的那一秒，我把手机扣在了枕头上。"

    play sound "audio/sfx/act3_msg_notify.wav"

    "10分钟后，屏幕亮了。"

    jack "我最喜欢看星星了。走起。"

    show ami adult soft_smile at half_left
    with dissolve

    "10分钟。我盯着那个数字，忽然很想知道，这10分钟里他在做什么。"

    scene bg act3 eden
    with dissolve

    "周六晚上八点半，网约车把我放在伊甸山脚下。秋天的风从海那边吹过来，干冷干冷的。路灯昏黄，远处有人在遛狗，城市的声音隔着光秃秃的树影传过来，闷闷的。"

    show jack smile at half_right
    with dissolve

    "Jack 靠在他的车边，深色大衣的领子立着，手里拿着手电。看到我，他站直了。"

    show ami adult curious at half_left
    with dissolve

    ami "你等很久了吗？"

    show jack smile at half_right

    jack "刚到。"

    show ami adult soft_smile at half_left

    "他的引擎盖已经凉透了，车窗上还凝了一层薄薄的雾。骗人。一看就是因为怕费油所以连空调都没舍得开。"

    show ami adult shy at half_left

    "我把脸往大衣领子里埋了埋。幸好天黑，他看不见我在笑。这人面子很薄，知道被我看穿了可能会跳崖。"

    scene bg act3 eden
    with dissolve

    "上山的小路不长，可是很陡。往右一侧头，整个奥克兰就铺在脚下：天空塔亮着红色的光。那些霓虹，圈住了多少人呢。"

    "Jack 走在我外侧。他用手机微弱的光照亮了山路。"

    show ami adult smile at half_left
    with dissolve

    "路太陡，安静太久会尴尬。"

    ami "上周你提到了哲学，我最近看过一本关于哲学的书，你听过加缪么？"

    show jack grin at half_right
    with dissolve

    jack "加缪？存在主义哲学？"

    show ami adult curious at half_left

    ami "加缪。「必须想象西西弗斯是快乐的。」石头滚下来了，还要硬说他快乐。你说这不就是安慰奖吗？"

    show ami adult nod at half_left

    ami "这个世界本来就是荒谬的。承认这一点就够了，没必要再给它颁个安慰奖。"

    show jack smile at half_right

    jack "我倒觉得，这世界是有解的。"

    show ami adult pout at half_left

    ami "你看，乐观的人总是最先开始表演。"

    show jack grin at half_right

    jack "生活是一场表演，就算没有观众，也要演给自己看。"

    "他说得轻飘飘的，像随口抖了个包袱。可是「演给自己看」那半句，他说得太顺了，像是对着镜子练过很多遍。极有可能是在喝醉的时候。"

    show ami adult nod at half_left

    ami "我不喜欢表演的。"

    show jack curious at half_right

    jack "为什么？"

    show ami adult soft_smile at half_left

    ami "因为演的人明明知道自己在演，还非要别人陪着一起信。"

    show jack gentle at half_right

    jack "那台下空了以后呢？剧场里一个人都没有，灯还亮着，你还站不站在你该站的那个位置上？"

    show jack serious at half_right

    jack "没人看的时候就垮下来么？"

    show ami adult curious at half_left

    ami "演给自己看，那也还是在演。观众只剩一个，骗起来更容易。"

    show jack grin at half_right

    jack "恰恰相反。这个观众最难骗，他买的是终身票，中途还不能退场。"

    show ami adult shy at half_left

    "我差点笑出来，忍住了。笑了就输了。"

    "他停下来，靠着木栏杆，指了指山下的灯火。"

    show jack gentle at half_right

    jack "歇会儿吧，我想拍张照。"

    "他的手机一直揣在兜里，根本没拿出来。……他大概是觉得我爬不动了。他可能不知道我是登山爱好者。"

    show ami adult curious at half_left

    ami "加缪还说过一句：真正严肃的哲学问题只有一个，就是自杀。判断人生到底值不值得过。"

    show ami adult nod at half_left

    ami "他给的答案是反抗，而且是不上诉的反抗。不上诉的意思就是：没有人会给你一个解。你说的「有解」，恰恰是他说不能要的东西。"

    show ami adult soft_smile at half_left

    ami "「世界有解」，是最舒服的谎言。比工作、房贷、恋爱都舒服。"

    show jack serious at half_right

    jack "你说的那个解，是答案。石头停在山顶不下来，那叫结果。我说的解，不是结果。"

    show ami adult curious at half_left

    ami "那是什么？"

    show jack smile at half_right

    jack "是一种姿态"

    show jack serious at half_right

    jack "我说的解，是一种源于儒家和道家的东西。是一种生活的姿态。"

    show ami adult nod at half_left

    ami "姿态。你说的是心态的意思么？"

    show jack serious at half_right

    jack "不一样。心态是你心里怎么想，关起门来谁都看不见，也不付出什么。姿态是你做出来的，要花力气，别人看得见，你自己也躲不掉。"

    "他没有再往下说，只是把手机微微抬了一下，光洒落在我前面。"

    show jack gentle at half_right

    jack "比如这个。"

    show ami adult surprised at half_left

    "从山脚到这里，那束光一次都没有离开过我脚下。他没有解释，他是在演示给我看。"

    show ami adult soft_smile at half_left

    "我决定给他挖个坑，挖一个他的「有解」绝对爬不出来的坑。"

    show ami adult curious at half_left

    ami "那你说，加缪版的《红楼梦》会怎么样？"

    show jack grin at half_right

    jack "加缪应该不会写中国诗歌。"

    show ami adult nod at half_left

    ami "没人要你改诗。你看开头那些荣华富贵，元妃省亲，一桌接一桌的宴席。所有人都知道盛筵必散，可他们还是在演。演给宫里看，演给族里看，也演给自己将来被抄家的那一天看。"

    show ami adult pout at half_left

    ami "一整座府都在表演。"

    show jack serious at half_right

    jack "明知道无以为继，今晚还是把酒温上。"

    show ami adult soft_smile at half_left

    ami "那你就是贾母。戏不能停，场面不能散。诚实的客人应该尝一口菜，然后不鼓掌。"

    "我这辈子在饭局上最擅长的事，就是不鼓掌。"

    show jack curious at half_right

    jack "好，那抄家呢？"

    show ami adult nod at half_left

    ami "抄家才是重点。你的「有解」，就结束在这一回。"

    show jack serious at half_right

    jack "抄家不是解，也不是报应，它什么都解释不了。就是荒诞推开了大门。蹉跎一个人最高明的不是让他一无所有，而是让他拥有过，再失去。"

    show jack gentle at half_right

    jack "所以加缪不会写抄家那天。他会写第二天早上：箱子都贴了封条，可总还得有人决定，接下来怎么办。"

    show jack grin at half_right

    jack "我是欣赏探春的姿态的。她明知道结果，还是一笔一笔查账。明知不可为而为之。"

    show ami adult soft_smile at half_left

    ami "那我站宝玉。出家，是那本书里唯一诚实的出口。我要是坐在那桌宴席上，也会起身悄悄的走掉。"

    show jack gentle at half_right

    jack "可走掉也是在追一个结果。一个空舞台，一个再也没人要求你演的地方。"

    show jack serious at half_right

    jack "加缪不会让他走上那条和尚的路。他会把宝玉留在抄家第二天早上的院子里。"

    show ami adult shy at half_left

    "做什么呢？"

    show ami adult nod at half_left

    ami "那加缪的红楼梦，就没有「白茫茫一片大地真干净」了。那个结尾太干净，干净得像一场救赎，谁都被洗白了。说到底，也是安慰奖。"

    show jack gentle at half_right

    jack "嗯，没有白茫茫。只有第二天、第三天，和一些流水账。"

    show ami adult curious at half_left

    ami "可你发现没有？你把每一个人都留在了抄家后的废墟上。"

    show ami adult nod at half_left

    ami "那我换个说法。如果「解」只剩下一个姿态，石头永远停不住，那你不过是给失败换了个名字。"

    show ami adult soft_smile at half_left

    ami "你偷换概念。"

    "他愣了一下，然后笑出了声，他手中的光也跟着他的身影摇曳。"

    show jack smile at half_right

    jack "算你赢。"

    show jack grin at half_right

    jack "反正我和生活，只有一个会幸存下来。我打算从生命长度上打败一切人。"

    show ami adult surprised at half_left

    "他是笑着说的，像一句段子。可是前半句和后半句之间，他停了半秒。「长度」是段子，「只有一个会幸存下来」是真的。"

    show ami adult soft_smile at half_left

    ami "……你那不是加缪。加缪不跟生活打仗。"

    show jack smile at half_right

    jack "我逗你玩呢，你那么认真干嘛？"

    show ami adult teary at half_left

    "他认输认得那么快，脚下却一步都没有退。一个什么样的人，才需要把活着说成一场仗，还要笑着说给别人听？"

    "最后一段是几级高高的台阶，边缘被人踩得有点松。Jack 先上去，回身朝我伸出手。他完全不知道，会爬山的人是我。"

    show jack gentle at half_right

    jack "来。"

    menu:
        "把手放进他的手心。":
            $ act3_love += 2
            jump act3_hand_a

        "笑着摇头：「我自己可以，你在上面等我。」":
            $ act3_love += 1
            jump act3_hand_b

        "「早知道这么远，我就约在山脚看了……」":
            jump act3_hand_c


label act3_hand_a:

    "他的手很暖，掌心有一点粗糙。他轻轻一拉我就上去了。可上去以后，他没有马上松开。"

    show jack blush at half_right
    with dissolve

    jack "……你的手好凉。"

    show ami adult blush at half_left

    "坡走完了。他没提松手，我也没提。我们就这么走，假装前面还有松动的台阶。"

    show ami adult shy at half_left

    "放开以后，掌心那一点热还在。我把手插进大衣口袋，免得它写在脸上。"

    show ami adult blush at half_left

    "心跳快得不像话。大概是爬坡爬的。"

    jump act3_crater


label act3_hand_b:

    show jack gentle at half_right

    "他真的就站在台阶顶上等我，手一直半伸着没收回去。没人要他伸着，他还是伸着。我想，这大概就是他说的姿态。"

    jump act3_crater


label act3_hand_c:

    show jack smile at half_right

    jack "那就慢慢走。星星又不会跑。"

    "明明是我约的他，现在倒像他在哄我。我有点后悔说了那句话。"

    jump act3_crater


label act3_crater:

    scene bg act3 crater
    with dissolve

    "山顶是一圈火山口的边缘。脚下那个巨大的碗形凹地黑沉沉的，长满了草；再远一点，是整座城市的灯火。"

    show jack grin at half_right
    with dissolve

    jack "你看天上的星星么，有一颗就是你，我一眼就能看出来。"

    show ami adult curious at half_left
    with dissolve

    ami "怎么分辨？"

    show jack gentle at half_right

    jack "你的那颗，是那个大大的圆圆的。"

    show ami adult nod at half_left

    ami "那个是月亮。"

    show jack grin at half_right

    jack "对啊，所以我说一眼就能看出来。整片天最亮的那个。"

    "我就那么看着他。三秒钟里，他的眼睛没有回到天上。"

    show ami adult curious at half_left

    ami "你根本没在看天。"

    show jack gentle at half_right

    jack "在看啊。"

    show ami adult shy at half_left

    "他的眼睛还在我脸上。那句「在看啊」，说的不是星星。"

    "他又撑了两秒，自己先笑出了声。"

    show ami adult soft_smile at half_left

    "他当然知道那是月亮。这笨拙的玩笑从头到尾都不是说给星星听的，是冲着我来的。"

    show jack smile at half_right

    jack "我在奥克兰住了十几年，从来没上来看过一次。"

    show ami adult soft_smile at half_left

    ami "其实比起西西弗斯，我更喜欢《局外人》里的默尔索。"

    show jack curious at half_right

    jack "那个妈妈去世了都不哭的人？"

    show ami adult nod at half_left

    ami "对。整本书只有他是诚实的。葬礼上所有人都在演悲伤，只有他不演。"

    show ami adult soft_smile at half_left

    ami "他什么都不要。不要人懂，不要人原谅。安安静静地活着，就够了。"

    show jack serious at half_right

    jack "可他最后被判死刑，真的是因为不哭吗？我觉得，是因为整个法庭里，没有一个人站在他旁边。"

    show jack gentle at half_right

    jack "没有爱的诚实，也只是另一块石头。加缪后来写《鼠疫》，写的是一整座城的人一起扛，不是一个人冷冷地站在太阳底下。"

    show ami adult pout at half_left

    ami "你又要说姿态了。"

    show jack grin at half_right

    jack "被你抢了台词。"

    show jack tender at half_right

    jack "……好，不开玩笑了。诚实地说，我需要人。演给自己看，演久了，也会想有一个人坐在台下，看一眼。"

    show ami adult shy at half_left

    "这是他今晚第一句没有包装的话。那层玩世不恭，终于滑下来了一角。"

    "他每一次跟我吵，绕来绕去，最后都绕回人和人之间。他不是在跟加缪辩论，他是在跟我说话。"

    scene cg act3 cross
    with dissolve

    "Jack 没有说话。过了一会儿，他站到我身后，抬起手臂，越过我的肩膀，指向南边的天空。"

    "羊毛大衣贴上我的后背。他的心在怦怦的跳。这天降异象啊，这是什么天象啊，这一定是天意啊，这是天意让我和Jack在一起啊。这星星比月亮都要大了。"

    "我盯着他指的方向，一步都没往前迈。这真是我见过最假的南十字星，比月亮还大。我的天。"

    ami "……你离太近了，我看不清你指的是哪颗。"

    jack "那就先看这颗。我的手不放下，你就还认得。"

    jack "看那四颗，像风筝一样的，是南十字星。把长的那条边延长四倍半，就是正南方。在这里迷路的人，都靠它找方向。"

    jack "以后你再看到它，它就不算陌生的星星了。如果你真的看到这样的星星那一定是UFO到访地球了。"

    scene bg act3 crater
    with dissolve

    show jack gentle at half_right
    show ami adult shy at half_left
    with dissolve

    "我们并排站在火山口边，谁都没有说话。山下的灯火和头顶的星星之间，隔着一层薄薄的秋夜。"

    show ami adult curious at half_left

    "我在心里把这一晚过了一遍：一段陡坡，一场关于加缪的对话，一座被抄了的大观园，还有一颗其实是月亮的星星。每一件都很荒唐，可每一件我都觉得有意思。这不对劲。"

    show ami adult nod at half_left

    ami "我有个假设。和喜欢的人在一起，什么都会感到很有趣。爱可能只是生活的一层滤镜。"

    show ami adult blush at half_left

    "话一出口我就后悔了。「喜欢的人」这四个字，根本不该出现在一个假设里。"

    "Jack 没有笑。他沉默了一会儿。"

    show jack serious at half_right

    jack "我不觉得是滤镜。爱是生活追求的本质。"

    show jack tender at half_right

    jack "它之所以让生活变得有趣，是因为那本来就是生活应该去追寻的轨迹。不是后来贴上去的颜色，是路本来的样子。"

    show jack gentle at half_right

    jack "所以它也不是一种单纯的心情，而是一系列动作，只不过这些动作包括了大量的心理活动。"

    show ami adult soft_smile at half_left

    ami "爱情是一种脑内的有机化学反应。"

    show jack gentle at half_right

    jack "嗯。你学过有机化学吧。你大概挂科了。"

    show ami adult shy at half_left

    "他没有反驳我，也没有说服我，只是站在那里。"

    show ami adult shy at half_left

    play sound "audio/sfx/act3_wind.wav"

    "山顶的风突然大了，奥克兰秋夜的寒冷从大衣领口灌进去，直往脖子里钻。我下意识缩了缩肩膀。"

    "出门太急，围巾落在了玄关的椅子上。我以为他不会注意到。"

    "下一秒，他解下自己的围巾，绕过我的大衣领子。围巾上还带着他的体温。"

    "绕到第二圈的时候，他的指节擦过我的下颌。我们都停了一下。"

    show jack noscarf_blush at half_right

    jack "……围好了。"

    show ami adult blush at half_left

    "我的脉搏就在他手指底下。更糟的是，我把下巴抬高了一点，好让他绕得顺。我是自己把脖子送过去的。"

    show jack noscarf_smile at half_right

    jack "围着。我不冷，我北方人，脖子抗冻。"

    show ami adult soft_smile at half_left

    "他说完，悄悄把大衣领子往上拽了拽。北方人看来也没那么抗冻。"

    stop music fadeout 1.5

    scene bg act3 storm
    with dissolve

    play sound "audio/sfx/act3_thunder_far.wav"

    "不知道什么时候，西边的城市灯火被一堵灰黑色的雨墙吞了进去。星星一颗一颗熄灭，快得像有人在天上拉上了帘子。"

    play amb "audio/sfx/act3_rain_heavy.wav" fadein 1.2

    "第一滴雨落在我手背上，冰凉。然后是第二滴、第三滴，接着整座山都响了起来。"

    scene bg act3 eden
    show rain
    with dissolve

    "奥克兰的天气一向如此多变。一场大雨倾盆而下。"

    scene bg act3 cliff
    with dissolve

    scene act3 flash
    with Dissolve(0.05)

    play sound "audio/sfx/act3_thunder.wav"

    scene bg act3 cliff
    with Dissolve(0.15)

    play hit "audio/sfx/act3_phone_drop.wav"

    "一道闪电劈下来，照亮了整个火山口。我吓得一缩，攥在手里的手机滑了出去，在泥地上弹了两下，卡在了坡沿的草丛里。屏幕还亮着。"

    scene cg act3 phone
    with dissolve

    "那里面有一张截图，是 2013 年一个陌生人发给我的第一条私信，末尾跟着一个笨拙的笑脸。我换了三部手机，每次都先把那张图存过去。"

    "那个陌生人，现在就站在我旁边。"

    jump act3_cliff_choice


label act3_cliff_choice:

    scene bg act3 cliff
    with dissolve

    show jack wet at half_right
    with dissolve

    jack "你的手机！我去捡，就在那儿，两步路。"

    menu:
        "一把拉住他：「不要了！你比它重要。」":
            $ act3_love += 1
            jump act3_key_a

        "「……那里面，有对我很重要的东西。」":
            jump act3_bad


label act3_key_a:

    show ami soaked teary at half_left
    with dissolve

    "我抓住他的袖子，抓得那么紧，连我自己都吓了一跳。雨水顺着他的头发往下淌，他看着我，愣了两秒。"

    show jack gentle at half_right

    jack "……好，听你的。"

    scene bg act3 eden
    show jack gentle at half_right
    show ami soaked teary at half_left
    show rain
    with dissolve

    "他反手握住我的手，十指扣紧。剩下的一路，再也没有松开过。"

    scene bg act3 car_rain
    with dissolve

    play sound "audio/sfx/act3_car_door.wav"
    stop amb fadeout 0.3
    play music "audio/bgm/bgm_act3_2.ogg" loop fadein 2.0

    "车门「砰」地关上，世界一下子被隔在了外面。雨砸在车顶上，发出咚咚的响声。"

    show jack wet_smile at car_right
    show ami soaked smile at car_left
    with dissolve

    "我们俩浑身湿透，喘着气看着对方，然后同时笑了出来。"

    show ami soaked smile at car_left

    ami "我约你看星星，结果约来一场暴雨。"

    show jack wet_smile at car_right

    jack "挺好的。这样我就能记一辈子了。"

    "Jack 把暖风开到最大，又从后座翻出一条毯子，抖开，盖在我腿上。他的大衣湿得发沉，头发还在往下滴水。"

    "他的围巾还在我脖子上，湿透了，可贴着皮肤的那一层还是暖的。"

    show jack gentle at car_right

    jack "雨太大了，现在开车不安全。等一会儿吧。"

    "车窗被雨水糊成一片，山下的灯火化成一团一团晕开的光。车里只剩下仪表盘幽幽的蓝光。"

    show ami soaked blush at car_left

    "这么小的空间。我能听见他的呼吸，也能听见自己的心跳。分不清哪个更大声。"

    "毯子底下，我的膝盖碰到了他的膝盖。两个人都没有挪开。"

    show jack sad at car_right

    jack "你手机没了……"

    "他低着头，手指无意识地拨着后座边上的一道缝线。我忽然发现，这个在餐厅里吹了一晚上创业故事的人，原来也会紧张。"

    menu:
        "看着他，告诉他手机里那张截图的事。":
            if act3_love >= 3:
                jump act3_best
            else:
                jump act3_n0

        "移开视线：「雨小一点，我们就回去吧。」":
            jump act3_n1


label act3_best:

    show ami soaked soft_smile at car_left

    ami "那个手机里，有一张截图。2013 年，你发给我的第一条私信，你说我回帖末尾那个笑脸很可爱。"

    show ami soaked teary at car_left

    ami "你说你翻不到我们的聊天记录了。我这里一直有。我换了三部手机，每一次，都先把那张图存过去。"

    ami "刚才它掉下去的时候，我一点都没犹豫。因为发那条消息的人，现在就坐在我旁边。"

    show jack surprised at car_right

    "他怔怔地看着我，很久都没有说话。"

    show jack serious at car_right

    jack "……Ami"

    jack "那天给你发了信息之后，我想了很久，怎么才能再约你出来。假设了很多种方法，全删了。"

    show jack blush at car_right

    jack "你发蘑菇那条的时候，我看了十分钟。不是不想回。是怕回得太快，你就知道我有多想来。"

    "雨声好像一下子变远了。他伸出手，把我额前一缕湿透的碎发拨到耳后。指尖碰到我脸颊的时候，在微微发抖。"

    show jack tender at car_right

    jack "……可以吗？"

    hide jack
    hide ami
    with dissolve

    "我没有回答，只是闭上了眼睛。"

    scene cg act3 kiss
    with dissolve

    "雨还在下。整个世界只剩下车顶的雨声，和一个很轻、很轻的吻，像星星落在水面上。"

    scene bg act3 car_stars
    with dissolve

    stop amb fadeout 1.2
    play music "audio/bgm/bgm_act3.ogg" fadein 2.0 loop

    "不知道过了多久，雨停了。后挡玻璃上的水珠一颗一颗滑下去，云散开了，城市的灯火上面，星星又回来了。"

    show jack tender at car_right
    show ami soaked soft_smile at car_left
    with dissolve

    jack "你看，南十字星。"

    show ami soaked soft_smile at car_left

    ami "嗯。现在我认得它了。"

    show jack tender at car_right

    jack "以后想看星星，不用你约。我来。"

    scene black
    with dissolve

    window hide
    $ act3_poem_music()
    call screen act3_poem
    window auto

    stop music fadeout 2.0
    stop amb fadeout 0.5
    stop sound fadeout 0.5

    return


label act3_n0:

    show ami soaked soft_smile at car_left

    "截图的事已经到了嘴边。可看着他疲惫的侧脸，我又咽了回去：「……没事，雨小一点我们就回去吧。」"

    jump act3_neutral


label act3_n1:

    show ami soaked nod at car_left

    ami "雨小一点，我们就回去吧。"

    jump act3_neutral


label act3_neutral:

    show jack gentle at car_right

    "「好。」他好像还想说什么，最后只是把暖风又调高了一格。"

    play hit "audio/sfx/act3_wiper.wav"

    "半小时后雨小了，车慢慢开出伊甸山。雨刷一下一下地刮，像钟摆。窗外的城市被雨洗得发亮。"

    show ami soaked shy at car_left

    "一路上我们都没怎么说话，可是一点也不尴尬。他偶尔看我一眼，我就假装睡着，等他转回去，再偷偷睁开眼。"

    scene bg act3 door
    with dissolve

    "车停在我家门口时，已经快十二点了。路灯下的积水亮晶晶的，倒映着一角重新放晴的夜空。"

    show jack gentle at car_right
    with dissolve

    jack "到了。快进去，别感冒，改天再见。"

    hide jack
    hide ami
    with dissolve

    "我下了车，走到门口，回头看。他的车还停在原地没走，车灯一直亮着，等我进了门、开了灯。"

    scene black
    with dissolve

    window hide
    call screen act3_birthday("生日快乐！！！", "【次好结局 🐰 改天再见】")
    window auto

    stop music fadeout 2.0
    stop amb fadeout 0.5
    stop sound fadeout 0.5

    return


label act3_bad:

    show ami soaked teary at half_left
    with dissolve

    ami "……那里面，有对我很重要的东西。"

    show jack wet_smile at half_right

    jack "那就等我。"

    stop music fadeout 0.5

    "他把自己的手机塞进我手里，侧过身，一步一步挪向火山口的坡沿。雨水顺着草往下淌，整片斜坡都在发亮。"

    "他蹲下去，伸长手臂。指尖碰到了手机。"

    show jack wet_smile at half_right

    jack "拿到了！"

    hide jack
    with Dissolve(0.15)

    play hit "audio/sfx/act3_ground_give.wav"
    with hpunch

    "就在那一瞬间，他脚下那块被雨泡软的泥土，无声地塌了下去。"

    show ami soaked shock at half_left
    with dissolve

    ami "Jack——！"

    scene act3 flash
    with Dissolve(0.05)

    scene bg act3 cliff
    with Dissolve(0.2)

    "我扑过去，指尖擦过他的袖口。只差一点点。只差一点点。"

    "漆黑的火山口和铺天盖地的雨。没有人回答。"

    scene cg act3 kneel
    with dissolve

    "我跪在雨里攥着手机，一遍一遍喊他的名字。雨声太大了，大到我听不见自己的声音。"

    "我约他来看星星，我想让他陪我把这片天认熟。可是这片天上，从今以后，又多了一颗我找不到的星星。下雨天到野山看星星不如在家刷剧。有些浪漫是会死人的。"

    scene black
    with dissolve

    centered "{size=+10}【最坏结局 ☠️ 坠落的星】有些东西，比回忆更重要。你把天才都给作没了。{/size}"
    with Pause(2.0)

    jump act3_cliff_choice
