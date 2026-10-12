# 信息导引与材质编辑

按宿主现有工具实施主流程。信息导引可使用图层、遮罩、节点、栅格或矢量；本文件的脚本、资产和参数属于可选参考路线，不要求其他 Agent 安装或调用。只有主流程要求的结果与验收保持一致。

## 技术起点及其边界

用本次原内容生成精确矩阵，再设计其可见材料。`assets/particle-locators.json` 仅含三处功能区标准化几何与色阶，不含任何用户数据矩阵或链接。默认颗粒方法使用 M 纠错、至少版本 5、24 像素模块单位、6 模块留白及 0.2 载体密度；0.15–0.3 可作实验范围，不保证通过，也不是自然构成配方。

`render_guide.py` 的固定遍历合并适合单款基线，不适合整套作品共用终稿。新款可用新 mask/版本和 `render_organic_guide.py` 的合法随机横纵分组；构成差异仍须由材料行为和场景关系决定。深色颗粒、浅色空腔导引存在软件通过实例，不能据此推定成图、反色或任意角度成功。

定位区用材料表达必要明暗，不能机械删除。默认软边轮廓可能变成三处独有的灰团或清空区；相同材质也可能仍然突兀。按 [主工作流](../SKILL.md) 先审查整个分布，不把定位模板的可扫性当成外观合格。

改动灰度轮廓、把暗核拆成碎屑、添加细屑或连接形状都属于须复测的实验。相似平均灰度不能证明保真；变更数据区聚合轮廓也不能为掩护定位区随意引入编码错误。提高纠错不能保证功能信息缺失后还能检测。

## 场景编辑提示词

先按主工作流固定事件、材料形成机制和构成。当前导引图必须已按该构成安排比例及位置；不要用提示词为不合适的固定方阵找理由。按宿主支持的引用方式标记“信息导引”和“视觉参考”，后者如存在仅提供审美；不假定固定图片编号或顺序。

```text
Create [EVENT OR VISUAL RULE] in [STYLE AND PALETTE].
Show how [MATERIAL] forms, gathers and disperses through [PROCESS].
A viewer unaware of the hidden code should understand the composition.
The information-guide input fixes the marks within this full scene.
Preserve their footprint, tonal gaps, relative scale and framing.
Render them as the same material produced by the event, with coherent
cluster sizes, surface behavior and density changes inside and outside.
The surrounding details must participate in this process, not decorate
a separate rectangular pattern. Do not add arbitrary matching blobs
as camouflage or make three regions receive unique visual treatment.
Keep the necessary light gaps and safe exterior separation intact.
No pasted code, display panel, square backing or three replacement icons.
The style-reference input, if present, supplies style only, not encoded content.
```

此模板不要求每一块编码都与其他块连通，也不要求加噪声。材料行为合理、信息区不暴露为专设码面，才是目标；粉末、连续液体、裂片或负形各自须形成可信分布。

## 抽象或材料主视觉提示词

仅当用户选择此方向时使用；不要把“码点占据主体”强加给场景方向。明确抽象规则，不靠元素数量或纹理复杂度代替构成。

```text
Create an abstract artwork governed by [COMPOSITIONAL RULE], using
[MATERIAL OR SHAPE VOCABULARY] in [PALETTE].
The information-guide input constrains information positions and light gaps.
Translate these marks into meaningful groups, varied scales and edges
consistent with the rule, without exposing a rectangular code panel.
Apply the same visual vocabulary throughout; avoid three unique corner
symbols, cleared islands, nested targets or decorative locator rings.
Preserve all encoded centers, proportions, framing and tonal separation.
Control highlights and shadows inside the existing dark footprints.
No random replacement code, conventional QR overlay or decorative
background doing all the creative work. No unwanted text or watermark.
```

## 修改的顺序

保留当前合格文件与报告作为技术回退，不继承其修改版的资格。

1. 整体刻意时重新设计材料分布和场景关系；不要只给固定方阵加纹理、外围点或尾巴。
2. 局部材料失配时统一区内外的厚度、光泽、粒径范围和边缘；高光及微阴影限制在既有暗轮廓内，保护浅色间隙。
3. 三处特殊时检查其形状、灰度、锐度和周围空隙。不要加三个新图标或无来历的陪衬团块，也不要直接删功能信息。
4. 解码失败时对照导引图诊断密度和明暗变化，做针对性修复。原图失败而某尺寸通过时可导出新候选，再对新的实际文件和全部预定变体完整验码；选用参考脚本时使用 qualify。
5. 每次信息、视觉或导出变化后重新验扫码，同时重看整图。材质统一、骨架通过、单个尺寸成功都不能替代最终双重验收。
