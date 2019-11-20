from decoripy import AbstractDecorator


class DecoratorWithoutParameters(AbstractDecorator):

    def __do_before__(self, *args, **kwargs):
        print("Executing: __do_before__")
        return "Executed: __do_before__"

    def __do__(self, *args, **kwargs):
        print(self.before_result, ", Executing: __do__")
        function_result = self.function(*args, **kwargs)
        return function_result + ", Executed: __do__"

    def __do_after__(self, *args, **kwargs):
        print(self.execution_result, ", Executing: __do_after__")
        return "Executed: __do_after__"


@DecoratorWithoutParameters
def function_to_decorate1(var1, var2, dict_var1, dict_var2):
    print("Executing: function: ", var1, var2, dict_var1, dict_var2)
    return "Executed: function"


class DecoratorWithParameters(AbstractDecorator):

    def __do_before__(self, *args, **kwargs):
        if self.execute_before:
            print("Executing: __do_before__")
            return "Executed: __do_before__"

    def __do__(self, *args, **kwargs):
        # Non-existing params -> error!
        try:
            if self.execute_do:
                print(self.before_result, ", Executing: __do__")
                function_result = self.function(*args, **kwargs)
                return function_result + ", Executed: __do__"
        except AttributeError:
            self.function(*args, **kwargs)

    def __do_after__(self, *args, **kwargs):
        if self.execute_after:
            print(self.execution_result, ", Executing: __do_after__")
            return "Executed: __do_after__"


@DecoratorWithParameters(3, execute_before=False, execute_after=False)
def function_to_decorate2(var1, var2, dict_var1, dict_var2):
    print("Executing: function: ", var1, var2, dict_var1, dict_var2)
    return "Executed: function"


if __name__ == "__main__":
    function_to_decorate1(1, "var2", dict_var1=[1, 2, 3], dict_var2={"key": "value"})
    function_to_decorate2(1, "var2", dict_var1=[1, 2, 3], dict_var2={"key": "value"})
