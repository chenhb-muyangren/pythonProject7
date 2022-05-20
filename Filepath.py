
import os

from imghdr import what

class Filepath(object):
    """
    获取文件夹里的目录
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.path = self.GetFilepath()
        self.JudgeImage()

    def GetFilepath(self):
        return [os.path.join(self.filepath, filepath)
                for filepath in os.listdir(self.filepath)]

    def JudgeImage(self):
        for path in self.path:

            if not str(
                    what(path)) in [
                       'png',
                       'jpg',
                       'jpeg']:  # if path isn't a image file,return
                self.path.remove(path)
                return self.path
            if os.path.isdir(path):
                self.path.remove(path)
                return self.path

    def True_filepath(self):
        number = []
        for item in self.path:
            number.append(int(str(item).split(".")[0][-3:]))
        number_min = min(number)
        number_max = max(number)

        True_filepaths = []
        for x in range(number_min, number_max):
            if x < 10:
                filepaths2 = self.path[1].split(".")[0][:-3] + '00{}'.format(x) + '.{}'.format(self.path[1].split(".")[1])
                True_filepaths.append(filepaths2)
            if x >= 10 and x < 100:
                filepaths2 = self.path[1].split(".")[0][:-3] + '0{}'.format(x) + '.{}'.format(self.path[1].split(".")[1])
                True_filepaths.append(filepaths2)
            if x >= 100:
                filepaths2 = self.path[1].split(".")[0][:-3] + '{}'.format(x) + '.{}'.format(self.path[1].split(".")[1])
                True_filepaths.append(filepaths2)

        return True_filepaths



if __name__ == '__main__':
    filepath='/Users/mac/Desktop/test_data/day2'
    r1=Filepath(filepath)
    True_filepaths=r1.True_filepath()
    print(True_filepaths)
    #filepaths=(PaddleOcr(filepath) for filepath in True_filepaths)















