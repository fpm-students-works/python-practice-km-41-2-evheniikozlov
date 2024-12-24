import factorial
import exp_root
import logarithm
from utils import input_with_condition, input_with_transform, condition_transform

    
def console_fact():
    argument = input_with_condition(
        lambda: input_with_transform(
            lambda: input_with_condition(
                lambda: input("Enter an argument: "),
                lambda inp: condition_transform(inp, int),
                lambda inp: print(f"An argument must be an integer")
            ),
            lambda inp: int(inp)
        ),
        lambda inp: inp >= 0,
        lambda inp: print(f"An argument must be non-negative")
    )
    print(f"Factorial of {argument} is {factorial.fact(argument)}")
    

def console_exp_2():
    base = input_with_transform(
        lambda: input_with_condition(
            lambda: input("A base a number: "),
            lambda inp: condition_transform(inp, float),
            lambda inp: print(f"A base must be a float")
        ),
        lambda inp: float(inp)
    )
    print(f"{base} squared is {exp_root.exp2(base)}")
    

def console_exp_3():
    base = input_with_transform(
        lambda: input_with_condition(
            lambda: input("Enter a base: "),
            lambda inp: condition_transform(inp, float),
            lambda inp: print(f"A base must be a float")
        ),
        lambda inp: float(inp)
    )
    print(f"{base} cubed is {exp_root.exp3(base)}")


def console_root_2():
    radicand = input_with_condition(
        lambda: input_with_transform(
            lambda: input_with_condition(
                lambda: input("Enter a radicand: "),
                lambda inp: condition_transform(inp, float),
                lambda inp: print(f"A radicand must be a float")
            ),
            lambda inp: float(inp)
        ),
        lambda inp: inp >= 0,
        lambda inp: print(f"A radicand must be non-negative")
    )
    print(f"The square root of {radicand} is {exp_root.root2(radicand)}")
    

def console_root_3():
    radicand = input_with_transform(
        lambda: input_with_condition(
            lambda: input("Enter a radicand: "),
            lambda inp: condition_transform(inp, float),
            lambda inp: print(f"A radicand must be a float")
        ),
        lambda inp: float(inp)
    )
    print(f"The cube root of {radicand} is {exp_root.root3(radicand)}")


def console_log():
    base = input_with_condition(
        lambda: input_with_condition(
            lambda: input_with_transform(
                lambda: input_with_condition(
                    lambda: input("Enter a base: "),
                    lambda inp: condition_transform(inp, float),
                    lambda inp: print(f"Base must be a float")
                ),
                lambda inp: float(inp)
            ),
            lambda inp: inp > 0,
            lambda inp: print(f"Base must be positive")
        ),
        lambda inp: inp != 1,
        lambda inp: print(f"Base must not equal 1")
    )
    argument = input_with_condition(
        lambda: input_with_transform(
            lambda: input_with_condition(
                lambda: input("Enter an argument: "),
                lambda inp: condition_transform(inp, float),
                lambda inp: print(f"An argument must be a float")
            ),
            lambda inp: float(inp)
        ),
        lambda inp: inp > 0,
        lambda inp: print(f"An argument must be positive")
    )
    print(f"The logarithm of {argument} to the base {base} is {logarithm.log(base, argument)}.")


def console_ln():
    argument = input_with_condition(
        lambda: input_with_transform(
            lambda: input_with_condition(
                lambda: input("Enter an argument: "),
                lambda inp: condition_transform(inp, float),
                lambda inp: print(f"An argument must be a float")
            ),
            lambda inp: float(inp)
        ),
        lambda inp: inp > 0,
        lambda inp: print(f"An argument must be positive")
    )
    print(f"The nartural logarithm of {argument} is {logarithm.ln(argument)}.")
    

def console_lg():
    argument = input_with_condition(
        lambda: input_with_transform(
            lambda: input_with_condition(
                lambda: input("Enter an argument: "),
                lambda inp: condition_transform(inp, float),
                lambda inp: print(f"An argument must be a float")
            ),
            lambda inp: float(inp)
        ),
        lambda inp: inp > 0,
        lambda inp: print(f"An argument must be positive")
    )
    print(f"The common logarithm of {argument} is {logarithm.lg(argument)}.")


def main():
    commands = {
        "1": {
            "name": "factorial",
            "function": console_fact
        },
        "2": {
            "name": "square",
            "function": console_exp_2
        },
        "3": {
            "name": "cube",
            "function": console_exp_3
        },
        "4": {
            "name": "square root",
            "function": console_root_2
        },
        "5": {
            "name": "cube root",
            "function": console_root_3
        },
        "6": {
            "name": "logarithm",
            "function": console_log
        },
        "7": {
            "name": "natural logarithm",
            "function": console_ln
        },
        "8": {
            "name": "common logarithm",
            "function": console_lg
        }
    }

    
    while True:
        print()
        
        for id, command in commands.items():
            print(f"Enter {id} if you want to calculate {command['name']}")
        
        print("Enter stop, if you want to end the program")
        
        controller = input()
        print()
        
        if controller == "stop":
            break
        
        if controller in commands:
            commands[controller]["function"]()
        else:
            print("This option does not exist")
    

if __name__ == "__main__":
    main()