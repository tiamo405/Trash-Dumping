# Train YOWOv2 on UCF24 dataset
python train.py \
        --cuda \
        -d trash \
        -v yowo_v2_medium \
        --root . \
        --num_classes 2 \
        --num_workers 2 \
        --eval_epoch 5 \
        --max_epoch 30 \
        --lr_epoch 2 3 4 5 \
        -lr 0.0001 \
        -ldr 0.5 \
        -bs 8 \
        -accu 16 \
        -K 16
