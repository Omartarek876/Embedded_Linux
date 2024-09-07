
# Header File Parser

## Overview

The Header File Parser is a Python script designed to extract and organize key elements from C/C++ header files (`.h` files) into an Excel spreadsheet (`.xlsx`). The tool identifies functions, global variables, macros, and include statements, outputting each into a dedicated sheet within the generated Excel file. This is particularly useful for developers who need to analyze, document, or refactor large codebases.

## Features

- **Function Prototypes**: Extracts and lists all function prototypes found in the header file.
- **Global Variables**: Identifies and records global variable declarations.
- **Macros**: Captures and lists all `#define` macros.
- **Include Statements**: Records all `#include` statements.

## Requirements

- **Python 3.x**: Ensure you have Python 3.x installed.
- **openpyxl**: This package is required for Excel file manipulation. Install it via pip if not already installed:

  ```sh
  pip install openpyxl
  ```

## Usage

1. **Clone the Repository**:
   
   Clone or download the script to your local machine.

2. **Run the Script**:

   Execute the script from the command line:

   ```sh
   python header_parser.py
   ```

3. **Provide the Header File Path**:

   When prompted, enter the path to the header file you want to parse. The script verifies the file's existence and extension before proceeding.

4. **Specify Output File**:

   Enter the desired name for the output Excel file (without the `.xlsx` extension). If the file already exists, you'll have the option to overwrite it or provide a new name.

5. **Review the Output**:

   After execution, the script generates an Excel file containing:
   
   - **Functions**: List of all function prototypes.
   - **Global Variables**: Declarations of global variables.
   - **Macros**: `#define` macro definitions.
   - **Includes**: `#include` statements.

   If no items of a certain type are found, the corresponding sheet will contain a message stating "not mentioned in the header file."

## Example

Assume you have a header file named `example.h` and you want to extract its contents into an Excel file named `output.xlsx`.

```sh
python header_parser.py
```

- **Input**: Enter the path to `example.h`.
- **Output**: Specify `output` as the output file name. The result will be `output.xlsx` in the current directory.

## File Structure

- **Functions**: Contains the ID and function prototype.
- **Global Variables**: Contains the ID and global variable declaration.
- **Macros**: Contains the ID and macro definition.
- **Includes**: Contains the ID and include statement.

## Error Handling

- The script checks if the input header file exists and has a `.h` extension.
- If the output file name already exists, the script provides options to overwrite or rename the file.

## Customization

Feel free to modify the script to include additional patterns or customize the output format. The script is designed to be modular and easy to extend.

