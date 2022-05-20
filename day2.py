import pickle
import datetime
with open('number3.pickle','rb') as f:
    result=pickle.load(f)
print([1]*10)
left_botton=[str(item[0][0]) for item in result]
right_botton=[str(item[0][0]) for item in result]
right_top=[str(item[0][0]) for item in result]
left_top=[str(item[0][0]) for item in result]

word=[item[1][0] for item in result]
# print(word)
# print(datetime.datetime.now())
