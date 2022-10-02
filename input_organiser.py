
# isValidInput
# @param: input_to_calc -> the input string of the user
# @return: bool -> returns true if the string only contains valid characters
validChars = {'+','-','%','x','(',')'}
def isValidChars(input_to_calc:str) -> bool:
    for tmpChar in input_to_calc:
        special = validChars.intersection({tmpChar})
        if len(special)==0 and (ord(tmpChar)<48 or ord(tmpChar)>57):
            return False
    return True
