import datetime

class Users:
    
    def __init__(self, dict_info):
        self.id = dict_info['id']
        self.name = dict_info['name']
        self.birth_year = dict_info['birth_year']
        self.address = dict_info['address']
        self.gender = dict_info['gender']
        self.height = dict_info['height']
        self.created_at = dict_info['created_at']
        self.friend_id = dict_info['friend_id']
        
    
    # 사용자 정보를 간단하게 가공해서 출력
    # 이름 - ?세, 성별 (210805 가입)
    # 가입일로부터 50일이 지나면, 정회원으로 취급하려고한다
    # 2021년 10월 10일 정회원 등록 예정 ==> datetime으로부터 50일이 지난 날짜 (덧셈/뺄셈)
    def get_simple_info(self):
        
        temp_date = self.created_at.strftime('%y%m%d')
        print(f'{self.name} - {self.get_age()}세, {self.gender} ({temp_date} 가입)')
            
        # timedelta체험해보자 ==> 몇일을 더해줄 지 변수에 저장
        add_day = datetime.timedelta(days=50)
        print(f'정회원 일자 : {self.created_at + add_day } ')
    
    
    # 사용자의 나이 출력
    def get_age(self):
        
        current_year = datetime.datetime.utcnow().year
        return current_year - self.birth_year + 1