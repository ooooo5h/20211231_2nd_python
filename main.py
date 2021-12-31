from db_handler import get_user_list
from models import Users

# 메인 메뉴 출력 기능(함수)
def show_main_menu():
    while True:
        print('======= 강의 관리 시스템 (LMS) =======')
        print('1. 수강생 목록 조회')
        print('0. 프로그램 종료')
        print('=====================================')
        num = int(input('메뉴 선택 : '))
        
        if num == 0:
            print('프로그램을 종료합니다.')
            break
        elif num == 1:
            get_user_list_from_db()
    

# 1번 누르면, DB에서 수강생 목록 조회를 요청하는 기능
def get_user_list_from_db():
    result = get_user_list() 
  
    for row in result:
        # print(row)    # row 한 줄 : 하나의 dictionary
        user = Users(row)
        user.get_simple_info()  # dictionary가 Users 객체로 변환되었는지 확인
        
show_main_menu()