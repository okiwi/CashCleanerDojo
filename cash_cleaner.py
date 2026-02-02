from dataclasses import dataclass

def validate_hundred(bill: Bill):
    return bill.amount == 100

def validate_dollar(bill: Bill):
    return bill.currency == "$"

def validate_legitemite(bill: Bill):
    return bill.is_authentic

def cash_cleaner_machine(bill_stack: list[Bill]) -> dict[list, list]:
    validators = [validate_hundred, validate_dollar, validate_legitemite]
    return {
        "accepted":[bill for bill in bill_stack if all(v(bill) for v in validators)],
        "rejected":[bill for bill in bill_stack if not all(v(bill) for v in validators)] 
    }

def dry_machine (bill_stack: list[Bill]) -> list:
    for bill in bill_stack:
        bill.is_dry = True
    return bill_stack

@dataclass
class Bill:
    amount: int
    currency: str = "$"
    is_authentic: bool = True
    is_dry: bool = True