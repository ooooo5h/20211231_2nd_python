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


# 페이지에 맞는 게시글 목록 가져오기
def get_posts(page):
    
    offset = (page - 1) * 5
    sql = f"SELECT * FROM posts AS p ORDER BY p.created_at DESC LIMIT {offset}, 5"
    
    cursors.execute(sql)
    result = cursors.fetchall()
    
    return result