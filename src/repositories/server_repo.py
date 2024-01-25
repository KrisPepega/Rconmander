from abc import ABC, abstractmethod


class IServerRepository(ABC):
    @abstractmethod
    def add_server(
        self, iid: str, ip: str, port: int, password: str, game: str
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_server_by_id(self, id) -> dict:
        raise NotImplementedError

    @abstractmethod
    def update_server(self, id: str, key: str, value) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_server(self, id: str) -> None:
        raise NotImplementedError
