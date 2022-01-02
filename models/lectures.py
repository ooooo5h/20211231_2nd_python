class Lecture:
    
    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.id = data_dict['id']
        
        self.avg_score = data_dict['avg_score']