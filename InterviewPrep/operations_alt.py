import json

class CalHelp():
    def __init__(self):
        self.operator = None
        self.number1 = None
        self.number2 = None
        self.is_negative = None
        self.is_complete = False

    def cal(self):
        if self.operator == "+": return self.number1 + self.number2
        if self.operator == "-": return self.number1 - self.number2
        raise

class Test():
    def __init__(self, input):
        self.input = input
        self.index = 0
    
    def is_number(self, str_num):
        try:
            int(str_num.strip())
            return True
        except:
            return False
    
    def is_negative(self, str_num):
        if self.is_number(str_num):
            if -1 * int(str_num) > 0:
                return True
        
        return False
    
    def is_operator(self, char):
        if char in '+-':
            return True
        return False
    
    def is_left_bracket(self, string):
        return string == '('
    
    def is_right_bracket(self, string):
        return string == ')'    
    
    def is_space(self, string):
        return string == ' '
    
    def call(self):
        return self.new_cal(CalHelp())

    def new_cal(self, calculator):
        temp = ""
        
        if (self.input[self.index] == '-'):
            calculator.is_negative = True;
            self.index += 1        
        
        
        
        while  self.index < len(self.input): 
            #print(json.dumps(calculator))
            if self.is_right_bracket(self.input[self.index]):
                if calculator.is_complete != True: 
                    raise
                self.index += 1
                return calculator.number1
            if self.is_number(self.input[self.index]):
                print(self.input[self.index])
                temp = self.input[self.index]
                self.index += 1
                while self.index < len(self.input) and self.is_number(self.input[self.index]):
                    temp += self.input[self.index]
                    self.index += 1
                    
                if (calculator.number1 == None):
                    calculator.number1 = int(temp)
                    print("++++++++")
                    if self.index < len(self.input) and self.is_negative(self.input[self.index]):
                        calculator.number1 = calculator.number1 * -1
                        calculator.is_negative = None
                else:
                    calculator.number2 = int(temp)
                    calculator.number1 = calculator.cal()
                    calculator.operator = None
                    calculator.number2 = None
                    calculator.is_complete = True
                    print("==========")
                    print(calculator.number1)
            if self.index < len(self.input) and self.is_operator(self.input[self.index]):
                calculator.is_complete = False
                if (calculator.operator != None):
                    raise                
                calculator.operator = self.input[self.index]
                self.index += 1
                
            if self.index < len(self.input) and self.is_left_bracket(self.input[self.index]):
                print("---------")
                self.index += 1
                if self.is_right_bracket(self.input[self.index]): 
                    raise
                if calculator.number1 == None:
                    calculator.number1 = self.new_cal(CalHelp()) 
                else:
                    calculator.number2 = self.new_cal(CalHelp()) 
                    calculator.number1 = calculator.cal()
                    calculator.operator = None
                    calculator.number2 = None
                    calculator.is_complete = True
                    print("**********")
                    print(calculator.number1)
            
            if self.index < len(self.input) and self.is_space(self.input[self.index]):
                self.index += 1

        if calculator.is_complete == False:
            return "Invalid"
        
        return calculator.number1
                      

expression = "1- (-1 + 2 - (0- 20 -    18) + (1 + (1   - 2)) -(6- (3    -    (1+1)   ) ))  "
calculation = Test(expression)
print(calculation.call())







class Calculator():
    def __init__(self):
        self.operator = None
        self.first = None
        self.second = None
        self.is_negative = None
        self.is_complete = False
        self.result = None

    def calculate(self):
        if self.operator == "+": return self.number1 + self.number2
        if self.operator == "-": return self.number1 - self.number2
        raise "No supported operator"

class SimpleMath():
    def __init__(self, input):
        self.input: str = input
        self.index = 0
    
    def is_number(self, str_num):
        try:
            int(str_num)
            return True
        except:
            return False
    
    def is_negative(self, str_num):
        if self.is_number(str_num):
            if -1 * int(str_num) > 0:
                return True
        
        return False
    
    def is_operator(self, char):
        return char in '+-'
    
    def is_left_bracket(self, string):
        return string == '('
    
    def is_right_bracket(self, string):
        return string == ')'    
    
    def is_space(self, string):
        return string == ' '
    
    def call(self):
        return self.new_cal(Calculator())
    
    def is_reach_end(self, index):
        return not index<self.input
    
    def get_number_end_index(self, index):
        next_index += index
        while (next_index < len(self.input) and self.is_number(self.input[next_index])):
            next_index += 1
        return next_index


    def new_cal(self, calculator: Calculator):
        # check the first input is negative symbol
        if (self.input[self.index] == '-'):
            calculator.is_negative = True;
            self.index += 1
            if self.is_reach_end(self.index):
                raise "Invalid negative symbol"
        
        while  self.index < len(self.input): 
            if self.is_right_bracket(self.input[self.index]):
                if calculator.is_complete != True and calculator.operator != None: 
                    raise "Invalid input data"
                self.index += 1
                return calculator.number1
            
            if self.is_number(self.input[self.index]):
                number_end_index = self.get_number_end_index(self.index)
                temp = self.input[self.index : number_end_index]
                    
                if (calculator.number1 == None):
                    calculator.number1 = int(temp)
                    if (calculator.is_negative):
                        calculator.number1 = calculator.number1 * -1
                        calculator.is_negative = None
                else:
                    calculator.number2 = int(temp)
                    calculator.number1 = calculator.cal()
                    calculator.operator = None
                    calculator.number2 = None
                    calculator.is_complete = True
                    print(f'calculator result: {calculator.result}')
                self.index -= number_end_index 
            elif self.is_operator(self.input[self.index]):
                calculator.is_complete = False
                if (calculator.operator != None):
                    raise "Invalid operator symbol"               
                calculator.operator = self.input[self.index]
            elif self.is_left_bracket(self.input[self.index]):
                if self.is_right_bracket(self.input[self.index + 1]): 
                    raise "invalid input with ()"
                if calculator.number1 == None:
                    calculator.number1 = self.new_cal(Calculator()) 
                else:
                    calculator.number2 = self.new_cal(Calculator()) 
                    calculator.number1 = calculator.cal()
                    calculator.operator = None
                    calculator.number2 = None
                    calculator.is_complete = True
                    calculator.result = calculator.number1
                    print(f'bracket calculator result: {calculator.result}')
            
            elif not self.is_space(self.input[self.index]):
                raise "Invalid Charator"
            self.index += 1

        if calculator.is_complete == False:
            return "Invalid"
        
        return calculator.number1
                      

expression = "1- (-1 + 2 - (0- 20 -    18) + (1 + (1   - 2)) -(6- (3    -    (1+1)   ) ))  "
calculation = Test(expression)
print(calculation.call())
