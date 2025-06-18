from typing import List
from Split.Split import Split
from Split.ExpenseSplitStrategy import ExpenseSplitStrategy


class PercentageExpenseSplit(ExpenseSplitStrategy):
    def validate_split_request(self, split_list: List[Split], total_amount: float):
        total_percentage = sum(split.amount_owe for split in split_list)
        
        if abs(total_percentage - 100.0) > 1e-6:  # Use tolerance to handle float precision issues
            raise ValueError("Total percentage must sum up to 100%")
