#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BaseConfig():
    DIR_IMG = '/content/drive/MyDrive/Final Project/Databases/fer-2013/images'
    DIR_ANN_TRAIN = '/content/drive/MyDrive/Final Project/Databases/fer-2013/EmoLabel/Training.txt'
    DIR_ANN_DEV = '/content/drive/MyDrive/Final Project/Databases/fer-2013/EmoLabel/Test.txt'
    # index to class mapping
    index2class = {
            7: 'neutral',
            6: 'anger',
            3: 'disgust',
            2: 'fear',
            4: 'happiness',
            5: 'sadness',
            1: 'surprise',
            }

    # class to index mapping
    class2index = {
             'neutral': 7,
             'anger': 6,
             'disgust': 3,
             'fear': 2,
             'happiness': 4,
             'sadness': 5,
             'surprise': 1,
            }
