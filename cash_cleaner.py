from dataclasses import dataclass

def condition(bill: Bill): 
    return bill.amount == 100 and bill.currency == "$"

def cash_cleaner_machine(bill_stack: list[Bill]) -> dict[list, list]:
    return {
        "accepted":[bill for bill in bill_stack if condition(bill)],
        "rejected":[bill for bill in bill_stack if not condition(bill)] 
    }

@dataclass
class Bill:
    amount: int
    currency: str = "$"