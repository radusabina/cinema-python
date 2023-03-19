from dataclasses import dataclass


@dataclass
class ReservationError(Exception):
    message: any

    def __str__(self) -> str:
        return f'ReservationError: {self.message}'
