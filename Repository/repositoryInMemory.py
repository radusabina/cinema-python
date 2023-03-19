from typing import Type, Union, Optional, List

from Domain.entity import Entity
from Exceptions.idErorr import DuplicateIdError, NoSuchIdError
from Repository.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entities = {}

    def read(self, idEntity=None) -> Type[Union[Optional[Entity],List[Entity]]]:
        if idEntity is None:
            return list(self.entities.values())
        if idEntity in self.entities:
            return self.entities[idEntity]
        else:
            return None

    def add(self, entity: Entity) -> None:
        if self.read(entity.idEntity) is not None:
            raise DuplicateIdError("There is already an entity with that id!")
        self.entities[entity.idEntity] = entity

    def delete(self, idEntity: str) -> None:
        if self.read(idEntity) is None:
            raise NoSuchIdError("There's no entity with the specified id!")
        del self.entities[idEntity]

    def update(self, entity: Entity) -> None:
        if self.read(entity.idEntity) is None:
            raise NoSuchIdError("There's no entity with the specified id!")
        self.entities[entity.idEntity] = entity
