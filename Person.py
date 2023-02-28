class Person:
    def __init__(self, name, last_name) -> None:
        self._name = name
        self._last_name = last_name

    def update_info(self, name, last_name):
        self._name = name
        self._last_name = last_name