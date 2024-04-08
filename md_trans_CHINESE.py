import os
import re
import shutil

def extract_image_filenames_from_md(directory, new_base_path):
    # 定义一个正则表达式来匹配Markdown文件中的图片链接
    img_pattern = re.compile(r'!\[.*?\]\((\.\/)?pic\/(.*?)\)')
    image_filenames = []

    # 遍历指定目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件扩展名是否为.md
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                # 读取.md文件内容
                with open(filepath, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()
                    # 查找所有匹配的图片文件名
                    matches = img_pattern.findall(content)
                    for match in matches:
                        # 将找到的图片文件名添加到列表中
                        image_filenames.append(match[1])
                replace_image_paths(filepath, new_base_path)

    return image_filenames

def replace_image_paths(md_file_path, new_base_path):
    # 定义用于匹配图片链接的正则表达式
    img_pattern = re.compile(r'!\[(.*?)\]\((\.\/pic\/)(.*?)\)')
    new_content = []

    # 读取Markdown文件
    with open(md_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 遍历每一行，寻找并替换图片路径
    for line in lines:
        new_line = re.sub(img_pattern, r'![\1](' + new_base_path + r'\3)', line)
        new_content.append(new_line)

    # 将修改后的内容写回文件
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_content)

# 使用示例
directory_path = 'D:/blog/posts/posts'  # 将此处替换为Gridea中的md的目录的位置
dst = 'D:/blog/posts/post-images' # Gridea的图片存放路径，正常不需要更改
pic_path = 'C:/Users/qi/Desktop/研究生/Notes/pic/'  # Typora所插入图片所自动保存的位置
new_base_path = 'file://D:/blog/posts/post-images/' # 新的基础路径

image_filenames = extract_image_filenames_from_md(directory_path, new_base_path)

for img in image_filenames:
    img_full_path = pic_path + img
    shutil.copy(img_full_path, dst)
    print(img_full_path)
