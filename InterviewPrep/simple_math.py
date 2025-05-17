class Calculator():
    def __init__(self):
        self.operator = None
        self.number1 = None
        self.Number2 = None
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

    def is_reach_end(self, i):
        return not i < len(self.input)

    def get_number_end_index(self, i):
        next_index = i + 1
        while (next_index < len(self.input) and self.is_number(self.input[next_index])):
            next_index += 1
        return next_index
    
    def get_space_end_index(self, i):
        next_index = i
        count = 0
        while (next_index < len(self.input) and self.is_space(self.input[next_index])):
            next_index += 1
            count += 1
        return count
    

    def new_cal(self, calculator: Calculator):
        
        self.index += self.get_space_end_index(self.index)
        
        # check the first input is negative symbol        
        if (self.input[self.index] == '-'):
            calculator.is_negative = True;
            self.index += 1
            if self.is_reach_end(self.index):
                raise "Invalid negative symbol"

        while self.index < len(self.input): 
            if self.is_right_bracket(self.input[self.index]):
                print(f'{calculator.number1}, {calculator.Number2}, {calculator.operator}, {calculator.is_complete}')
                if calculator.is_complete != True and calculator.operator != None: 
                    raise "Invalid input data"
                self.index += 1
                return calculator.number1

            print(f'current index: {self.index}')

            if self.is_number(self.input[self.index]):
                number_end_index = self.get_number_end_index(self.index)
                temp = self.input[self.index : number_end_index]

                if (calculator.number1 == None):
                    calculator.number1 = int(temp)
                    if (calculator.is_negative):
                        calculator.number1 = calculator.number1 * -1
                        calculator.is_negative = None
                else:
                    print(f'Num1: {calculator.number1}, num2: {temp},  op: {calculator.operator}')
                    calculator.number2 = int(temp)
                    calculator.number1 = calculator.calculate()
                    calculator.operator = None
                    calculator.number2 = None
                    calculator.is_complete = True
                    print(f'calculator result: {calculator.result}')
                self.index = number_end_index
            elif self.is_operator(self.input[self.index]):
                calculator.is_complete = False
                if (calculator.operator != None):
                    raise "Invalid operator symbol"               
                calculator.operator = self.input[self.index]
                self.index += 1
            elif self.is_left_bracket(self.input[self.index]):
                if self.is_right_bracket(self.input[self.index + 1]): 
                    raise "invalid input with ()"
                self.index += 1
                if calculator.number1 == None:
                    calculator.number1 = self.new_cal(Calculator()) 
                else:
                    calculator.number2 = self.new_cal(Calculator()) 
                    print(f'num1: {calculator.number1}, Num2: {temp},  op: {calculator.operator}')
                    calculator.number1 = calculator.calculate()
                    calculator.operator = None
                    calculator.number2 = None
                    calculator.is_complete = True
                    calculator.result = calculator.number1
                    print(f'bracket calculator result: {calculator.result}')

            elif self.is_space(self.input[self.index]):
                self.index += 1             
            else:     
                raise "Invalid Charator"
            #self.index += 1             

        if calculator.is_complete == False:
            return "Invalid"

        return calculator.number1


expression = "1- ((1) + 2 - (0- 20 -    18) + (1 + (     -2)) -(6- (3    -    (1+1)   ) ))  "
print("length: " + str(len(expression)))
calculation = SimpleMath(expression)
print(calculation.call())
