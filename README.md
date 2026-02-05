# HereComesTheGoodNews

用于 **定时检测浙江大学盲审结果** 的自动化工具。

本项目基于 **GitHub Actions**，通过定时任务自动登录浙大系统，获取盲审状态，并在结果发生变化时，使用 **PushMe** 将通知发送到手机。  
⚠️ 本项目参考自：[https://gist.github.com/FanBB2333/229d177bbffdb1adc96f5f8a65a3c47f](https://gist.github.com/FanBB2333/229d177bbffdb1adc96f5f8a65a3c47f)


---

## ✨ 功能简介

- ⏱ 基于 GitHub Actions 的定时执行
- 🔐 自动登录浙大系统并获取盲审状态
- 🔄 自动检测盲审结果是否发生变化
- 📲 使用 PushMe 推送结果到手机
- ▶ 支持手动触发执行，便于调试

---

## 🧠 工作原理

```text
GitHub Actions 定时 / 手动触发
        ↓
运行 Python 脚本
        ↓
登录浙大系统
        ↓
获取盲审状态
        ↓
与历史结果对比
        ↓
结果变化 → PushMe 推送通知
````

---

## 📦 使用流程

### 1️⃣ Fork 本仓库

将本仓库 fork 到你自己的 GitHub 账号下。

---

### 2️⃣ 设置仓库权限（重要）

进入你 fork 后的仓库：

```
Settings → Actions → General
```

将 **Workflow permissions** 设置为：

* ✅ **Read and write permissions**

该权限用于在 workflow 运行时，将最新的盲审结果写入仓库（用于状态对比）。

---

### 3️⃣ 安装 PushMe 并获取 Push Key

1. 下载并安装 **PushMe**： [https://github.com/yafoo/pushme](https://github.com/yafoo/pushme)  
2. 在手机端获取你的 **Push Key**。

> 该 Key 将用于将盲审结果推送到你的手机。

### 4️⃣ 配置 GitHub Actions Secrets

进入：

```
Settings → Secrets and variables → Actions
```

新增以下 **Secrets**：

| Secret 名称        | 说明             |
| ---------------- | -------------- |
| `PUSH_KEY`       | PushMe 的push_key |
| `ZJUAM_ACCOUNT`  | 浙大统一身份认证账号     |
| `ZJUAM_PASSWORD` | 浙大统一身份认证密码     |

> ⚠️ 注意
> 所有敏感信息仅存储在 GitHub Secrets 中，**不要**写入代码或提交到仓库。

---

### 5️⃣ 手动运行测试

在仓库中进入：

```
Actions → HereComesTheGoodNews → Run workflow
```

手动运行一次 workflow，确认：

* 登录是否成功
* 是否能够正确获取盲审结果
* PushMe 是否能够正常收到通知

---

## ⏱ 定时执行说明

项目使用 GitHub Actions 的 `schedule` 触发器定时运行，具体执行时间可在：

```
.github/workflows/*.yml
```

中自行调整。

---

## ⚠️ 注意事项

1. **请勿设置过高的检测频率**
   频繁访问可能触发系统风控或导致账号异常。

2. **GitHub Actions 执行时间可能存在延迟**
   定时任务不保证精确到分钟级执行。

3. **账号与密码安全**
   请妥善保管账号信息，避免泄露。

---

## 📄 免责声明

本项目仅用于 **个人盲审状态查询的自动化辅助**，请勿用于任何违反相关系统使用条款的行为。
因使用本项目造成的任何后果，均由使用者自行承担。

