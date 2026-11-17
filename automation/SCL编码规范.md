# SCL 编码规范

> 适用于西门子 S7-1200/1500 的 SCL 块。SICAR 项目的具体命名以项目手册为准，本页只写通则不违背的部分。

## 1. 命名

| 对象 | 规则 | 例子 |
|---|---|---|
| 功能块 FB | 动词 + 对象 | `FB_AxisHome` |
| 功能 FC | 动词 + 对象 | `FC_CalcCycleTime` |
| 数据块 DB | 前缀 + 用途 | `DB_AxisParam` |
| 临时变量 | `#snake_case` | `#iRetryCount` |
| 静态变量 | 匈牙利别加，用域区分 | `#stStatus` 而非 `#statStatus` |
| I/O 点 | 设备_动作_序号 | `S1_LightOn_01` |

禁：拼音缩写、无意义前缀、`tmp1` `a` `b`。

## 2. 块结构

```scl
FUNCTION_BLOCK "FB_Example"
{ S7_Optimized_Access := 'TRUE' }
VERSION : 0.1

VAR_INPUT
  iEnable : Bool;
END_VAR

VAR_OUTPUT
  qDone : Bool;
  qError : Bool;
END_VAR

VAR
  stState : Int;
  tonTimeout : TON;
END_VAR

BEGIN
  // 1. 初始化 / 复位
  // 2. 状态机
  // 3. 报警处理
  // 4. 输出
END_FUNCTION_BLOCK
```

规则：
- 一个 FB 只做一件事；超过 200 行就该拆
- 状态机用 `Int` 常量或 `Enum`，不要用一堆布尔标志互相判
- 输入先判 `iEnable`，禁用时所有输出回默认值

## 3. 注释

块头必写：

```
(*
  功能：
  调用要求：
  输入：
  输出：
  作者/日期：
  变更记录：
*)
```

行内注释写“为什么”，不写“是什么”。`// 加一` 这种不要写。

## 4. 错误处理

- 每个带 `ENO` 的调用都要判 `ENO`，不判就等于默认永不失败
- 错误分两级：可恢复（重试 / 提示）与不可恢复（停机 / 报警）
- 错误码集中定义在一个 DB 里，不要在代码里散落数字

## 5. 时间与数值

- 定时不用 `SLEEP`、不用扫描周期凑时间；用 `TON` / `TONR`
- 浮点比较用容差，不用 `==`
- 单位写进变量名（`rSpeed_mm_s`、`tDelay_ms`）

## 6. 版本与变更

- 每块头写 `VERSION`，改动就升
- 交付前归档整个 TIA 项目（含硬件组态），不只导程序
- 符号表与 I/O 清单跟着归档走，不要事后补

## 7. 交付前自检

- [ ] 没有未使用的变量、没有调不通的块
- [ ] 所有 `ENO` 都判了
- [ ] 报警码与报警文本一一对应
- [ ] 掉电保持的 DB 确认过
- [ ] 冷启动、热重启都测过
