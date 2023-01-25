class TelegramUser:
    def __init__(self, username , firstname, lastname,is_active, chat_id):
        self._username = username
        self._firstname = firstname
        self._lastname = lastname
        self._is_active = is_active
        self._chat_id = chat_id

    def get_user(self):
        return print(f'Welcome: {self._username}, {self._firstname},{self._lastname}, {self._is_active}, {self._chat_id}')

    def set_user(self, username, firstname, lastname, is_active, chat_id):
        self._username = username
        self._firstname = firstname
        self._lastname = lastname
        self._is_active = is_active
        self._chat_id = chat_id


user = TelegramUser("bob ","bobinski ", " "," "," ")
user.get_user()
user1 = user.set_user("nice","joi","division","active","hello")
user.get_user()
print(user)
print(user1)