import openpyxl
import re
import os 

out = "" 

def parse_hf(header_path):
    with open(header_path, "r") as file:
        content = file.read()
    
    # Regular expressions to match function prototypes and variable declarations
    function_pattern = re.compile(r'\b[A-Za-z_][A-Za-z0-9_]*\s+\**\b[A-Za-z_][A-Za-z0-9_]*\s*\([^)]*\)\s*;')

    # Global Variables
    global_variable_pattern = re.compile(r'\b(?:extern\s+)?[A-Za-z_][A-Za-z0-9_]*\s+\**\b[A-Za-z_][A-Za-z0-9_]*\s*(?:=\s*[^;]+)?\s*;')

    # # Macro Definitions
    # macro_pattern = re.compile(r'#define\s+\w+\s+.+')

    # # Include Statements
    # include_pattern = re.compile(r'#include\s+[<"]\w+(\.\w+)?[>"]')

    # # Typedef Declarations
    # typedef_pattern = re.compile(r'typedef\s+.*\s+\w+\s*;')

    # # Struct Declarations
    # struct_pattern = re.compile(r'struct\s+\w+\s*\{[^}]*\}\s*;')

    # # Enum Declarations
    # enum_pattern = re.compile(r'enum\s+\w*\s*\{[^}]*\}\s*;')

    # # Preprocessor Directives
    # preprocessor_pattern = re.compile(r'#\s*(if|ifdef|ifndef|else|elif|endif|pragma|undef)\b')

    # # Function-Like Macros
    # function_like_macro_pattern = re.compile(r'#define\s+\w+\(.*?\)\s+.+')
    
    # patterns = [
    # 'function_pattern',
    # 'global_variable_pattern',
    # 'macro_pattern',
    # 'include_pattern',
    # 'typedef_pattern',
    # 'struct_pattern',
    # 'enum_pattern',
    # 'preprocessor_pattern',
    # 'function_like_macro_pattern'
    # ]   


    functions = function_pattern.findall(content)
    global_variables = global_variable_pattern.findall(content)

    return functions,global_variables


def append_data(functions_sheet, variables_sheet, functions, variables):
    # Add functions to the Functions sheet
    for i, function in enumerate(functions, start=1):
        print(f"Appending function: ID={i}, Prototype={function}")
        functions_sheet.append([i, function])

    # Add variables to the Variables sheet
    for i, variable in enumerate(variables, start=1):
        print(f"Appending variable: ID={i}, Declaration={variable}")
        variables_sheet.append([i, variable])


def create_excel (out_file , header) :  
    global out
    res = 'n'
    while(res == 'n')  :
        out = input("Enter the file name : " ) + ".xlsx"
        if os.path.exists(out):
            res = input("the file exists [y to remove / n to change the file name] : ")
            if res == 'y' : 
                os.remove(out)
                print(f"{out} has been deleted and the new one has been created.") 
            elif res == 'n' : 
                continue 
            else : 
                print("invalid input") 
                continue
        else:
            print(f"{out} does not exist and your file has been created.")
            break

    # Create a new workbook
    workbook = openpyxl.Workbook()
    
    # Create a sheet for functions
    functions_sheet = workbook.active
    functions_sheet.title = "functions"
    functions_sheet.append(["ID", "Function Prototype"])
    
    # Create a new sheet for variables
    variables_sheet = workbook.create_sheet(title="variables")
    variables_sheet.append(["ID", "Variable Declaration"])

    # Adjust the column width
    functions_sheet.column_dimensions['A'].width = 10
    functions_sheet.column_dimensions['B'].width = 50
    variables_sheet.column_dimensions['A'].width = 10
    variables_sheet.column_dimensions['B'].width = 50 

    return functions_sheet , variables_sheet , workbook


def header_path () : 
    while(True) :        
        header = input("Enter the header path : " ) 
        if os.path.exists(header):  
            if os.path.isfile(header) and header.endswith('.h'):
                print("right! the file exists.")
                break
        else:
            print(f"invalid header file path.") 

    return header


def main():
    header = header_path()
    
    functions_sheet , variables_sheet , workbook = create_excel(out , header)
    
    # Parse the header file
    functions, variables = parse_hf(header)
    
    # Append data to the respective sheets
    append_data(functions_sheet, variables_sheet, functions, variables) 

    workbook.save(out) 
    print("done")


if __name__ == "__main__":
    main()
