class TelegramUser:
    def __init__(self, username, firstname, lastname, is_active, chat_id):
        self._username = username
        self._firstname = firstname
        self._lastname = lastname
        self._is_active = is_active
        self._chat_id = chat_id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, name):
        self._username = name

    @property
    def first(self):
        return self._firstname

    @first.setter
    def first(self, first):
        self._firstname = first

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, last):
        self._lastname = last

    @property
    def active(self):
        return self._is_active

    @active.setter
    def active(self, active):
        self._is_active = active

    @property
    def chat_id(self):
        return self._chat_id



