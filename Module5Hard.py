class UrTube:
    users = list()
    videos_title = list()
    videos = list()
    def __new__(cls,*arg,**kwargs):
        return object.__new__(cls)


    def __init__(self):
        self.current_user = None



    def register(self, username,password,age):
        self.username = username
        if len(self.users) > 0:
            for i in range(len(self.users)):
                if self.username == self.users[i].username:
                    print(f'Пользователь {username} уже существует')
                    return
        user_new = User(username,password,age)
        self.users.append(user_new)
        return self.log_in(username,password)


    def add (self,*args):
        for i in args:
            if i.title in self.videos_title:
                continue
            else:
                self.videos_title.append(i.title)
                self.videos.append(i)

    def get_videos (self,searh_words):
        get_list = list()
        for i in self.videos_title:
            if searh_words.lower() in i.lower():
                get_list.append(i)
        return get_list

    def log_in (self,username,password):
        for i in range(len(self.users)):
            if (self.username == self.users[i].username
                    and hash(password) == self.users[i].password):
                self.current_user = self.users[i]
                return self.current_user
            else:
                self.current_user = None



    def watch_video (self,title):
        if self.current_user == None:
            print('Войдите в аккаунт чтобы смотреть видео')
        else:
            if title in self.videos_title:
                import time
                i = self.videos_title.index(title)
                if (self.videos[i].adult_mode == True and
                       self.current_user.user_age < 18):
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    j = self.videos[i].time_now
                    for j in range(self.videos[i].duration):
                        print(j,' ',end="")
                        time.sleep(1)
                    print('Конец видео')

            else:
                print('Видео не найдено') # Или, по условию задачи, не прописывать "else" совсем


class Video:
    def __init__(self,title,duration,adult_mode=False):
        self.time_now = 0
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode





class User:
    def __init__(self,username,password,age):
        self.username = username
        self.password = hash(password)
        self.user_age = age

    def __str__(self):
        return f'{self.username}'





ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2, v3)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')