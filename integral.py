import sympy as sp

def integral_calculator():
    print("Python Integral Calculator")
    print("Enter your function in terms of 'x'. For example, x^2 should be entered as x**2.")
    
    while True:
        user_input = input("Enter a function (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            break
        
        try:
            x = sp.symbols('x')
            function = sp.sympify(user_input)
            integral = sp.integrate(function, x)
            print("Integral of", function, "is", integral)
        except sp.SympifyError:
            print("Invalid input. Please enter a valid function.")

if __name__ == "__main__":
    integral_calculator()
