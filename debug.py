# import os
# os.environ['OPENCV_IO_ENABLE_OPENEXR'] = "1"
# import OpenEXR
# import Imath
# from PIL import Image
# import numpy as np
# import cv2


# # 指定路径
# input_dir = "/home/db3/kyz/Code/TensoSDF/data/Custom/hdr_luckycat/inputs/images"
# output_dir = "/home/db3/kyz/Code/TensoSDF/data/Custom/hdr_luckycat/inputs/converted_images"

# # 如果输出文件夹不存在，创建文件夹
# os.makedirs(output_dir, exist_ok=True)

# # 获取目录下所有的.exr文件
# for file_name in os.listdir(input_dir):
#     if file_name.endswith('.exr'):
#         input_file_path = os.path.join(input_dir, file_name)
#         output_file_path = os.path.join(output_dir, file_name.replace('.exr', '.png'))
#         hdr = cv2.imread(input_file_path, flags=cv2.IMREAD_ANYDEPTH)
#         # Simply clamp values to a 0-1 range for tone-mapping
#         ldr = np.clip(hdr, 0, 1)
#         # Color space conversion
#         ldr = 255.0 * ldr
#         cv2.imwrite(output_file_path, ldr)
#         print(f"Converted {file_name} to PNG")

import os
os.environ['OPENCV_IO_ENABLE_OPENEXR'] = "1"
import cv2
import numpy as np
from utils.raw_utils import linear_to_srgb

# 输入和输出路径
input_dir = "/home/db3/kyz/Code/TensoSDF/data/Custom/hdr_goldenqilin/inputs/images"
output_dir = "data/custom/GoldenQiLin/images"

# 如果输出文件夹不存在，创建文件夹
os.makedirs(output_dir, exist_ok=True)

# 获取目录下所有的.exr文件
for file_name in sorted(os.listdir(input_dir)):
    if file_name.endswith('.exr'):
        input_file_path = os.path.join(input_dir, file_name)
        
        # 读取EXR图像
        img = cv2.imread(input_file_path, cv2.IMREAD_UNCHANGED)
        
        # 检查图像是否读取成功
        if img is not None:
            # 检查是否是浮动点图像 (通常EXR是浮动点格式)
            if img.dtype == np.float32 or img.dtype == np.float64:
                # 将图像的像素值调整到[0, 255]的范围
                img = np.clip(img, 0, 1.)
                img = linear_to_srgb(img) * 255
                img = img.astype(np.uint8)
            
            # 将图像保存为PNG格式
            output_file_path = os.path.join(output_dir, file_name.replace('.exr', '.png'))
            cv2.imwrite(output_file_path, img)
            print(f"Converted {file_name} to PNG")
        else:
            print(f"Failed to read {file_name}")