from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data_queue: list[tuple[int, str]] = []
        self.rank: int = 0
        self.total_processed: int = 0

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
            self.total_processed += 1

        if isinstance(data, list):
            for item in data:
                self.data_queue.append((self.rank, str(item)))
                self.rank += 1
                self.total_processed += 1


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
            self.total_processed += 1

        if isinstance(data, list):
            for item in data:
                self.data_queue.append((self.rank, item))
                self.rank += 1
                self.total_processed += 1


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
            self.total_processed += 1

        if isinstance(data, list):
            for item in data:
                formated = (f"{item.get('log_level', '')}: "
                            f"{item.get('log_message', '')}")
                self.data_queue.append((self.rank, formated))
                self.rank += 1
                self.total_processed += 1


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    processed = True
                    break
            if not processed:
                print(f"DataStream error - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
            return
        for processor in self.processors:
            processor_name = processor.__class__.__name__
            remaining = len(processor.data_queue)
            print(f"{processor_name}: total {processor.total_processed} "
                  f"items processed, remaining {remaining} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    stream = DataStream()
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    numeric = NumericProcessor()
    stream.register_processor(numeric)

    print("\nSend first batch of data on stream: "
          "['Hello world', [3.14, -1, 2.71], "
          "[{'log_level': 'WARNING', \n\t'log_message': "
          "'Telnet access! Use ssh instead'}, "
          "{'log_level': 'INFO', 'log_message': "
          "'User wil is \n\tconnected'}], 42, ['Hi', 'five']]")
    first_batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]
    stream.process_stream(first_batch)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(first_batch)
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nConsume some elements from the "
          "data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        rank, value = numeric.output()
    for _ in range(2):
        rank, value = text.output()
    for _ in range(1):
        rank, value = log.output()

    print("== DataStream statistics ==")
    stream.print_processors_stats()
