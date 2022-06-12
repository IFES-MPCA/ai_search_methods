import os.path
from pathlib import Path
from typing import Optional

import pandas


class ReportResult:
    def __init__(self, n_exec: int, n_rows: int, n_cols: int, seed: Optional[int] = None):
        self.__columns__ = ['método', 'média (ms)', 'desvio (ms)', 'desvio (%)', 'custo caminho', 'nós gerados', 'nós expandidos']
        self.file_name = self.__get_file_name__(n_exec, n_rows, n_cols, seed)
        self.directory = './results/'
        self.file_path = os.path.join(self.directory, self.file_name)
        self.__create_empty__()

    def __create_empty__(self):
        if os.path.exists(self.file_path):
            return

        file_path = Path(self.directory)
        file_path.mkdir(parents=True, exist_ok=True)

        result_df = pandas.DataFrame([], columns=self.__columns__)
        result_df.to_csv(self.file_path)

    def append_line(self, method: str, time_mean: float, time_std: float, cost: float, n_generated: int, n_expanded: int):
        columns_value = [method, time_mean, time_std, time_std / time_mean * 100, cost, n_generated, n_expanded]
        line_df = pandas.DataFrame([columns_value], columns=self.__columns__)
        line_df.to_csv(self.file_path, mode='a', header=False, float_format='%.2f')

    def __get_file_name__(self, n_exec: int, n_rows: int, n_cols: int, seed: Optional[int] = None):
        return f'exec-{n_exec}_{n_rows}x{n_cols}_seed-{seed}.csv'
