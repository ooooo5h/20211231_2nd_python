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
    sql = f"SELECT p.*, u.name AS writer_name FROM posts AS p JOIN users AS u ON p.user_id = u.id ORDER BY p.created_at DESC LIMIT {offset}, 5"
    # 쿼리 자체를 날릴 때, 너무 많은 정보는 필요없다 :: 포스트의 전체와 작성자의 이름만 가져오기
    
    cursors.execute(sql)
    result = cursors.fetchall()
    
    for row in result:
        
        row['reply_count'] = 0
    
    return result


# 전체 회원의 수 물어보는 함수 추가
def get_all_user_count():
    
    sql = f"SELECT COUNT(DISTINCT u.id) AS user_count FROM users AS u"
    
    cursors.execute(sql)
    result = cursors.fetchone()
       
    return result['user_count']


# 강의 목록과 평점을 같이 가져오는 함수 추가
def get_all_lectures():
    
    sql = f"""
    SELECT l.name, AVG(lr.score) AS avg_score 
    FROM lectures AS l 
    JOIN lecture_review AS lr ON l.id = lr.lecture_id
    GROUP BY l.id
    ORDER BY l.name;
    """
    
    cursors.execute(sql)
    result = cursors.fetchall()
    
    return result