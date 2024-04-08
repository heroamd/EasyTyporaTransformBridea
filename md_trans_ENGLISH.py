import os
import re
import shutil

def extract_image_filenames_from_md(directory, new_base_path):
    # Define a regular expression to match image links in Markdown files.
    img_pattern = re.compile(r'!\[.*?\]\((\.\/)?pic\/(.*?)\)')
    image_filenames = []

    # Traverse a specified directory.
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file extension is .md.
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                # Read the contents of a .md file.
                with open(filepath, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()
                    # Find all matching image file names.
                    matches = img_pattern.findall(content)
                    for match in matches:
                        # Add the found image file names to a list.
                        image_filenames.append(match[1])
                replace_image_paths(filepath, new_base_path)

    return image_filenames

def replace_image_paths(md_file_path, new_base_path):
    # Define a regular expression for matching image links.
    img_pattern = re.compile(r'!\[(.*?)\]\((\.\/pic\/)(.*?)\)')
    new_content = []

    # Read Markdown files
    with open(md_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Iterate through each line, search for and replace image paths.
    for line in lines:
        new_line = re.sub(img_pattern, r'![\1](' + new_base_path + r'\3)', line)
        new_content.append(new_line)

    # 将修改后的内容写回文件
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_content)

# DEMO
directory_path = 'D:/blog/posts/posts'  # Replace this with the directory location of Markdown files in Gridea.
dst = 'D:/blog/posts/post-images' # The directory location for storing images in Gridea, typically does not need to be changed.
pic_path = 'C:/Users/qi/Desktop/master/Notes/pic/'  # The default location where Typora automatically saves inserted images.
new_base_path = 'file://D:/blog/posts/post-images/' # The new base path.

image_filenames = extract_image_filenames_from_md(directory_path, new_base_path)

for img in image_filenames:
    img_full_path = pic_path + img
    shutil.copy(img_full_path, dst)
    print(img_full_path)
