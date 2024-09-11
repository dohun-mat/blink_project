from argparse import ArgumentParser
import time
import video2img_info
import video_inference
import blink_convertor
import result_visual
import socket
import cv2
import struct
import json
import blink_gogo

import os
from flask import Flask, request, jsonify
from threading import Thread
import numpy as np
import torch
from mmcv import DictAction
from mmcv.parallel import collate, scatter
from tqdm import tqdm
import math
from mmdet.apis import init_detector
from mmdet.datasets.pipelines import Compose
from mmcv.cnn.utils.flops_counter import add_flops_counting_methods, flops_to_string, params_to_string
from mmdet.core import build_assigner
from mmcv import ConfigDict
import time
import numpy as np

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--config', default='configs/instblink/instblink_r50.py', help='Config file')
    parser.add_argument('--checkpoint',default='pretrained_models/instblink_r50.pth', help='Checkpoint file')
    parser.add_argument(
        '--json',
        default="demo_video/intermediate_results/info.json",
        help='Path to mpeblink test json file')   
    parser.add_argument(
        '--root', default="demo_video/intermediate_results", help='Path to image file') 
    parser.add_argument(
        '--device', default='cuda:0', help='Device used for inference')
    parser.add_argument(
        '--cfg-options',
        nargs='+',
        action=DictAction,
        help='override some settings in the used config, the key-value pair '
        'in xxx=yyy format will be merged into config file. If the value to '
        'be overwritten is a list, it should be like key="[a,b]" or key=a,b '
        'It also allows nested list/tuple values, e.g. key="[(a,b),(c,d)]" '
        'Note that the quotation marks are necessary and that no white space '
        'is allowed.')
    parser.add_argument('--download', action='store_true', help = 'watch_result')
    args = parser.parse_args()
    return args

app = Flask(__name__)
# 전역 변수로 이미지 저장
@app.route('/api/process', methods=['POST'])
def process_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video provided'}), 400

    # 비디오 파일 받기
    file = request.files['video']
    video_path = 'received_video.mp4'
    file.save(video_path)

    # 비디오 파일 처리 (예시로 첫 프레임 읽기)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return jsonify({'error': 'Could not open video'}), 500

    ret, frame = cap.read()
    if not ret:
        return jsonify({'error': 'Could not read frame from video'}), 500

    # 이미지 시각화
    # cv2.imshow("Received Frame", frame)
    # cv2.waitKey(0)  # 키 입력 대기
    # cv2.destroyAllWindows()
    
   

    # 예시 결과
    # result = {'result': '처리 완료'}

    # 비디오 파일 삭제 (옵션)
    # os.remove(video_path)
    a = main(cap)
    print("a")
    print(a)
    os.remove(video_path)
    
    return jsonify(f'{a}')



def main(cap):
    # 비디오를 프레임으로 나누고 JSON으로 저장
    
    print("vvvvvvvvvvvvvvvvvvvvv")

    
    video2img_info.main(cap)
    
    # # 비디오에서 모델 추론 수행
    args = parse_args()
    video_inference.main(args)
    
    # 눈 깜빡임 감지
    b = blink_gogo.main(args)

    
    if args.download == True:
        # print("@@@@@@@@@@@@@@")
        # 결과 시각화
        data_root = "demo_video"
        result_visual.visual_pred(data_root)
    
    return b
    
    # # 결과 시각화
    # data_root = "demo_video"
    # result_visual.visual_pred(data_root)
    
    # # 결과 삭제 (중간 결과 파일)
    # # import shutil
    # # shutil.rmtree('demo_video/intermediate_results', ignore_errors=True)
    
    print('All tasks completed.')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50023,debug=True)
    # while(True):
    # main()
