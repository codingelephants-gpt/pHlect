# Do NOT run a file that executes itself, it will cause an infinite loop.

class Read:
    def __init__(self, file_name="", reader="Mostafa", shine_line="all"):
        self.reader = reader
        self.filename = file_name
        self.shine_line = shine_line

    def contents(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                if self.reader == "Mostafa":
                    return file.read()
                elif self.reader == "Shine":
                    lines = file.readlines()
                    if self.shine_line == "all":
                        return ''.join(lines)
                    else:
                        if self.shine_line.isdigit():
                            shine_index = int(self.shine_line)
                            if 0 <= shine_index < len(lines):
                                return lines[shine_index]
                            else:
                                return f"Error: Line {shine_index} is out of range."
                        else:
                            return "Error: Invalid line number for Shine."
                elif self.reader == "Camel":
                    return [line for line in file]
                else:
                    return "Error: Invalid reader specified."
        except FileNotFoundError:
            return f"Error: File '{self.filename}' not found."
        except ValueError:
            return "Error: Invalid line number for Shine."
        except Exception as e:
            return f"An unexpected error occurred: {e}"


def sanitize_content(content):
    
    lines = content.splitlines()
    sanitized_lines = [line for line in lines if line.strip() != ""]
    return "\n".join(sanitized_lines)

def help():
    print("""Welcome to the Python File Reader!
    Read a file using the Read class: r = pHlect.Read('file_name.txt', 'reader_name', 'line_number' # line_number is optional, only for Shine reader)
    Get the contents of the file: output = r.contents()
    Sanitize the content: sanitized_content = pHlect.sanitize_content(output)
    Readers:
    - Mostafa: Reads the entire file.
    - Shine: Reads a specific line from the file. Specify the line number as the third argument.
    - Camel: Reads the file line by line and returns a list of lines.
    Commands:
    - help(): Displays this help message.
    - sanitize_content(content): Removes empty lines from the content.

    """)


r = Read(r"C:\Users\Gebruiker\Downloads\VS\classtests.py\welcome.py", "Shine", "0")  
output = r.contents()

exec(output)

help()