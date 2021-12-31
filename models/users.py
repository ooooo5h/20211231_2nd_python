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
    def get_simple_info(self):
        
        temp_date = self.created_at.strftime('%y%m%d')
        print(f'{self.name} - {self.get_age()}세, {self.gender} ({temp_date} 가입)')
              
    
    # 사용자의 나이 출력
    def get_age(self):
        
        current_year = datetime.datetime.utcnow().year
        return current_year - self.birth_year + 1