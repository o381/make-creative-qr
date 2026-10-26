[English](execution.md) | **简体中文**

# 可选 Python/Node 参考实现

仅在宿主具备相应代码执行能力、且决定采用附带脚本时使用本文件。主工作流不要求安装这些库或调用这些命令；使用其他工具时按 SKILL.md 与 tool-adaptation.zh-CN.md 完成同等验收。缺少代码环境时选择可用的原生工具，不复制无法执行的终端命令。依赖准备须符合当前宿主的运行和权限规则。

将 `SKILL_DIR` 设为本技能实际目录，将 `TASK_DIR` 设为本次任务独立工作目录。安装后目录名可能改变。

先检查 Python 是否已有 `cv2`、`zxingcpp`、`segno`、`numpy`、`PIL`，以及 `cv2.wechat_qrcode_WeChatQRCode`。普通 opencv 不含 contrib 模块。必要时由助手在任务目录安装，不要求用户手动安装软件：

```bash
python3 -m pip install --target "$TASK_DIR/python-deps" -r "$SKILL_DIR/scripts/requirements.txt"
export PYTHONPATH="$TASK_DIR/python-deps${PYTHONPATH:+:$PYTHONPATH}"
```

使用 Node 和可用的 `sharp`；缺少时在任务目录安装并将 `CREATIVE_QR_NODE_MODULES` 指向该目录的 `node_modules`。不要全局安装或改变用户项目环境。能力不可用时如实说明，不假称已验证。

| 命令 | 输出及含义 |
| --- | --- |
| `capture` | 私有 payload.bin、本次 matrix.json、无明文内容的 source-report.json |
| `render_guide.py` | 精确信息骨架 SVG，尚未满足成图验收 |
| `rasterize.cjs` | 骨架 PNG 或明确尺寸的扫码 PNG，写出后必须复测 |
| `verify` | 完整文件快速检查；返回码 0 表示所有传入文件读出原内容，不代表完成缩放、压缩验收 |
| `probe` | 原图与内存变体诊断；返回码 0 仅表示至少一次诊断成功，不得批准交付 |
| `export` | 用与诊断相同的 Pillow Lanczos 机械导出 PNG，要求新路径且不放大；输出尚未获得资格 |
| `qualify` | 实际文件与全部预定 PNG、JPEG 变体均匹配且无冲突才返回 0；失败返回 2，异常返回 1 |
| `check_delivery.py` | 保存或展示前只读复核现有报告与当前实际文件；哈希、完整像素读取或必测证据不符则返回 2。不能替代 `qualify`、外观验收或手机证据。 |

`usable` 要求至少一个引擎读出原 payload，且无冲突内容。不能只看检测成功或 matching_engines。

ZXing 用 PIL RGB 图片；若改用 ndarray，按其 BGR 约定处理。OpenCV 明确进行 RGB→BGR 转换。错误通道顺序会错误淘汰彩色码。

WeChatCV 输出文本而非一般 raw bytes；脚本仅对 ASCII 回退。非 ASCII 或二进制内容用 ZXing 原始字节核对，不推测未知编码。

不向最终识别器传入四角、已知边界、纯码模式或裁剪区域。普通缩放用于诊断时区分原图与变体。

迭代时优先处理颗粒密度、浅色间隙、高光、暗阴影、粒径或尺寸。明亮颜色也可能含暗阴影。高分辨率不必然优于适合显示的尺寸。

如只有较小版本通过，导出该尺寸并对实际文件复测。印刷用途按预期尺寸与格式验证；手机拍照或印样测试实际执行之后才能报告。

## 软件验收与手机证据

手机分享默认 `qualify --widths 480 640 800 --qualities 85`，实际文件至少 800 像素宽。每个尺寸的 PNG 与 JPEG 85 均须通过，不能用“至少一个尺寸通过”替代。其他用途在生成前确定必测项，不在失败后削减。

读取 `qualification.json` 的 `all_qualified` 和逐张 `software_gate_passed`。报告同时保留实际文件 SHA-256、完整文件结果、每个变体结果、冲突及失败项。报告留在任务私有目录。批量调用中任一张失败会返回 2；可选择逐张全部通过的文件，不把组内失败图一并交付。

