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

Contact me via e-mail: gyxgawaine@163.com
