#Mixins
# миксины - это классы которые будут использоваться для наследования, но от этих миксинов не создают объекты
# Для чего:
# 1) вы хотите предоставить множнство доп методов класса
# 2) вы хотите использовать одну корректную функцию во множестве разных классов

# class Machines:
#     def start_engine(self):
#         print('stared engine')

# class RatioMixin:
#     def play_ratio(self):
#         print('music is playing')

# class Auto(RatioMixin, Machines):
#     pass

# class Plane(Machines):
#     pass

# class Train(RatioMixin, Machines):
#     pass

# obj = Auto()
# obj2 = Plane()
# obj3 = Train()

# obj.start_engine()
# obj2.start_engine()
# obj3.start_engine()

# obj.start_engine()
# obj3.start_engine()

