from functools import partial
from abc import ABCMeta


class AbstractDecorator:
    """ AbstractDecorator is """

    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs):
        if args and callable(args[0]):
            self.function = args[0]
            self.args = None
            self.kwargs = None
        else:
            self.function = None
            self.args = args
            self.kwargs = kwargs
            self.__set_kwargs__()
        self.before_result = None
        self.execution_result = None
        self.after_result = None

    def __call__(self, *args, **kwargs):
        if args and callable(args[0]):
            self.function = args[0]

            def wrapper(*func_args, **func_kwargs):
                return self.__execute_function__(*func_args, **func_kwargs)
            return wrapper
        else:
            return self.__execute_function__(*args, **kwargs)

    def __get__(self, instance, owner):
        return partial(self.__call__, instance)

    def __execute_function__(self, *func_args, **func_kwargs):
        self.before_result = self.__do_before__(*func_args, **func_kwargs)
        self.execution_result = self.__do__(*func_args, **func_kwargs)
        self.after_result = self.__do_after__(*func_args, **func_kwargs)
        return self.execution_result

    def __set_kwargs__(self):
        for key, value in self.kwargs.items():
            setattr(self, key, self.kwargs[key])

    def __do_before__(self, *args, **kwargs):
        pass

    def __do__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

    def __do_after__(self, *args, **kwargs):
        pass
