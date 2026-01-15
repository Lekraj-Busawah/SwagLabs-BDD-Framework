import configparser

config = configparser.RawConfigParser()
config.read('configurations/config.ini')

class ReadConfig:
    @staticmethod
    def get_browser():
        browser = config.get('common info', 'browser')
        return browser

    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url
    
    @staticmethod
    def get_user_email():
        username = config.get('common info', 'username')
        return username


    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
    
    @staticmethod
    def get_headless_mode():
        try:
            headless = config.get('common info', 'headless')
            return headless.lower() == 'true'
        except:
            return False