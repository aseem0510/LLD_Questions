from typing import List
from Split.Split import Split
from Split.ExpenseSplitStrategy import ExpenseSplitStrategy


class EqualExpenseSplit(ExpenseSplitStrategy):
    def validate_split_request(self, split_list: List[Split], total_amount: float):
        if not split_list:
            raise ValueError("Split list cannot be empty")

        amount_should_be_present = total_amount / len(split_list)

        for split in split_list:
            if abs(split.amount_owe - amount_should_be_present) > 1e-6:  # Use tolerance for float comparison
                raise ValueError("Each person should have an equal split")
