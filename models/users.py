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
    # 이름 - ?세, 성별 (2021년 8월 5일 가입)
    def get_simple_info(self):
        print(f'{self.name} - {self.get_age()}세, {self.gender}')
        
        # datetime 양식을 우리가 원하는 형식의 str로 가공해보자
        temp_str = self.created_at.strftime('%Y년 %m월 %d일')
        print(f'가입일자 : {temp_str}')
        
    
    # 사용자의 나이 출력
    def get_age(self):
        
        current_year = datetime.datetime.utcnow().year
        return current_year - self.birth_year + 1