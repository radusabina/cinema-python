from dataclasses import dataclass


@dataclass
class NoSuchIdError(Exception):
    message: any

    def __str__(self) -> str:
        return f'NoSuchIdError: {self.message}'


@dataclass
class DuplicateIdError(Exception):
    message: any

    def __str__(self) -> str:
        return f'DuplicateIdError: {self.message}'
