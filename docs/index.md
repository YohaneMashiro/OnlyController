---
layout: default
title: WereBench
nav_order: 1
description: A benchmark & docs site for WereBench.
---

# WereBench

> A Benchmark for Role Inference and Reasoning in Werewolf-style Settings

![banner](/WereBench/assets/banner.png){: .mt-4 .mb-4 }

**快速入口：**
- 📄 [Paper (arXiv: 2510.11389)](https://arxiv.org/pdf/2510.11389)
- 🐙 [GitHub Repo](https://github.com/YohaneMashiro/OnlyContorller)
- 🤗 [HuggingFace Dataset](https://huggingface.co/datasets/Yuan4629/WereBench)

---

## 简介
**WereBench** 是一个面向“狼人杀/角色推理”类任务的评测基准，聚焦**角色识别、阵营判断、基于发言的逻辑推理**等能力评测。数据以结构化问答形式组织，便于直接用于评测脚本或大模型推理调用。

👉 立刻上手：查看 [Quick Start](./quickstart){: .btn .btn-primary }  
📊 结果汇总：查看 [Leaderboard](./leaderboard){: .btn }

---

## 特性
- **任务聚焦**：围绕“角色/阵营/行动”的细粒度推理。
- **结构化数据**：统一字段、标准化选项，便于评测脚本处理。
- **可扩展**：可追加新季/新局数据、补充更复杂逻辑问题。

<!-- 更多细节见 [Dataset](./dataset)。 -->

---

## 引用 / Citation
如果本项目对您有帮助，请引用我们的论文：

```bibtex
@article{WereBench2025,
  title={WereBench: A Benchmark for Role Inference and Reasoning},
  author={Your Author List},
  journal={arXiv preprint arXiv:2510.11389},
  year={2025}
}
