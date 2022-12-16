import os
import shutil
import json
import sys

current_folder = os.path.dirname(os.path.abspath(__file__))

data_name = "Pallet_data"
data_folder = "train"

pallet_folder = sys.argv[1] # ../dataset/Pallet_data
dest_folder = sys.argv[2] # /train/0089
dest_folder = os.path.join(current_folder, dest_folder)

folder_key = os.path.basename(dest_folder) # "0089"

annotation_file_path = os.path.join(pallet_folder, f"via_region_data_{data_folder}.json")

annotation_file = open (annotation_file_path, "r")
annotation_data = json.load(annotation_file) 

copied_image_num = 0
print("Copying ...")

for key in annotation_data.keys():
    folder_num = key.split("_")[0]
    if folder_num != folder_key:
        continue

    image_num = key.split("_")[1]
    image_folder = os.path.join(pallet_folder, folder_num)

    if not os.path.isdir(image_folder):
        continue
    copied_image = os.path.join(image_folder, f"{image_num}-color.png")
    if not os.path.isfile(copied_image):
        continue
    
    # dest_sub_folder = os.path.join(dest_folder, folder_num)
    dest_file_path = os.path.join(dest_folder, f"{image_num}-color.png")
    if os.path.isfile(dest_file_path):
        continue
    os.makedirs(dest_folder, exist_ok=True)
    shutil.copy(copied_image, dest_folder)

    # copied_image_num += 1
    # print("{:.2f}".format(copied_image_num / len(annotation_data.keys()) * 100), "% ", end = "")

print("Copy done")