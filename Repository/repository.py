from typing import Protocol, Type, Union, Optional, List

from Domain.entity import Entity


class Repository(Protocol):
    def read(self, idEntity=None) -> Type[Union[Optional[Entity], List[Entity]]]:
        ...

    def add(self, entity: Entity) -> None:
        ...

    def delete(self, idEntity: str) -> None:
        ...

    def update(self, entity: Entity) -> None:
        ...
