# 角色定义文件
# LX: 高中同学, Act 1 女主角 (暂用 Rita 角色图作为立绘)

# LX - 高中同学, 姜黄大衣, 红色发卡
define lx = Character("LX",
    who_color="#d4af37",
    what_color="#fff5e1",
    voice_tag="lx"          # voice 文件命名: audio/voice/lx{1,2,3,...}.ogg
)

# Jack - 主角
define jack = Character("Jack", color="#d4d4d4")

# AMI - Act 2 女主角
define ami = Character("Ami", color="#88cc88")

# 旁白 (使用 Ren'Py 内置 narrator 时显式 define 以便统一管理)
define narrator = Character(None, what_color="#cccccc")
