
Sample ="""
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

"""[1:-1]

def test_CheckEntryFourthLineIsBlank_IsTrue():

    # Arrange
    entry = """ |
                |
                |

            """
    # Act
    expected = CheckEntryFourthLineIsBlank(entry)

    # Assert
    assert (expected)

def test_CheckLineIsLenght27():

    # Arrange
    entry = """
|||||||||||||||||||||||||||
                           
___________________________

            """
    # Act
    expectedLine1 = CheckLineIsValidLength(entry.splitlines()[1])
    expectedLine2 = CheckLineIsValidLength(entry.splitlines()[2])
    expectedLine3 = CheckLineIsValidLength(entry.splitlines()[3])
    # Assert
    assert (expectedLine1)
    assert (expectedLine2)
    assert (expectedLine3)

def test_InvalidCharactersInEntry():

    # Arrange
    entry = """
|||||||||||||||||||||||||||
                           
AA_________________________

"""
    # Act
    expected = CheckOnlyValidCharacters(entry)
    # Assert
    assert (not expected)


def CheckEntryFourthLineIsBlank(entry):

    return  entry.splitlines()[3] == ""

def CheckLineIsValidLength(entry):

    return len(entry) == 27
    
def CheckOnlyValidCharacters(entry):
    return all(c in " |_\n" for c in entry)

def test_DigitRecognizer():
    #Arrange
    entryDigit = """
 _ 
|_|
|_|
"""
    FlatEntryDigit = entryDigit.replace("\n", "")
    #Act
    expected = DigitRecognizer(FlatEntryDigit)
    #Assert
    assert(expected==8)
   
def DigitRecognizer(entry):
    digits = {
        " _ | ||_|": 0,
        "     |  |": 1,
        " _  _||_ ": 2,
        " _  _| _|": 3,
        "   |_|  |": 4,
        " _ |_  _|": 5,
        " _ |_ |_|": 6,
        " _   |  |": 7,
        " _ |_||_|": 8,
        " _ |_| _|": 9
    }
    return digits.get(entry, "?")

def test_ExtractDigitFromEntry():

    # Arrange
    entry = """
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|

"""

    # Act
    expectedInt = ExtractEntryToInt(entry)
    # Assert
    assert (expectedInt==123456789)

def test_ReadEntryFromFile():
    # Act
    actuelDigits = ReadEntryFromFile(Sample)

    exceptedDigits = [123456789, 123456789, 123456789, 123456789]

    # Assert
    assert (actuelDigits == exceptedDigits)

def ExtractEntryToInt(entry):

    print(entry)
    lines = entry.splitlines()
    digits = []
    for i in range(0, len(lines[1]), 3):

        digit_entry = lines[1][i:i+3] + lines[2][i:i+3] + lines[3][i:i+3]
        digits.append(DigitRecognizer(digit_entry))
    return int("".join(map(str, digits)))   

def ReadEntryFromFile(file_content):
    entries = file_content.split("\n\n")

    for entry in entries:
        print(entry)
        if len(entry.splitlines()) != 3 :
            printError(entry, "Invalid number of lines by entry in file content")
        if not all(CheckLineIsValidLength(line) for line in entry.splitlines()) :
            printError(entry, "Invalid line length in file content")
        if not CheckOnlyValidCharacters(entry) :
            printError(entry, "Invalid characters in file content")

    return [ExtractEntryToInt("\n"+entry) for entry in entries]

def printError(entry, error_message):
    print(entry)
    raise ValueError(error_message)