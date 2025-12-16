import os
import xml.etree.ElementTree as ET
from pathlib import Path

# ============ 用户配置区域 ============
XML_FOLDER = r"H:\dataset\rice\160\annotations"  # 修改为你的XML文件夹路径
OLD_CLASS_NAME = "Rice_Blast"
NEW_CLASS_NAME = "Rice_Lesion"
# ====================================


def change_class_name_in_xml(xml_path, old_name, new_name):
    """
    修改单个XML文件中的类别名称
    """
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        modified = False
        # 遍历所有object标签
        for obj in root.findall('object'):
            name_tag = obj.find('name')
            if name_tag is not None and name_tag.text == old_name:
                name_tag.text = new_name
                modified = True
        
        # 如果有修改，保存文件
        if modified:
            tree.write(xml_path, encoding='utf-8', xml_declaration=True)
            return True
        return False
    
    except Exception as e:
        print(f"处理文件 {xml_path} 时出错: {e}")
        return False


def main():
    xml_folder = Path(XML_FOLDER)
    
    # 检查文件夹是否存在
    if not xml_folder.exists():
        print(f"错误: 文件夹 {xml_folder} 不存在!")
        return
    
    # 获取所有XML文件
    xml_files = list(xml_folder.glob('*.xml'))
    
    if not xml_files:
        print(f"在 {xml_folder} 中没有找到XML文件!")
        return
    
    print(f"找到 {len(xml_files)} 个XML文件")
    print(f"开始将类别名称从 '{OLD_CLASS_NAME}' 修改为 '{NEW_CLASS_NAME}'...\n")
    
    modified_count = 0
    
    for xml_file in xml_files:
        if change_class_name_in_xml(xml_file, OLD_CLASS_NAME, NEW_CLASS_NAME):
            modified_count += 1
            print(f"✓ 已修改: {xml_file.name}")
    
    print(f"\n完成! 共修改了 {modified_count} 个文件")
    print(f"未修改 {len(xml_files) - modified_count} 个文件 (不包含类别 '{OLD_CLASS_NAME}')")


if __name__ == "__main__":
    main()
