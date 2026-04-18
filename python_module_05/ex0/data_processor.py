from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data_queue: list[tuple[int, str]] = []
        self.rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data_queue:
            raise ValueError("No data to output")
        rank, data = self.data_queue.pop(0)
        return (rank, data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) and
                       not isinstance(item, bool)
                       for item in data)
        return False

    def ingest(self, data: Union[int, float, list[int]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, (int, float)):
            self.data_queue.append((self.rank, str(data)))
            self.rank += 1
        if isinstance(data, list):
            for item in data:
                self.data_queue.append((self.rank, str(item)))
                self.rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: Union[str, list[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, str):
            self.data_queue.append((self.rank, data))
            self.rank += 1

        if isinstance(data, list):
            for item in data:
                self.data_queue.append((self.rank, item))
                self.rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(i, str) and isinstance(j, str)
                       for i, j in data.items())
        if isinstance(data, list):
            return all(isinstance(item, dict) and
                       all(isinstance(i, str) and isinstance(j, str)
                           for i, j in item.items())
                       for item in data)
        return False

    def ingest(self, data: Union[dict[str, str],
                                 list[dict[str, str]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, dict):
            formated = (f"{data.get('log_level', '')}: "
                        f"{data.get('log_message', '')}")
            self.data_queue.append((self.rank, formated))
            self.rank += 1

        if isinstance(data, list):
            for item in data:
                formated = (f"{item.get('log_level', '')}: "
                            f"{item.get('log_message', '')}")
                self.data_queue.append((self.rank, formated))
                self.rank += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input'42': {numeric.validate(42)}")
    print(f"Trying to validate input'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string'foo' without prior validation:")
    try:
        numeric.ingest('foo')
    except ValueError as e:
        print(f"Got exception: {e}")

    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        rank, value = numeric.output()
        print(f"Numeic value {rank}: {value}")

    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input'42': {text.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(['Hello', 'Nexus', 'World'])
    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input'Hello': {log.validate('Hello')}")
    print("Processing data: [{'log_level': 'NOTICE',"
          "'log_message': 'Connection to server'}, {'log_level': 'ERROR',"
          "'log_message': 'Unauthorized access!!'}]")
    log.ingest([
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ])
    print("Extracting 2 values...")
    for i in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")
