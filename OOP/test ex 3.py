from abc import ABC, abstractmethod
from datetime import datetime

class Handler(ABC):
    @abstractmethod
    def emit(self, message: str):
        pass


class ConsoleHandler(Handler):
    def emit(self, message):
        print(message)

class FileHandler(Handler):
    def emit(self, message):
        return f"Запись в файл: {message}"


class TimeMixin: 
    def format_with_timestamp(self, message: str):
        return f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{message}]"

class Logger(TimeMixin):
    def __init__(self, handlers: list):
        self._handlers = handlers

    def log(self, message: str):
        a = self.format_with_timestamp(message)
        for x in self._handlers:
            x.emit(a)

    def __call__(self, message: str):
        self.log(message)


    