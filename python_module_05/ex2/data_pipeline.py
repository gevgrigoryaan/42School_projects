from abc import ABC, abstractmethod
from typing import Any, Union, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        csv_line = ','.join(value for rank, value in data)
        print("CSV Output:")
        print(csv_line)


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return

        json_dict = {f"item_{rank}": value for rank, value in data}
        json_str = "{"
        items = []
        for key, value in json_dict.items():
            items.append(f'"{key}": "{value}"')
        json_str += ", ".join(items)
        json_str += "}"
        print("JSON Output:")
        print(json_str)


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            data: list[tuple[int, str]] = []
            for _ in range(nb):
                if processor.data_queue:
                    data.append(processor.output())
            plugin.process_output(data)
    
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
    print("=== Code Nexus - Data Pipeline ===")

    print("\nInitialize Data Stream...")
    stream = DataStream()
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering Processors")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

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

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()
    
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nSend another batch of data: [21, ['I love AI', "
          "'LLMs are wonderful', 'Stay healthy'], "
          "[{'log_level': 'ERROR', 'log_message': "
          "'500 server crash'}, {'log_level': "
          "'NOTICE', 'log_message': 'Certificate "
          "expires in 10 days'}], [32, 42, 64, "
          "84, 128, 168],'World hello']")
    second_batch = [
            21,
            ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
            [
                {'log_level': 'ERROR',
                'log_message': '500 server crash'},
                {'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'}
            ],
            [32, 42, 64, 84, 128, 168],
            'World hello'
            ]
    stream.process_stream(second_batch)
    print('\n== DataStream statistics ==')
    stream.print_processors_stats()
    
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)
    
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()
