class Singleton:
    __instance = None

    def __int__(self):
        self.some_attr = 1

    @staticmethod
    def get_inst():
        if Singleton.__instance is None:
            Singleton.__instance = Singleton()
        return Singleton.__instance


singleton1 = Singleton.get_inst()
singleton2 = Singleton.get_inst()

print(singleton1 is singleton2)
