from typing import Type, Union, Optional, List

import jsonpickle

from Domain.entity import Entity
from Repository.repositoryInMemory import RepositoryInMemory


class RepositoryJson(RepositoryInMemory):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __readFile(self):
        try:
            with open(self.filename, "r") as f:
                file = f.read()
                return jsonpickle.loads(file)
        except Exception:
            return {}

    def __writeFile(self):
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.entities, indent=2))

    def read(self, idEntity=None) -> Type[Union[Optional[Entity], List[Entity]]]:
        self.entities = self.__readFile()
        return super().read(idEntity)

    def add(self, entity: Entity) -> None:
        self.entities = self.__readFile()
        super().add(entity)
        self.__writeFile()

    def delete(self, idEntity: str) -> None:
        self.entities = self.__readFile()
        super().delete(idEntity)
        self.__writeFile()

    def update(self, entity: Entity) -> None:
        self.entities = self.__readFile()
        super().update(entity)
        self.__writeFile()
