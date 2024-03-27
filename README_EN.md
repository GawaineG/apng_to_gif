![Static Badge](https://img.shields.io/badge/License-MIT-blue?style=flat-square) ![Static Badge](https://img.shields.io/badge/Language-Python-yellow?style=flat-square) ![Static Badge](https://img.shields.io/badge/Python%20Version-%3E%3D3.6-red?style=flat-square)

English / [中文](./README.md)
# APNG to GIF
This is a script which can convert APNG files to GIF files in batches and set to infinite loop. 
## Origin
I want to use those cute dynamic stickers on LINE when chatting on other social apps which do not support the APNG format. However, the image files exported from LINE are in the APNG format and can only be played once, so I wrote this script.
## Usage Instructions
To use this script, please follow these steps:
1. This script requires a library called [apnggif](https://pypi.org/project/apnggif/), which requires python>=3.6, Please ensure that you have installed this library. You can Use the package manager [pip](https://pip.pypa.io/en/stable/) to install it:
```sh
pip install apnggif
```

2. The input directory is `./input`. You need to create a folder named "input" in the directory where the script is located and put the APNG files to be converted into it;

3. Run apng_to_gif.py;

4. Done. You can find those converted GIF files in `./output`.
## License
[MIT](https://choosealicense.com/licenses/mit/)
## Problem
As a beginner in coding, I currently encounter a problem:

I want to encapsulate the script into an EXE file to easily send it to others, but after encapsulating it into a single EXE file with pyinstaller using the `pyinstaller -F apng_to_gif.py` command, I cannot read the path where the EXE file is stored, which means I also cannot read the "input" folder under the same path as the EXE file. After checking, I found that when the EXE is running, a temporary folder will be generated and the EXE will run in the folder, and the folder will be deleted after running.

At present, I found that the EXE file generated using the `pyinstaller apng_to_gif.py` command can read the `./_internal` folder, so I changed the fifth line in this script to `os.chdir(os.path.dirname(script_path))`. After that, the EXE can be run smoothly and the conversion can be completed. But I always feel that this method is a bit tricky and not quite right. If you can solve this problem, please teach me!

Contact me via e-mail: gyxgawaine@163.com