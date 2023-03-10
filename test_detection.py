import mmcv
from mmcv.runner import load_checkpoint

from mmdet.apis import inference_detector, show_result_pyplot
from mmdet.models import build_detector

def main():
    # Choose to use a config and initialize the detector
    # config = 'configs/faster_rcnn/faster_rcnn_r50_caffe_fpn_mstrain_3x_coco.py'
    config = 'configs/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_pallet.py'
    # Setup a checkpoint file to load
    # checkpoint = 'checkpoints/faster_rcnn_r50_caffe_fpn_mstrain_3x_coco_20210526_095054-1f77628b.pth'
    checkpoint = 'work_dirs/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_pallet/epoch_12.pth'

    # Set the device to be used for evaluation
    device='cuda:0'

    # Load the config
    config = mmcv.Config.fromfile(config)
    # Set pretrained to be None since we do not need pretrained model here
    config.model.pretrained = None

    # Initialize the detector
    model = build_detector(config.model)

    # Load checkpoint
    checkpoint = load_checkpoint(model, checkpoint, map_location=torch.device('cpu') )

    # Set the classes of models for inference
    model.CLASSES = checkpoint['meta']['CLASSES']

    # We need to set the model's cfg for inference
    model.cfg = config

    # Convert the model to GPU
    model.to(device)
    # Convert the model into evaluation mode
    model.eval()

    img = "demo/pallet.png"
    result = inference_detector(model, img)
    show_result_pyplot(model, img, result, score_thr=0.3)

if __name__ == "__main__":
    main()
