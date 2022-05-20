
from paddleocr import PaddleOCR
import threading
from queue import Queue
import pickle

class Paddleocr(threading.Thread):

    def __init__(self, IMG_Url_Queue_paddleocr, result_queue, event,
                 *args,
                 **kwargs):
        super(
            Paddleocr,
            self).__init__(
            *
            args,
            **kwargs)
        self.IMG_Url_Queue_paddleocr = IMG_Url_Queue_paddleocr
        self.result_queue = result_queue
        self.lock = threading.Lock()
        self.event = event

    def result_heal_word(self, result):
        result_healeds = []
        for i in range(len(result[1])):
            result_healeds.append(result[1][i][1][0])
        return result_healeds

    def result_heal_number(self, result):
        result_healeds = []
        for i in range(len(result[1])):
            result_healeds.append(result[1][i][0])
        return result_healeds

    def run(self) -> None:
        self.lock.acquire()
        try:
            while True:
                if self.IMG_Url_Queue_paddleocr.qsize() == 0:
                    # print('生产者队列数量：',self.IMG_Url_Queue_paddleocr.qsize())
                    self.event.set()
                    break
                self.filepath = self.IMG_Url_Queue_paddleocr.get()
                ocr = PaddleOCR(use_angle_cls=True, use_gpu=False)
                # img_path = '/Users/mac/Desktop/text/ceshi/1.jpg'  #
                # 这个是自己的图片，自行放置在代码目录下修改名称
                result = ocr.ocr(self.filepath, cls=True)
                self.result_queue.put([self.filepath, result])
                print('消费者', self.result_queue.qsize())
        finally:
            self.lock.release()


class Csv_INTO(threading.Thread):

    def __init__(self, result_Queue, event, filename=None, *args, **kwargs):
        super(Csv_INTO, self).__init__(*args, **kwargs)
        self.result_queue = result_Queue
        self.event = event
        self.filename = filename

    def run(self) -> None:
        self.event.wait()
        results_dict = []
        while True:
            if self.result_queue.qsize() == 0:
                break
            # print("第三者数量：",self.result_queue.qsize())
            results_dict.append(self.result_queue.get())

        print(type(results_dict))

        filename = 'number.pickle'
        with open(self.filename, 'wb') as f:
            pickle.dump(results_dict, f)


def main(filepaths):

    IMG_Url_Queue = Queue(200)
    result_Queue = Queue(200)

    for filepath in filepaths:
        IMG_Url_Queue.put(filepath)

    event = threading.Event()
    for x in range(4):
        r2 = Paddleocr(
            IMG_Url_Queue_paddleocr=IMG_Url_Queue,
            result_queue=result_Queue,
            event=event)
        r2.start()
        r2.join()
    print(result_Queue.get())
    r3 = Csv_INTO(result_Queue=result_Queue, event=event)
    r3.start()
    r3.join()


if __name__ == '__main__':
    filepath = '/Users/mac/Desktop/test_data/day3'
    main(filepath)







    



