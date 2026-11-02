# chapter_select.rpy - 章节选择界面
#
# 用户点击主菜单的"开始游戏"后，会跳转到此界面。
# 灰色背景 + 两个角色立绘（左右各一），点击进入对应 act。
# 角色立绘占屏幕 80% 高度。
#
# 关键机制：
# - tag menu：让本屏幕与 main_menu 互斥（同一时间只能显示一个）
# - on "show" event：显示本屏幕时主动 hide main_menu（保险）
# - 按钮 action 同时 Hide("main_menu") + Jump：确保跳转后 main_menu 不会再回来
#
# 需要准备的图片（占位符，用户后续替换）：
# - images/character_act1.png  # 占位符：act 1 角色（建议 LX）
# - images/character_act2.png  # 占位符：act 2 角色（建议 Jack）
# 说明：角色立绘建议为竖版全身图（高度大于宽度），如 1080x1920。
#      代码会按 80% 屏幕高度缩放，宽度自动按比例缩放。

# ============================================
# 角色立绘占位符声明
# ============================================
image character_act1 = "images/characters/rita/sprite_neutral-emote_0004.png"  # act 1 角色立绘
image character_act2 = "images/characters/ami/ami_smile.png"  # act 2 角色立绘

# ============================================
# 角色大小 transform
# ============================================
transform character_select_size:
    # 占屏幕 80% 高度，按比例缩放宽度
    ysize 0.8
    fit "contain"
    xanchor 0.5
    yanchor 0.5

# ============================================
# 章节选择屏幕
# ============================================
screen chapter_select():
    # 关键 1: 让本屏幕与 main_menu 互斥
    tag menu

    # 关键 2: 显示本屏幕时，主动隐藏 main_menu（保险，防止任何残留）
    on "show" action Hide("main_menu")

    # 灰色背景
    add Solid("#666666")

    # 左侧角色（点击进入 act 1）
    imagebutton:
        idle "character_act1"
        hover "character_act1"
        xalign 0.25
        yalign 0.5
        # 关键 3: 跳转前显式 hide main_menu
        action [Hide("main_menu"), Jump("act1")]
        at character_select_size

    # 右侧角色（点击进入 act 2）
    imagebutton:
        idle "character_act2"
        hover "character_act2"
        xalign 0.75
        yalign 0.5
        # 关键 3: 跳转前显式 hide main_menu
        action [Hide("main_menu"), Jump("act2")]
        at character_select_size

    # 第三章入口。左右两张立绘仍是第一幕、第二幕。
    textbutton _("第三章  雨落星河"):
        xalign 0.5
        yalign 0.06
        action [Hide("main_menu"), Jump("act3")]

    # 返回主菜单按钮
    textbutton _("返回主菜单"):
        xalign 0.5
        yalign 0.95
        # 关键 4: 返回时显式 show main_menu
        action [Show("main_menu"), Return()]

# ============================================
# 章节选择入口标签
# 从主菜单的"开始游戏"按钮跳转到这里
# ============================================
label chapter_select:
    call screen chapter_select
    return
