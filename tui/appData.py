class AppData:
    userName='Emeka'
    @classmethod
    def modifyUserName(cls,u):
        AppData.userName=u
    def getUsername(cls):
        return cls.userName