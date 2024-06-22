import os
import zipfile
from tqdm import tqdm


def unzip_file(zip_filepath, dest_path):
    """
    解压缩zip文件到指定目录，并显示进度条

    参数:
    zip_filepath (str): ZIP文件的路径
    dest_path (str): 解压后文件应存放的目录
    """
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        # 获取ZIP文件内所有文件的信息
        zip_info_list = zip_ref.infolist()
        total_size = sum(file.file_size for file in zip_info_list)

        with tqdm(total=total_size, unit='B', unit_scale=True, desc='Unzipping') as pbar:
            for file in zip_info_list:
                zip_ref.extract(file, dest_path)
                pbar.update(file.file_size)


# 使用示例
zip_file = 'C:\\Users\\28318\\Desktop\\material-design-icons-master.zip'  # ZIP文件的路径
extract_to = 'C:\\Users\\28318\\Desktop\\material-design-icons-master'  # 解压后文件存放的目录

# 如果目标目录不存在，则创建它
if not os.path.exists(extract_to):
    os.makedirs(extract_to)

# 解压缩ZIP文件
unzip_file(zip_file, extract_to)
