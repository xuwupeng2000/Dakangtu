# 游戏变量定义
# 这些是游戏状态变量，会在第一幕剧情中被使用和修改

# 好感度系统：-10 ~ +10，初始为 0
default ami_love = 0
default jack_love = 0

# 第三幕好感。进章时会清零。≥3 且选择告诉他，才进最好结局。
default act3_love = 0

# 玩家名字
default player_name = "杰克"

# 剧情进度标记
default act1_complete = False
default met_at_airport = False
default helped_with_luggage = False
default shared_coffee = False

# 时间线标记
default current_time = "afternoon"
default current_location = "wellington_airport"
