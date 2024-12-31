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

OnlyController aims to use Controller to use your computer instead of keyboard/mouse

Currently only simple mappings are supported

</div>

## Installation

```shell
$ git clone https://github.com/YohaneMashiro/OnlyController.git
$ cd OnlyController
```

```shell
$ pip install -r requirements.txt
```

## Existing Functionality

**One-way** mapping

| Controller input | Mapping     |
| -------- | -------- |
| A        | Left mouse button |
| B | Right mouse button |
| X | LeftCtrl |
| LS | Cursor movement |

## Usage

### 1.Run directly

If the above functions have met your needs, you can directly use the packaged executable program(./dist/OnlyController.exe)

### 2.Modify script

By simply modifying the script, you can

- Adjust refresh rate -> Modify variable frame_delay$
- Adjust sensitivity -> Modify variable sensitivity
- Modify mapping -> Modify function handle_button_events


However, the executable program will not immediately reflect your modifications