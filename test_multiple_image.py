import subprocess
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(current_dir, "test_model", "image")
result_dir = os.path.join(current_dir, "test_model", "result")
print(image_dir, result_dir)

os.makedirs(image_dir, exist_ok=True)
os.makedirs(result_dir, exist_ok=True)

run_file = "demo/image_demo.py"
config_file = "configs/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_pallet.py"
weigth_file = "work_dirs/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_pallet/epoch_12.pth"

for image_name in os.listdir(image_dir):
    image_path = os.path.join(image_dir, image_name)
    result_path = os.path.join(result_dir, image_name)
    detect_command = ["python", run_file, image_path, config_file, weigth_file, "--device", "cpu", "--out-file", result_path]
    try:
        subprocess.run(detect_command)
    except Exception as e:
        print(e)
        break
