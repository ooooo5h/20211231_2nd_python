class Lecture:
    
    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.avg_score = round(data_dict['avg_score'], 1)