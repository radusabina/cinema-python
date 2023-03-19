from dataclasses import dataclass


@dataclass
class CNPError(Exception):
    message: any

    def __str__(self) -> str:
        return f'CNPError: {self.message}'
