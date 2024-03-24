
import os
import csv

# 函数用于获取指定文件夹中的文件路径列表
def get_file_paths(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths

# 文件夹路径
# folder1_path = "./dataset/STS_npy_train/Image"
# folder2_path = "./dataset/STS_npy_train/Mask"
path = 'F:\competition\\teeth-seg\PytorchDeepLearing-main'
folder1_path = path + "/dataprocess/dataset/STS_npy_augtrain/Image"
folder2_path = path + "/dataprocess/dataset/STS_npy_augtrain/Mask"


# 获取文件路径列表
folder1_files = get_file_paths(folder1_path)
folder2_files = get_file_paths(folder2_path)

# 写入文件路径到CSV文件
with open('./dataset/augtrain_paths.csv', 'w', newline='') as csvfile:
    fieldnames = ['Image', 'Mask']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for image_path, mask_path in zip(folder1_files, folder2_files):
        writer.writerow({'Image': image_path, 'Mask': mask_path})

