#include <iostream>
#include <iomanip>  // For formatting output

int main() {
    // Print the table header
    std::cout << std::setw(10) << "ASCII Code" 
              << std::setw(15) << "Character" 
              << std::setw(25) << "Description" << std::endl;
    std::cout << "---------------------------------------------------" << std::endl;

    for (int i = 0; i < 128; ++i) {
        // Print the ASCII code
        std::cout << std::setw(10) << i;
        
        // Print the character (for non-printable characters, show as 'non-printable')
        if (i >= 32 && i <= 126) {
            std::cout << std::setw(15) << static_cast<char>(i);
        } else {
            std::cout << std::setw(15) << "Non-printable";
        }

        // Provide a description for control characters
        switch (i) {
            case 0: std::cout << std::setw(25) << "Null character (NUL)"; break;
            case 1: std::cout << std::setw(25) << "Start of Header (SOH)"; break;
            case 2: std::cout << std::setw(25) << "Start of Text (STX)"; break;
            case 3: std::cout << std::setw(25) << "End of Text (ETX)"; break;
            case 4: std::cout << std::setw(25) << "End of Transmission (EOT)"; break;
            case 5: std::cout << std::setw(25) << "Enquiry (ENQ)"; break;
            case 6: std::cout << std::setw(25) << "Acknowledge (ACK)"; break;
            case 7: std::cout << std::setw(25) << "Bell (BEL)"; break;
            case 8: std::cout << std::setw(25) << "Backspace (BS)"; break;
            case 9: std::cout << std::setw(25) << "Horizontal Tab (TAB)"; break;
            case 10: std::cout << std::setw(25) << "Line Feed (LF)"; break;
            case 11: std::cout << std::setw(25) << "Vertical Tab (VT)"; break;
            case 12: std::cout << std::setw(25) << "Form Feed (FF)"; break;
            case 13: std::cout << std::setw(25) << "Carriage Return (CR)"; break;
            case 27: std::cout << std::setw(25) << "Escape (ESC)"; break;
            case 32: std::cout << std::setw(25) << "Space"; break;
            case 127: std::cout << std::setw(25) << "Delete (DEL)"; break;
            default:
                if (i < 32) {
                    std::cout << std::setw(25) << "Control character";
                } else {
                    std::cout << std::setw(25) << "Printable character";
                }
                break;
        }
        
        std::cout << std::endl;  // Newline after each row
    }
    
    return 0;
}
