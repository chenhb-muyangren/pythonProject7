import pickle

from paddleocr import PaddleOCR

import threading

from Filepath import Filepath

import pandas as pd

from MySQL import mysqlconn
import datetime

class Paddleocr(threading.Thread):

    def __init__(
            self,
            filepaths,
            *args,
            **kwargs):
        super(
            Paddleocr,
            self).__init__(
            *args,
            **kwargs)
        self.filepath_queue=filepaths

    def run(self) -> None:
        #filename = 'number3.pickle'
        while True:
            self.filepath=self.filepath_queue.get()
            ocr = PaddleOCR(use_angle_cls=True, use_gpu=False)
            # img_path = '/Users/mac/Desktop/text/ceshi/1.jpg'  # 这个是自己的图片，自行放置在代码目录下修改名称
            result = ocr.ocr(self.filepath, cls=True)
            try:
                filepath = [self.filepath] * len(result)
                left_botton = [str(item[0][0]) for item in result]
                right_botton = [str(item[0][1]) for item in result]
                right_top = [str(item[0][2]) for item in result]
                left_top = [str(item[0][3]) for item in result]
                word = [item[1][0] for item in result]

                data = {'filepath': filepath,
                        'left_botton': left_botton,
                        'right_botton': right_botton,
                        'right_top': right_top,
                        'left_top': left_top,
                        'word': word}
                df = pd.DataFrame(data=data)
                mysqlconn().to_sql('newtable12313', df)
            except:
                print(self.filepath)
                pass


if __name__ == '__main__':
    filepath = '/Users/mac/Desktop/test_data/day2'
    r1 = Filepath(filepath)
    True_filepaths = r1.True_filepath()
    r1 = Paddleocr(filepaths=True_filepaths)
    r1.start()













