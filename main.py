

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
            pass
        
show_main_menu()