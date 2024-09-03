from time import sleep


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        UrTube.users.append(self)

    def __str__(self):
        return self.nickname


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration

    def __str__(self):
        return self.title


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname and hash(password) == i.password:
                self.current_user = i

    def register(self, nickname, password, age):
        is_prime = False
        for i in self.users:
            if i.nickname == nickname:
                is_prime = True
        if is_prime:
            print(f'Пользователь {nickname} уже существует')
        else:
            User(nickname, password, age)
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, string):
        names = []
        for i in self.videos:
            if string.lower() in str(i.title).lower():
                names.append(i.title)
        return names

    def watch_video(self, title):
        if self.current_user is not None:
            if self.current_user.age > 18:
                for i in self.videos:
                    if title in i.title:
                        for j in range(1, 11):
                            print(j, end=' ')
                            sleep(1)
                        print('Конец видео')
            else:
                print(f'Вам нет 18 лет. Пожалуйста покиньте страницу')
        else:
            print(f'Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

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