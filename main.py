#
#
#
# def calcul_time(func):
#     import time
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         value = func(*args, **kwargs)
#         stop = time.time()
#         return value, stop - start
#
#     return wrapper
#
#
# @calcul_time
# def get_time(url):
#     import requests
#     return requests.get(url)
#
# url = 'https://tproger.ru/'
# print(get_time(url))
#
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie -= 3
        return method_to_decorate(self, lie)
    return wrapper

class Lucy:
    def __init__(self):
        self.age = 32
    @method_friendly_decorator
    def sayYourAge(self, lie):
        print(f"Мне {self.age+lie} лет, а ты бы сколько дал?")

l = Lucy()
l.sayYourAge(-3)
l.sayYourAge(-3)

