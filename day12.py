import pandas as pd
import pickle
import numpy as np





def PandasResult(results):
    # filepath = "number.pickle"

    xy_coordinates = [results[y][1][x][0] for y in range(
        len(results)) for x in range(len(results[y][1]))]
    result_word = [results[y][1][x][1][0] for y in range(
        len(results)) for x in range(len(results[y][1]))]
    ZHI_Xin_DU = [results[y][1][x][1][1] for y in range(
        len(results)) for x in range(len(results[y][1]))]
    filepaths = [results[y][0] for y in range(len(results))]
    count = [len(results[y][1]) for y in range(len(results))]

    def filepath(filepaths, count):
        file_path = []
        for x in range(len(filepaths)):
            for y in range(count[x]):
                file_path.append(filepaths[x])
        return file_path

    file_path = filepath(filepaths, count)
    data = [[file_path[j], xy_coordinates[j], result_word[j], ZHI_Xin_DU[j]]
            for j in range(len(file_path))]
    dataframe = pd.DataFrame(data, columns=['文件路径', '坐标', '结果', '置信度'])
    dataframe['起点坐标'] = [dataframe['坐标'][q][0]
                         for q in range(len(dataframe['坐标']))]
    # dataframe.to_excel('data4.xls',sheet_name='data')
    return dataframe

def main():
    def results():
        filepath = "number.pickle"
        with open(filepath, 'rb') as f:
            results = pickle.load(f)
        return results

    df = PandasResult(results())
    results = results()
    df["特征值"] = pd.factorize(df["结果"])[0].astype(np.uint16)
    # print(df.iloc[1])
    # print(len(df))
    world =  [list(df.iloc[x]) for x in range(len(df))]

    return world


if __name__ == '__main__':
    result=main()
    #print(result)
    for (row, customer) in enumerate(result):
        print((row, customer))
        for column in range(len(customer)):
            print(customer[column])
        break

        # results_filepaths = [results[i][0] for i in range(len(results))]
        # word_1 = list(df[df['文件路径'] == results_filepaths[0]]['坐标'])
        # word_2 = list(df[df['文件路径'] == results_filepaths[1]]['坐标'])
        # # x1=[word_1[x][y][0]for x in range(len(word_1)) for y in range(4)]
        # # y1=[word_1[x][y][1]for x in range(len(word_1)) for y in range(4)]
        # #
        # #
        # # x2 = [word_2[x][y][0] for x in range(len(word_2)) for y in range(4)]
        # # y2 = [word_2[x][y][1] for x in range(len(word_2)) for y in range(4)]
        # # plt.scatter(x1, y1,marker = 'x',color = 'blue')
        # # plt.scatter(x2, y2,marker = '+',color = 'red')
        # #
        # # plt.show()
        # for img_path in results_filepaths:
        #     img = cv2.imread(img_path)
        #     size = img.shape
        #     w = img.shape[1]
        #     h = img.shape[0]
        #     print('图片宽:{}，长:{}'.format(w,h))

