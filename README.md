# 大康兔 Dakangtu

一个用于**学习 + 测试 ComfyUI 图像生成工作流**的 2D Galgame 项目。

游戏本体基于 **Ren'Py** 引擎编写，剧情围绕两段跨越数十年的异地重逢展开。所有的角色立绘、场景背景、封面图均由本地 ComfyUI 流水线生成，是研究 SDXL / Z-Image / Anima / Wan 2.2 等不同 DiT 架构在视觉小说场景下表现差异的实验载体。

> 当前版本 **1.5**。Act 1「落日和明天」、Act 2「相见有期」、Act 3「雨落星河」都已进游戏。主菜单从「开始第一章」（Act 2）和「开始第二章（生日快乐）」（Act 3）进入。

在浏览器里玩：[xuwupeng2000.itch.io/dakangtu](https://xuwupeng2000.itch.io/dakangtu)

---

## 画面

第三幕的场景和 CG，直接用 `game/images/` 里的原图。

<p align="center">
  <img src="game/images/cg/act3/cg_southern_cross.png" alt="山顶，南十字" width="900">
  <br>山顶，南十字
</p>

<p align="center">
  <img src="game/images/backgrounds/act3/bg_eden_night.png" alt="月下山路" width="440">
  <img src="game/images/backgrounds/act3/bg_bedroom_night.png" alt="夜里看消息" width="440">
  <br>月下山路 · 夜里看消息
</p>

<p align="center">
  <img src="game/images/cg/act3/cg_kneel_rain.png" alt="雨里" width="440">
  <img src="game/images/backgrounds/act3/bg_car_stars.png" alt="雨停后的后座" width="440">
  <br>雨里 · 雨停后的后座
</p>

<p align="center">
  <img src="game/images/cg/act3/cg_kiss_car_rain.png" alt="后座" width="900">
  <br>后座
</p>

<p align="center">
  <img src="game/images/characters/ami_adult/ami_smile.png" alt="Ami" width="280">
  <img src="game/images/characters/jack/jack_smile.png" alt="Jack" width="280">
  <br>Ami · Jack
</p>

---

## 特性

- 纯本地图像生成（无 API 调用）
- 多模型 / 多 LoRA 横向对比工作流
- 模块化章节选择（点角色头像进入对应 Act）
- 角色一致性方案：Rembg 去背 + Anima 风格迁移
- 项目内含 12+ 个 ComfyUI 工作流 JSON，附带 schema 修复脚本

---

## 技术栈

| 类别 | 工具 / 框架 | 用途 |
|---|---|---|
| 游戏引擎 | Ren'Py 8.5.3 | 视觉小说运行时 |
| 界面 | Ren'Py Screen Language | 主菜单、章节选择、对话 |
| 图像生成 | ComfyUI Desktop | 本地 SD 工作流调度 |
| 背景移除 | ComfyUI `rembg` + `isnet-anime` | 角色立绘去背 |
| Inpainting | ComfyUI GroundingDINO + SAM2 | 局部精修 |

---

## 使用的生成模型

### 基础模型 (UNet / Checkpoint)

| 模型 | 架构 | 参数量 / 精度 | 角色 | 备注 |
|---|---|---|---|---|
| `z_image_turbo_bf16.safetensors` | DiT | bf16 量化 | 背景 / Inpainting | 主用模型，速度优先 |
| `waiIllustriousSDXL_v170.safetensors` | SDXL | fp16 | 像素风对比测试 | 经典 SDXL baseline |
| Wan 2.2 (high + low) | DiT | fp8 | 动态背景（实验）| 视频扩散模型 |
| Anima (Qwen3 4B + Flux) | DiT | mixed | 角色 / 封面 | 一致性表现最佳 |

### 文本编码器 (Text Encoder)

| 模型 | 类型 | 搭配底模 |
|---|---|---|
| `qwen_3_4b.safetensors` | `qwen_image` | z-image / Anima |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `umt5` | Wan 2.2 |
| (内置于 CheckpointLoader) | sdxl | waiIllustriousSDXL |

### VAE

| 模型 | 搭配 |
|---|---|
| `ae.safetensors` | z-image / Anima |
| (内置于 CheckpointLoader) | SDXL / Wan 2.2 |

### 关键参数

| 参数 | z-image | Anima | SDXL | Wan 2.2 |
|---|---|---|---|---|
| Steps | 10 | 10 | 25 | 20 |
| CFG | 1.0 | 1.0 | 7.0 | 5.0 |
| Sampler | euler | euler | euler_ancestral | euler |
| Scheduler | simple | simple | karras | normal |
| Denoise (img2img) | 0.45-0.55 | 0.45-0.55 | 0.6-0.8 | — |
| Denoise (Inpainting) | 0.6-0.8 | — | — | — |

---



## 快速开始

```bash
# 1. 启动 Ren'Py 项目
renpy Dakangtu/

# 2. 跑工作流（ComfyUI Desktop）
#    Load workflows/galgame_bg_anima_v5_*.json → Queue Prompt

```

---

## 已知限制

- 仅在 Windows + ComfyUI Desktop 验证
- 语音资源为 2019 年录制的老素材，未重新生成
- 部分工作流 JSON 存在老版 API 格式，加载时由 ComfyUI 自动转换

---

## License

个人学习项目，未授权商用。
