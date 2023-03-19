from dataclasses import dataclass


@dataclass
class ClientCardError(Exception):
    message: any

    def __str__(self) -> str:
        return f'CardClientError: {self.message}'
