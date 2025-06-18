from abc import ABC, abstractmethod
from typing import List
from Split.Split import Split


class ExpenseSplitStrategy(ABC):
    @abstractmethod
    def validate_split_request(self, split_list: List[Split], total_amount: float):
        pass
