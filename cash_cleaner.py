from dataclasses import dataclass

def condition(bill: Bill): 
    return bill.amount == 100 and bill.currency == "$"

def validate_hundred(bill: Bill):
    return bill.amount == 100

def validate_dollar(bill: Bill):
    return bill.currency == "$"

def cash_cleaner_machine(bill_stack: list[Bill]) -> dict[list, list]:
    validators = [validate_hundred, validate_dollar]
    return {
        "accepted":[bill for bill in bill_stack if all(v(bill) for v in validators)],
        "rejected":[bill for bill in bill_stack if not all(v(bill) for v in validators)] 
    }

@dataclass
class Bill:
    amount: int
    currency: str = "$"