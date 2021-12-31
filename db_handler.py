from pymysql import connect
from pymysql import cursors
from pymysql.cursors import DictCursor

db = connect(
    host= 'finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
    port=3306,
    user='admin',
    passwd='Vmfhwprxm!123',
    db='test_202112_python',
    charset='utf8',
    cursorclass=DictCursor    
    )

cursors = db.cursor()


# 사용자 목록 가져오기
def get_user_list():
    sql = f"SELECT * FROM users"
    
    cursors.execute(sql)
    result = cursors.fetchall()
    
    return result