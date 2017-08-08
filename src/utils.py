# coding: utf-8

import os
from tensorflow.contrib.keras.python.keras.preprocessing.sequence import pad_sequences as tf_pad_sequences

PAD_SYMBOL = 0

WORD2VEC_FILE_NAME = 'GoogleNews-vectors-negative300.txt'
GLOVE_FILE_NAME = 'glove.840B.300d.txt'
FASTTEXT_FILE_NAME = 'wiki.en.vec'


def original_embedding_file(pretrain='word2vec'):
    """
    Get file path to original unprocessed embeddings
    """

    data_path = directory('/data')

    if pretrain == 'glove':
        return data_path + '/' + GLOVE_FILE_NAME
    elif pretrain == 'word2vec':
        return data_path + '/' + WORD2VEC_FILE_NAME
    elif pretrain == 'fasttext':
        return data_path + '/' + FASTTEXT_FILE_NAME
    else:
        return None


def directory(dir='/', make_sub_dirs=None):
    """Get directory, from out directory in the repo"""
    full_dir = os.path.dirname(os.path.realpath(__file__)) + '/..' + dir
    if not os.path.exists(full_dir):
        os.makedirs(full_dir)

    if make_sub_dirs is not None:
        for sub_dir in make_sub_dirs:
            if not os.path.exists(full_dir + '/' + sub_dir):
                os.makedirs(full_dir + '/' + sub_dir)

    return full_dir


def pad_sequences(xs, maxlen):
    return tf_pad_sequences(
        xs,
        maxlen=maxlen,
        dtype='int32',
        padding='post',
        truncating='post',
        value=PAD_SYMBOL
    )


class dotdict(dict):
    """ dot.notation access to dictionary attributes """
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
