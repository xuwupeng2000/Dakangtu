# 颗粒雨。夜雨山路仍用 bg_eden_night，再 show rain。
image rain_streak = "images/effects/rain_streak.png"

image rain = SnowBlossom(
    "rain_streak",
    count=320,
    border=80,
    xspeed=(280, 520),
    yspeed=(1400, 1900),
    start=0.01,
    fast=True,
)
