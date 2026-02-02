from cash_cleaner import Bill, cash_cleaner_machine, dry_machine


def test_return_hundred_bills():
    bill_stack = [Bill(amount) for amount in [100, 50, 100, 20, 10, 5, 1]]
    
    assert cash_cleaner_machine(bill_stack) == {
        "accepted":[Bill(100, "$"), Bill(100, "$")], 
        "rejected":[Bill(amount, "$") for amount in [50, 20, 10, 5, 1]]
        }
    
def test_return_hundred_dollar_bills():

    bill_stack = [Bill(100, "€"), Bill(20, "$"), Bill(50, "€"), Bill(100, "$")]

    assert cash_cleaner_machine(bill_stack) == {
        "accepted":[Bill(100, "$")], 
        "rejected":[Bill(100, "€"), Bill(20, "$"), Bill(50, "€")]
    } 

def test_return_hundred_dollar_authentic_bills():

    bill_stack = [Bill(100, "$", False), Bill(20, "$"), Bill(50, "€"), Bill(100, "$")]

    assert cash_cleaner_machine(bill_stack) == {
        "accepted":[Bill(100, "$")], 
        "rejected":[Bill(100, "$", False), Bill(20, "$"), Bill(50, "€")]
    } 

def test_dry_bills():
    bill_stack = [Bill(100), Bill(20, is_dry=False), Bill(50), Bill(100, is_dry=False)]

    assert dry_machine(bill_stack) == [Bill(100), Bill(20), Bill(50), Bill(100)]