脚本固定将 `physical_phone_test_performed` 设为假，`phone_scan_status` 设为 `unverified`。这是软件证据边界，不能手改为已实测。手机反馈另存私有记录，绑定具体文件和扫描方式；用户反馈扫不出具有否决权。

内部变体是整图机械缩放、压缩后的诊断，不是已保存的交付文件。若缩小诊断通过，用 `export` 写出实际扫码 PNG 后重新 `qualify`。不要推定 Sharp 与 Pillow 输出相同；连续两次缩放也可能改变颗粒轮廓。最终图改动、重新导出或重编码后废弃旧报告。

迭代诊断可增加较小尺寸或更强压缩，不能用其部分成功批准交付：

```bash
python3 "$SKILL_DIR/scripts/qr_workflow.py" probe \
  --payload "$TASK_DIR/source/payload.bin" --image "$CANDIDATE_PNG" \
  --widths 320 480 640 800 --qualities 85 70 \
  --report "$TASK_DIR/probe-report.json"
```

需要机械导出时使用新路径，再对实际输出执行主工作流的全部 `qualify` 必测项：

```bash
python3 "$SKILL_DIR/scripts/qr_workflow.py" export \
  --image "$CANDIDATE_PNG" --out "$FINAL_PNG" --width 800
```

在实际交付前运行完整性复核，预定测试尺寸与压缩质量仍与生成前一致：

```bash
python3 "$SKILL_DIR/scripts/check_delivery.py" \
  --payload "$TASK_DIR/source/payload.bin" --report "$TASK_DIR/qualification.json" \
  --images "$FINAL_PNG" --widths 480 640 800 --qualities 85
```

检查所有工具的返回码，再执行依赖它的下一步。非零结果后不能继续上传、覆盖已保存版本或展示为成品。完整性检查不能让损坏文件通过，也不能借用同一报告批准另一个路径的文件；新的交付路径先重新 `qualify`。保存后若本地文件仍可能被写入，展示前再次核对。

生成前按已有偏好或 Skill 默认规则确定创意方向，并锁定本次用户的内容；不要把上一位用户的二维码用于下一位用户。

## 参考命令链

仅在选用本实现且依赖已就绪时使用；路径与文件名是本实现的约定，可按任务调整。

```bash
python3 "$SKILL_DIR/scripts/qr_workflow.py" capture \
  --source "$SOURCE_IMAGE" --out "$TASK_DIR/source"
python3 "$SKILL_DIR/scripts/render_guide.py" \
  --matrix "$TASK_DIR/source/matrix.json" --out "$TASK_DIR/guide.svg" --shape grains
node "$SKILL_DIR/scripts/rasterize.cjs" \
  "$TASK_DIR/guide.svg" "$TASK_DIR/guide.png" 1000
```

逐步检查成功状态。上述导引只作为技术约束，继续按主流程选择宿主创作能力制作实际作品。

需要同内容的新排列时，用原始字节重编码，参数按内容与构成选择；下面数值仅作接口示例：

```bash
python3 "$SKILL_DIR/scripts/qr_workflow.py" reencode \
  --payload "$TASK_DIR/source/payload.bin" --out "$TASK_DIR/variant-matrix.json" \
  --mask 6 --min-version 5
python3 "$SKILL_DIR/scripts/render_organic_guide.py" \
  --matrix "$TASK_DIR/variant-matrix.json" --out "$TASK_DIR/variant.svg" \
  --shape shards --group-probability .5
```

对实际完整成图执行默认七项测试，再进行交付复核：

```bash
python3 "$SKILL_DIR/scripts/qr_workflow.py" qualify \
  --payload "$TASK_DIR/source/payload.bin" --images "$FINAL_PNG" \
  --widths 480 640 800 --qualities 85 --report "$TASK_DIR/qualification.json"
```

返回码为 0 且当前文件 software_gate_passed 为真才通过这条实现的软件验收；之后再运行上文的 check_delivery.py。主流程中的外观与手机状态独立记录。
