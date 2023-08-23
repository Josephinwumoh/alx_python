from sqlalchemy import create_engine
import sys

mouse=  sys.argv[1]
password= sys.argv[2]
hbtn_0e_6_usa= sys.argv[3]


path = "mysql + mysqldb://{}:{}@localhost/{}".format(mouse, password, hbtn_0e_6_usa)

database = create_engine(path)
connection = database.connect()
