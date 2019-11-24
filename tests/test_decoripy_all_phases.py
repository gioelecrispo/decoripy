from decoripy import AbstractDecorator


class DecoratorWithParameters(AbstractDecorator):

    def __do_before__(self, *args, **kwargs):
        var = self.args[0]  # 1
        return var + 1

    def __do__(self, *args, **kwargs):
        assert self.before_result == 2
        return self.function(*args, **kwargs)

    def __do_after__(self, *args, **kwargs):
        return self.before_result + 1


@DecoratorWithParameters(1, execute_before=False, execute_after=False)
def function_to_decorate(var1, var2, dict_var1, dict_var2):
    return str(var1) + ", " + str(var2) + ", " + str(dict_var1) + ", " + str(dict_var2)


def test_decorator_with_parameter():
    function_result = function_to_decorate(1, "var2", dict_var1=[1, 2, 3], dict_var2={"key": "value"})
    assert function_result == "1, var2, [1, 2, 3], {'key': 'value'}"


class DecoratorWithoutParameters(AbstractDecorator):

    def __do_before__(self, *args, **kwargs):
        return None

    def __do__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

    def __do_after__(self, *args, **kwargs):
        return None


@DecoratorWithoutParameters
def function_to_decorate2(var1, var2, dict_var1, dict_var2):
    return str(var1) + ", " + str(var2) + ", " + str(dict_var1) + ", " + str(dict_var2)


def test_decorator_without_parameters():
    function_result = function_to_decorate2(1, "var2", dict_var1=[1, 2, 3], dict_var2={"key": "value"})
    assert function_result == "1, var2, [1, 2, 3], {'key': 'value'}"
