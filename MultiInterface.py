class animal:

    def is_alive(self):
        pass

    def get_name(self):
        pass

    def get_weight(self):
        pass


class walk_animal(animal):
    def get_legs(self):
        pass


class fly_animal(walk_animal,animal ):
    def fly_avg_speed(self):
        pass


class reptile_animal(animal):
    def moving_speed(self):
        pass


# class Final(type):
# #     def __new__(cls, name, bases, classdict):
# #         for b in bases:
# #             if isinstance(b, Final):
# #                 raise TypeError("type '{0}' is not an acceptable base type".format(b.__name__))
# #         return type.__new__(cls, name, bases, dict(classdict))
# #
# # class C(metaclass=Final): pass
# #
# # class D(C): pass


if __name__ == "__main__":
    v = fly_animal()

