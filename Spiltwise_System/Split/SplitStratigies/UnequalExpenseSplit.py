from typing import List
from Split.Split import Split
from Split.ExpenseSplitStrategy import ExpenseSplitStrategy


class UnequalExpenseSplit(ExpenseSplitStrategy):
    def validate_split_request(self, split_list: List[Split], total_amount: float):
        total_split_amount = sum(split.amount_owe for split in split_list)
        
        if abs(total_split_amount - total_amount) > 1e-6:  # Use tolerance for float precision
            raise ValueError("Split amounts do not match the total amount")
