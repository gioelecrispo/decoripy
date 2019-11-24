import threading
import time


from decoripy import AbstractDecorator


class BeforePhaseDecorator(AbstractDecorator):

    def __do_before__(self, *args, **kwargs):
        tester = args[0]
        tester.config["value"] = 10


class TestBeforePhaseDecorator:

    def __init__(self):
        self._id = "before"
        self.config = {"value": 0}

    @BeforePhaseDecorator
    def do(self):
        return "before"


def test_before_phase():
    t = TestBeforePhaseDecorator()
    result = t.do()
    assert result == "before"
    assert t.config["value"] == 10


class ExecutionPhaseDecorator(AbstractDecorator):

    def __do__(self, *args, **kwargs):
        tester = args[0]
        job_thread = threading.Thread(target=self.function, args=(tester,))
        job_thread.start()
        return job_thread


class TestExecutionPhaseDecorator:

    def __init__(self):
        self._id = "execution"
        self.config = {"run": True}

    @ExecutionPhaseDecorator
    def do(self):
        while self.config["run"]:
            time.sleep(0.5)


def test_execution_phase():
    t = TestExecutionPhaseDecorator()
    thread_control = t.do()
    t.config["run"] = False
    thread_control.join(1)
    assert thread_control is not None


class AfterPhaseDecorator(AbstractDecorator):

    def __do_after__(self, *args, **kwargs):
        tester = args[0]
        tester.config["value"] = 10


class TestAfterPhaseDecorator:

    def __init__(self):
        self._id = "after"
        self.config = {"value": 0}

    @AfterPhaseDecorator
    def do(self):
        return "after"


def test_after_phase():
    t = TestAfterPhaseDecorator()
    result = t.do()
    assert result == "after"
    assert t.config["value"] == 10
