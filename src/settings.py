import json

class Settings:
    def __init__(self, settings_file):
        self.settings_file = settings_file
        self.client_id = None
        self.client_secret = None
        self.username = None
        self.password = None
        self.user_agent = None
    
    def parse_settings(self):
        try:
            data = None
            with open(self.settings_file, 'r') as f:
                data = json.loads(f.read())
            
            self.client_id = data["client_id"]
            self.client_secret = data["client_secret"]
            self.username = data["username"]
            self.password = data["password"]
            self.user_agent = data["user_agent"]
        except Exception as e:
            print(e)