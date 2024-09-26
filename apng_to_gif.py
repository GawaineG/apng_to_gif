import os
import sys
from apnggif import apnggif

# 获取运行时 EXE 或脚本所在路径
if getattr(sys, 'frozen', False):
    app_path = os.path.abspath(sys.executable)
elif __file__:
    app_path = os.path.abspath(__file__)
script_path = os.path.dirname(app_path)

os.chdir(os.path.dirname(script_path))  # 修改当前路径为所在目录路径
input_dir = os.path.join(script_path, "input/")
output_dir = os.path.join(script_path, "output/")
os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在

# 将 GIF 文件循环次数改为无限
def set_gif_loop_count(file_path, loop_count):
    with open(file_path, 'rb+') as file:
        content = file.read()
        loop_pos = content.find(b'\x21\xFF\x0B\x4E\x45\x54\x53\x43\x41\x50\x45\x32\x2E\x30\x03\x01')
        if loop_pos > -1:
            loop_pos += 16  # 跳到循环次数位置
            file.seek(loop_pos)
            file.write(loop_count.to_bytes(2, byteorder='little'))

# 遍历文件夹内所有文件并处理
for filename in os.listdir(input_dir):
    if filename.endswith('.png'):  # 只处理后缀为.png的文件
        input_apng_file = os.path.join(input_dir, filename)  # 输入的 APNG 文件名
        output_gif_file = os.path.join(output_dir, os.path.splitext(filename)[0]+'.gif')  # 输出的 GIF 文件名
        apnggif(input_apng_file, output_gif_file)  # 将输入的 APNG 文件转换为 GIF 文件
        set_gif_loop_count(output_gif_file, 0)  # 设置 GIF 文件的循环次数为无限（0 表示无限次）
