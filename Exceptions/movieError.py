from dataclasses import dataclass


@dataclass
class MovieError(Exception):
    message: any

    def __str__(self) -> str:
        return f'MovieError: {self.message}'
