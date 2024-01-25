from abc import ABC, abstractmethod


class ICommandRepository(ABC):
    @abstractmethod
    def add_command(self, key: str, cmd: str, kwargs: [dict], args: []) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_command_by_id(self, id) -> dict:
        raise NotImplementedError

    @abstractmethod
    def get_command_by_name(self, name: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    def get_commands(self):
        raise NotImplementedError

    @abstractmethod
    def update_command(self, id: str, key: str, value) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_command(self, id: str) -> None:
        raise NotImplementedError
