import pandas as pd
from sqlalchemy import create_engine
class mysqlconn():

    def __init__(self):
        mysql_username = 'root'
        mysql_password = '12345678'
        # 填写真实数库ip
        host= 'localhost'
        port = 3306
        db = 'day2'
        # 初始化数据库连接,使用pymysql库
        self.engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(mysql_username, mysql_password, host, port,db))

    # 查询mysql数据库
    def query(self,newtable):
        sql = "select * from {}".format(newtable)
        df  = pd.read_sql_query(sql,self.engine)
        # df = pandas.read_sql(sql,self.engine)

        # 返回dateframe格式
        return df

    # 写入mysql数据库
    def to_sql(self,table,df):
        # 第一个参数是表名
        # if_exists:有三个值 fail、replace、append
        # 1.fail:如果表存在，啥也不做
        # 2.replace:如果表存在，删了表，再建立一个新表，把数据插入
        # 3.append:如果表存在，把数据插入，如果表不存在创建一个表！！
        # index 是否储存index列
        df.to_sql(table, con=self.engine, if_exists='append', index=False)


if __name__ =='__main__':
    # 创建 dateframe 对象
    df = pd.DataFrame([{'name':'小米','price':'3999','colour':'白色'},{'name':'华为','price':'4999','colour':'黑色'}])
    # result=pd.read_pickle('number.pickle')
    # df=PandasResult(results=result)
    # print(df)
    # 调用 mysqlconn 类的 to_sql() 方法
    mysqlconn().to_sql('newtable2',df)