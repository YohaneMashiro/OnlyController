<!-- markdownlint-disable -->

<div align="center">

<img alt="LOGO" src="./icon.ico" width="256" height="256" />

# OnlyContorller

<br>
<div>
    <img alt="python" src="https://img.shields.io/badge/python-3.11.7-%233776AB?logo=python&logoColor=white">
    <img alt="platform" src="https://img.shields.io/badge/platform-Windows-blueviolet">
    <img alt="license" src="https://img.shields.io/badge/License-MIT-yellow.svg">
</div>
<br>

<!-- markdownlint-restore -->
[简体中文](https://github.com/YohaneMashiro/OnlyController/blob/main/README.md) | [English](https://github.com/YohaneMashiro/OnlyController/blob/main/README_EN.md)

OnlyController功能为使用手柄代替键盘/鼠标

目前仅支持简单映射

~~绝赞更新中  ✿✿ヽ(°▽°)ノ✿~~
</div>

## 安装

```shell
$ git clone https://github.com/YohaneMashiro/OnlyController.git
$ cd OnlyController
```

```shell
$ pip install -r requirements.txt
```

## 现有功能

**单向**映射

| 手柄输入 | 映射     |
| -------- | -------- |
| A        | 鼠标左键 |
| B | 鼠标右键 |
| X | 左Ctrl |
| 左摇杆 | 光标移动 |

## 使用

### 1.直接运行

如果上述功能已经满足需求，可以直接使用打包好的可执行程序(./dist/OnlyController.exe)

### 2.修改脚本

通过简单地修改脚本，您可以

- 调整刷新率 -> 修改frame_delay变量
- 调整灵敏度 -> 修改sensitivity变量
- 修改映射 -> 修改handle_button_events函数

但是可执行程序并不会即时反映您的修改