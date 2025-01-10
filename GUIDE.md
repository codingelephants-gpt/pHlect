# Guide/Instructions on how to use pHlect
## Readers
In pHlect a reader is the model that reads the file.
### Mostafa
Mostafa is selected as default, that is if you dont add the reader attribute.
Mostafa reads every single line and places them into one single string.

### Shine
Shine reads only one line. So for example if you would only want to read one line, you should use Shine.
Shine has an attribute called 'shineline', this specifies which line you want to read. By default, Shineline is "all". With this it basically acts like Mostafa.

### Camel
Camel reads all lines, but puts the lines in a list.
Theres not a lot of explanation needed for this, so i wont continue it.

### Example:
```python
# Mostafa
from pHlect import *

x = Read(
    filename="/path/to/your/file",
    reader="Mostafa" # Mostafa is already selected by default, if your using it you dont have to place this.
)
a = x.contents()
print(a) # Prints the contents of 'x'

# Shine
from pHlect import *

x = Read(
    filename="/path/to/your/file"
    reader="Shine"
    shineline=5
)
a = x.contents()
print(a) # Prints the fifth line of 'x'

# Camel
from pHlect import *

x = Read(
    filename="/path/to/your/file"
    reader="Camel"
)
a = x.contents()
print(a[1], a[2]) # Prints the first and second line of 'x'
