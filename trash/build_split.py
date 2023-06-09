import argparse
import os
import numpy as np

def build_split_list(raw_path, mode):
    raw_path = os.path.join(raw_path, '{}list01.txt'.format(mode))
    print('{} analysis begin'.format(raw_path))
    with open(raw_path, 'r') as fin:
        lines = fin.readlines()
    fin.close()

    with open('{}list.txt'.format(mode), 'w') as fout:
        for i, line in enumerate(lines):
            line = line.strip()  # 'class_name/video_name'
            label_dir = 'labels' + '/' + line  # 'data/ucf24/labels/class_name/video_name'
            if not os.path.isdir(label_dir):
                continue
            txt_list = os.listdir(label_dir)
            txt_list.sort()
            for txt_item in txt_list:
                filename = label_dir + '/' + txt_item
                fout.write(filename + '\n')
            if i % 200 == 0:
                print('{} videos parsed'.format(i))
    fout.close()
    print('{} analysis done'.format(raw_path))

def create_txt(raw_data, label, arr_videos, mode) :
    with open('{}/{}list.txt'.format(raw_data ,mode), 'a') as fout:
        for video in arr_videos :
            file_list = os.listdir(os.path.join(raw_data, 'labels', label, video))
            file_list.sort()
            for file in file_list :
                path = os.path.join('labels', label, video, file)
                fout.write(path + '\n')
    fout.close()

def build_split_data(raw_data) :
    labels = os.listdir(os.path.join(raw_data, 'labels')) # lay cac label
    for label in labels :
        print(label)
        fvideos = os.listdir(os.path.join(raw_data, 'labels', label))
        N = len(fvideos)
        n_train = int(N * 0.8)
        n_test = N- n_train
        # np.random.shuffle(fvideos)

        train_video, test_video = fvideos[:n_train], fvideos[n_train:]
        create_txt(raw_data= raw_data, label= label, arr_videos= train_video, mode= 'train')
        create_txt(raw_data= raw_data, label= label, arr_videos= test_video, mode= 'test')

def parse_args():
    parser = argparse.ArgumentParser(description='Build file list')
    parser.add_argument('--raw_path', type=str, default='./trash')
    parser.add_argument('--out_list_path', type=str, default='./')
    parser.add_argument('--shuffle', action='store_true', default=False)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    build_split_data(args.raw_path)