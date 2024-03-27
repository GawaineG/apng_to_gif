![Static Badge](https://img.shields.io/badge/License-MIT-blue?style=flat-square) ![Static Badge](https://img.shields.io/badge/Language-Python-yellow?style=flat-square) ![Static Badge](https://img.shields.io/badge/Python%20Version-%3E%3D3.6-red?style=flat-square)

中文 / [English](./README_EN.md)
# 将 APNG 转换为 GIF
这是一个能够批量将 APNG 文件转换为 GIF 文件并设置为无限循环的脚本。
## 起源
因为想要在其他不支持 APNG 格式的社交软件上聊天时也能使用 LINE 上的好看的动态贴图，但从 LINE 导出的图片文件是 APNG 格式，且只播放一次，于是制作了此脚本。
## 使用说明
要使用该脚本进行转换，请按照以下步骤：
1. 此脚本利用了 [apnggif](https://pypi.org/project/apnggif/) 库，需要 python>=3.6 版本，请首先确保安装了该库。可利用 [pip](https://pip.pypa.io/en/stable/) 通过以下命令进行安装：
```sh
pip install apnggif
```

2. 输入目录为 `./input`。需要在脚本所在的目录下创建一个名为“input”的文件夹，并放入待转换的 APNG 文件；

3. 运行 apng_to_gif.py 脚本；

4. 完成。可以在 `./output` 内找到完成转换的 GIF 文件。
## 许可
[MIT](https://choosealicense.com/licenses/mit/)
## 问题
作为一个敲代码方面的新手，目前遇到了一个问题：

我想要将脚本封装成 EXE 文件以方便地发送给他人使用，但通过 pyinstaller 使用 `pyinstaller -F apng_to_gif.py` 命令封装成单个 EXE 文件后无法读取到 EXE 文件所存储的路径，也就无法读取到与 EXE 文件在同一路径下的 input 文件夹。查阅后发现 EXE 运行时会生成一个临时文件夹并在该文件夹内运行，运行结束后会删除。

目前发现使用 `pyinstaller apng_to_gif.py` 命令生成的 EXE 文件能读取到 `./_internal` 文件夹，于是我将脚本内第五行改为 `os.chdir(os.path.dirname(script_path))` 后能够顺利运行 EXE 并完成转换。但总觉得这个方法有点取巧，不太对劲，希望能得到社区大佬的指点。

联系我：gyxgawaine@163.com
