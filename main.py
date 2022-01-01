from db_handler import get_user_list, get_posts, get_all_user_count, get_all_lectures
from models import Users
from models.posts import Posts

# 메인 메뉴 출력 기능(함수)
def show_main_menu():
    while True:
        print('======= 강의 관리 시스템 (LMS) =======')
        print('1. 수강생 목록 조회')
        print('2. 게시글 목록 조회')
        print('3. 강의 목록 조회')
        print('0. 프로그램 종료')
        print('=====================================')
        num = int(input('메뉴 선택 : '))
        
        if num == 0:
            print('프로그램을 종료합니다.')
            break
        
        elif num == 1:
            get_user_list_from_db()
            
        elif num == 2:       
            page_num = int(input('몇 페이지를 보시겠습니까? : '))
            get_posts_by_page_from_db(page_num)
            
        elif num == 3:
            get_lectures_from_db()
    

# 1번 누르면, DB에서 수강생 목록 조회를 요청하는 기능
def get_user_list_from_db():
    
    result = get_user_list() 
  
    for row in result:
        # print(row)    # row 한 줄 : 하나의 dictionary
        user = Users(row)
        user.get_simple_info()  # dictionary가 Users 객체로 변환되었는지 확인
        
   
   # DB한번 더 접근해서, 인원수 가져오기(리턴되는 숫자를 user_count에 담음) 
    user_count = get_all_user_count()  
    print(f'총 수강생 : {user_count}명')   
    
     
        
# 2번 누르면, DB에서 게시글을 페이지에 맞게 요청하는 기능
def get_posts_by_page_from_db(page):
    result =  get_posts(page)

    for row in result:
        # print(row)
        post = Posts(row)
        post.get_simple_post()



# 3번 누르면, DB에서 강의목록과 강의별 평균 점수 요청하는 기능
def get_lectures_from_db():
    query_result = get_all_lectures()

    print(query_result)

show_main_menu()