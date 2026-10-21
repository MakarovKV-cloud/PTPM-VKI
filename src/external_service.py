from abc import ABC, abstractmethod


class ExternalService(ABC):
    """Абстрактный интерфейс сторонней зависимости."""

    @abstractmethod
    def send_data(self, data: str) -> bool:
        """Имитация отправки данных на внешний сервер."""
        ...


class EmailService(ExternalService):
    """Имитация email-сервера."""

    def __init__(self) -> None:
        self.sent_messages: list[str] = []

    def send_data(self, data: str) -> bool:
        self.sent_messages.append(data)
        print(f"[EmailService] Отправлено: {data}")
        return True