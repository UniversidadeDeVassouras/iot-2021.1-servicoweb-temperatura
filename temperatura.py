from datetime import datetime


class Temperatura:

    def __init__(self, id: int, dispositivo_id: int, valor: float, data: datetime):
        self.__id = id
        self.__dispositivo_id = dispositivo_id
        self.__valor = valor
        self.__data = data

    @property
    def id(self) -> int:
        return self.__id

    @property
    def dispositivo_id(self) -> int:
        return self.__dispositivo_id

    @dispositivo_id.setter
    def dispositivo_id(self, value: int) -> None:
        self.__dispositivo_id = value

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, value: float) -> None:
        self.__valor = value

    @property
    def data(self) -> datetime:
        return self.__data

    @data.setter
    def data(self, value: datetime) -> None:
        self.__data = value

    def toDict(self) -> dict:
        return {
            "id": self.__id,
            "dispositivo_id": self.__dispositivo_id,
            "valor": self.__valor,
            "data": self.__data.strftime('%d/%m/%Y %H:%M')
        }
