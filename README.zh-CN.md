<p align="right"><sub><a href="README.md">English</a> · <strong>简体中文</strong></sub></p>

<h1 align="center">Make Creative QR</h1>

<p align="center"><em>让二维码成为画面的一部分。</em></p>

<p align="center">
  一个创意二维码 Agent Skill。<br>
  将真实扫码内容融入画面，并验证整图。
</p>

<p align="center">
  <a href="#光影有了生命">精选作品</a> ·
  <a href="#开始创作">开始创作</a> ·
  <a href="examples/README.zh-CN.md">完整作品集</a>
</p>

<br>

<h3 align="center"><a name="光影有了生命"></a>光影有了生命</h3>

<p align="center"><em>一杯水，一支笔，另一种观看的方式。</em></p>

<p align="center">
  <a href="examples/README.zh-CN.md#caustic-jelly"><img src="docs/assets/showcase/caustic-jelly.webp" width="560" alt="水杯折射的光，在桌面上游成一只水母。"></a><br>
  <sub>杯底漏出一只水母</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.zh-CN.md#pencil-whale"><img src="docs/assets/showcase/pencil-whale.jpg" width="560" alt="铅笔投下的影子，游成一头鲸。"></a><br>
  <sub>铅笔的影子游成了鲸</sub>
</p>

<br>

<h3 align="center">小物件，另一个世界</h3>

<p align="center"><em>从日常的一处细节，走进另一个世界。</em></p>

<p align="center">
  <a href="examples/README.zh-CN.md#zipper-city"><img src="docs/assets/showcase/zipper-city.webp" width="560" alt="拉开的衣服里，一座小城正亮着灯。"></a><br>
  <sub>拉链里藏着一座城</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.zh-CN.md#stamp-sea"><img src="docs/assets/showcase/stamp-sea.jpg" width="560" alt="蜗牛从邮票里牵出了一片海。"></a><br>
  <sub>蜗牛偷走邮票里的海</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.zh-CN.md#shaved-night"><img src="docs/assets/showcase/shaved-night.jpg" width="560" alt="蓝色铅笔屑散落成一角夜色。"></a><br>
  <sub>削下的夜色</sub>
</p>

<br>

<h3 align="center">画面开始流动</h3>

<p align="center"><em>豹斑化蝶，音符飞走，雨水写信。</em></p>

<p align="center">
  <a href="examples/README.zh-CN.md#jaguar-butterfly"><img src="docs/assets/showcase/jaguar-butterfly.jpg" width="560" alt="睡着的美洲豹身前，豹斑化成展开的蝶翼。"></a><br>
  <sub>豹斑化蝶</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.zh-CN.md#flying-score"><img src="docs/assets/showcase/flying-score.webp" width="560" alt="钢琴边的乐谱，飞成了一群鸟。"></a><br>
  <sub>乐谱飞走之后</sub>
</p>

<br>

<p align="center">
  <a href="examples/README.zh-CN.md#rain-letter"><img src="docs/assets/showcase/rain-letter.jpg" width="560" alt="靛蓝版画里的雨圈，替纸船写下一封回信。"></a><br>
  <sub>雨替小船写回信</sub>
</p>

<br>

<p align="center"><a href="examples/README.zh-CN.md">浏览全部 14 张作品 →</a></p>

<p align="center"><sub><a href="examples/verification.json">软件验码与手机实扫记录</a><br>尚未实扫的作品保留待复核状态；公开作品指向本仓库。</sub></p>

<br>

<h3 align="center"><a name="开始创作"></a>开始创作</h3>

将 [Skill 目录](skills/make-creative-qr/) 导入支持目录型 Skill 的 Agent，或让它读取 [Skill 正文](skills/make-creative-qr/SKILL.zh-CN.md)。启用后直接上传二维码，也可提供待编码的准确链接或文字。AI 会沿用已有偏好，缺少偏好时自主选题，完成创作、修订和整图验码，无需重复交代流程。

后续用简短指令即可：

```text
换一个创意。
保留创意，修复扫码。
参考这张图的风格。
```

默认文档为英文，提供完整中文版；实际创作按用户的语言交流。

<details>
<summary>创作方法、验码与隐私</summary>

画面先独立成立：材料有来历，疏密有依据，信息区与周围场景使用连续的视觉语言。保留原始扫码字节，不擅自替换、缩短或改写；完整成图与分享变体都要验证，手机实扫失败则退回修订。

Skill 描述能力与验收要求，Agent 使用当前宿主可用的工具。附带的 Python/Node 脚本是一条可选参考路线；创作需要图片查看与生成、可靠读码、导出和文件核验能力。缺少真实验码或必测导出时，只能交付设计候选。

默认软件验收包含七项：实际完整文件，以及宽 480、640、800 像素的 PNG、JPEG 85 版本。每项须读取原始内容且无冲突；裁剪、已知四角辅助和纯码模式不能代替整图验证。用内容摘要或文件哈希绑定最终版本，修改与重新导出后复核。软件成功不能代替手机应用实扫。

沿用已有风格、元素与用途，缺少偏好时自主选方案，再建立信息导引，依据视觉与解码反馈修订。摄影、插画、动漫、几何与拼贴都可作为载体。非 ASCII 或二进制原码需要可靠的原始字节证据；无法确认输入内容时，不生成替代编码。

私人原码、载荷数据、作品与识别记录不进入公开案例、可复用资产或测试夹具。解码在宿主环境中执行，生成与存储依赖所选服务，本项目不承诺全程离线。

[宿主适配](skills/make-creative-qr/references/tool-adaptation.zh-CN.md) · [可选参考实现](skills/make-creative-qr/references/execution.zh-CN.md)

</details>

<br>

<p align="center"><sub>
  <a href="CONTRIBUTING.zh-CN.md">参与贡献</a> ·
  <a href="SECURITY.zh-CN.md">隐私与安全</a> ·
  <a href="docs/THIRD_PARTY_NOTICES.zh-CN.md">第三方说明</a> ·
  <a href="LICENSE">MIT 许可</a>
</sub><br><sub>MIT 适用于代码与文档；作品与第三方资产的许可另行说明。</sub></p>
