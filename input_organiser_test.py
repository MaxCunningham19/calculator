from input_organiser import isValidChars

class test:
    def __init__(self,name:str,input,output ) -> None:
        self.name = name
        self.input = input
        self.output = output

def isValidCharsTest() -> None:
    tests = [test("addition","1+1",True),
            test("multiplication","1x2",True),
            test("subtraction","1-1",True),
            test("division","1%1",True),
            test("all numbers","1+2+3+4+5+6+7+8+9+0",True),
            test("bad input correct chars","6+",True),
            test("brackets","(1+1)+1",True),
            test("letters","a+b",False),
            test("weird chars","$#^*.,",False)]
    
    fails = []
    for t in tests:
        result = isValidChars(t.input)
        if  t.output != result:
            fails.append(t)
            print("Test",t.name,"Fails Expected:",t.output,"Got:",result)
    print("isValidCharTest Complete...")
    assert(len(fails) == 0)