from __future__ import absolute_import
import argparse

def arg_parse():
    parser = argparse.ArgumentParser(description='DLCV TA\'s tutorial in image classification using pytorch')

    # Datasets parameters
    parser.add_argument('--data_dir', type=str, default='hw3_data',
                    help="root path to data directory")
    parser.add_argument('--workers', default=4, type=int,
                    help="number of data loading workers (default: 4)")

    # training parameters
    parser.add_argument('--gpu', default=0, type=int,
                    help='gpu device ids for CUDA_VISIBLE_DEVICES')
    parser.add_argument('--epoch', default=50, type=int,
                    help="num of validation iterations")
    parser.add_argument('--val_epoch', default=1, type=int,
                    help="num of validation iterations")
    parser.add_argument('--train_batch', default=10, type=int,
                    help="train batch size")
    parser.add_argument('--test_batch', default=30, type=int,
                    help="test batch size")
    parser.add_argument('--ngpu', default=1, type=int,
                        help="number of gpus")
    parser.add_argument('--lr', default=0.0002, type=float,
                    help="initial learning rate")
    parser.add_argument('--beta', default=0.5, type=float,
                        help="initial beta")
    parser.add_argument('--weight-decay', default=0.0005, type=float,
                    help="initial learning rate")

    # resume trained model
    parser.add_argument('--resume', type=str, default='',
                    help="path to the trained model")
    # others
    parser.add_argument('--save_GAN', type=str, default='log_GAN')
    parser.add_argument('--random_seed', type=int, default=999)
    parser.add_argument('--save_img', type=str, default='seg_img')

    args = parser.parse_args()

    return args
