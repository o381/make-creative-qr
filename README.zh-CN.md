[English](README.md) · **简体中文**

# Make Creative QR

**让二维码成为画面的一部分。**

一个创意二维码 Agent Skill：将真实扫码内容融入摄影、插画与材料构成，再验证完整成图的可读性。

[开始使用](#开始使用) · [阅读 Skill](skills/make-creative-qr/SKILL.zh-CN.md) · [全部 14 张作品](examples/README.zh-CN.md)

## 精选作品

光影、织物、纸张与刻线，承载同一份信息。点击图片可查看对应案例与完整原图。

<p align="center">
  <a href="examples/README.zh-CN.md#caustic-jelly"><img src="docs/assets/showcase/caustic-jelly.webp" width="560" alt="水杯折射的光，在桌面上游成一只水母。"></a>
</p>
<p align="center">
  <strong>杯底漏出一只水母</strong><br>
  <sub>水杯折射的光，在桌面上游成一只水母。</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.zh-CN.md#jaguar-butterfly"><img src="docs/assets/showcase/jaguar-butterfly.jpg" width="560" alt="睡着的美洲豹身前，豹斑化成展开的蝶翼。"></a>
</p>
<p align="center">
  <strong>豹斑化蝶</strong><br>
  <sub>睡着的美洲豹身前，豹斑化成展开的蝶翼。</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.zh-CN.md#zipper-city"><img src="docs/assets/showcase/zipper-city.webp" width="560" alt="拉开的衣服里，一座小城正亮着灯。"></a>
</p>
<p align="center">
  <strong>拉链里藏着一座城</strong><br>
  <sub>拉开的衣服里，一座小城正亮着灯。</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.zh-CN.md#stamp-sea"><img src="docs/assets/showcase/stamp-sea.jpg" width="560" alt="蜗牛从邮票里牵出了一片海。"></a>
</p>
<p align="center">
  <strong>蜗牛偷走邮票里的海</strong><br>
  <sub>蜗牛从邮票里牵出了一片海。</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.zh-CN.md#shaved-night"><img src="docs/assets/showcase/shaved-night.jpg" width="560" alt="蓝色铅笔屑散落成一角夜色。"></a>
</p>
<p align="center">
  <strong>削下的夜色</strong><br>
  <sub>蓝色铅笔屑散落成一角夜色。</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.zh-CN.md#pencil-whale"><img src="docs/assets/showcase/pencil-whale.jpg" width="560" alt="铅笔投下的影子，游成一头鲸。"></a>
</p>
<p align="center">
  <strong>铅笔的影子游成了鲸</strong><br>
  <sub>铅笔投下的影子，游成一头鲸。</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.zh-CN.md#rain-letter"><img src="docs/assets/showcase/rain-letter.jpg" width="560" alt="靛蓝版画里的雨圈，替纸船写下一封回信。"></a>
</p>
<p align="center">
  <strong>雨替小船写回信</strong><br>
  <sub>靛蓝版画里的雨圈，替纸船写下一封回信。</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.zh-CN.md#flying-score"><img src="docs/assets/showcase/flying-score.webp" width="560" alt="钢琴边的乐谱，飞成了一群鸟。"></a>
</p>
<p align="center">
  <strong>乐谱飞走之后</strong><br>
  <sub>钢琴边的乐谱，飞成了一群鸟。</sub>
</p>

[浏览全部 14 张作品 →](examples/README.zh-CN.md) · [验码与手机实扫记录](examples/verification.json)

公开作品统一指向本仓库。软件验码与手机实扫逐图记录；尚未实扫的作品保留待复核状态。

## 开始使用

将 [Skill 目录](skills/make-creative-qr/) 导入支持目录型 Skill 的 Agent，或提供 [SKILL.zh-CN.md](skills/make-creative-qr/SKILL.zh-CN.md) 作为指令，然后上传真实二维码：

```text
使用 make-creative-qr，创作一张二维码自然融入场景的作品。
先确认我的风格、元素与用途；保留原始扫码内容，
最终检查完整成图的视觉效果、解码结果与分享尺寸。
```

默认文档为英文，提供完整中文版；实际创作按用户的语言交流。

## 创作原则

- **画面独立成立。** 材料有来历，疏密有依据；信息区与周围场景使用连续的视觉语言。
- **内容保持一致。** 以原始扫码内容为基准，不擅自替换、缩短或改写。
- **验证完整成图。** 检查实际文件与分享变体，软件解码与手机实扫分别记录；手机失败则退回修订。

<details>
<summary>工具、验证与内容边界</summary>

Skill 描述能力与验收要求，Agent 使用当前宿主可用的工具。附带的 Python/Node 脚本是一条可选参考路线；创作需要图片查看与生成、可靠读码、导出和文件核验能力。缺少真实验码或必测导出时，只能交付设计候选。

默认软件验收包含七项：实际完整文件，以及宽 480、640、800 像素的 PNG、JPEG 85 版本。每项须读取原始内容且无冲突；裁剪、已知四角辅助和纯码模式不能代替整图验证。用内容摘要或文件哈希绑定最终版本，修改与重新导出后复核。软件成功不能代替手机应用实扫。

首次制作先确认风格、元素与用途，再建立信息导引，依据视觉与解码反馈修订。摄影、插画、动漫、几何与拼贴都可作为载体。非 ASCII 或二进制内容需要可靠的原始字节证据；无法确认输入内容时，不生成替代编码。

私人原码、载荷数据、作品与识别记录不进入公开案例、可复用资产或测试夹具。解码在宿主环境中执行，生成与存储依赖所选服务，本项目不承诺全程离线。

[宿主适配](skills/make-creative-qr/references/tool-adaptation.zh-CN.md) · [可选参考实现](skills/make-creative-qr/references/execution.zh-CN.md)

</details>

---

[贡献指南](CONTRIBUTING.zh-CN.md) · [隐私与安全](SECURITY.zh-CN.md) · [第三方说明](docs/THIRD_PARTY_NOTICES.zh-CN.md)

代码与文档采用 [MIT 许可](LICENSE)。作品与第三方资产的许可另行说明。
