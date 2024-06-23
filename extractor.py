'''
Algorightm:
Here are the steps you should follow to create this program:

Read the file: Start by reading the contents of Computerinfo.txt into your program.

Identify sections: You need to differentiate between the two formats.
Look for unique markers that can help you identify where each format starts and ends.

Extract data: 
Use regular expressions or string manipulation techniques 
to extract the required information from each format.

Store the extracted data: Store the extracted data in a 
suitable data structure, like a list of dictionaries, 
where each dictionary represents one entry.

Output the data: Once you have extracted all the data, 
you can output it in the desired format.'''
import re

with open('Computerinfo.txt', 'r') as file:
    data = file.read()

# Initialize lists
first_format_entries = []
second_format_entries = []

header = ["Serial Number", "Computer Number", "Computer Model", "Ethernet MAC Address", "Wireless MAC Address"]
second_format_entries.append(header)

# Corrected regular expressions
first_entry_pattern = re.compile(r"Computer: (.+?)\n.*?Ethernet MAC Address: (.+?)\nWi-Fi MAC Address: (.+?)\nComputer Model: (.+?)\nSerial Number: (.+?)\n", re.DOTALL)
second_entry_pattern = re.compile(r"Serial Number: \| (.+?) \| Computer number \| (.+?) \| Computer Model: \| (.+?) \| Ethernet MAC Address: \| (.+?) \| Wi-Fi MAC Address: \| (.+?)$")# Assume data is a string containing the file content
entries = data.split("\n\n")
processing_first_format = True

for entry in entries:
    if processing_first_format:
        match = first_entry_pattern.search(entry)
        if match:
            first_format_entries.append([match.group(5), '', match.group(4), match.group(2), match.group(3)])
        else:
            processing_first_format = False
    if not processing_first_format:
        match = second_entry_pattern.search(entry)
        if match:
            second_format_entries.append(list(match.groups()))

extracted_data = first_format_entries + second_format_entries

with open('ExtractedComputerInfo.txt', 'w') as output_file:
    for item in extracted_data:
        output_file.write(" | ".join(item) + "\n")
  
"""# For demonstration, printing the results

for item in extracted_data:
    print(" | ".join(item))"""


'''To run the Python script directly from a USB drive and have it process a file on that drive, you can follow these steps. This explanation assumes you're using a Linux system, as mentioned earlier.

### Step 1: Prepare the Python Script

1. **Modify the Script**: Ensure the script points to the correct file path on the USB drive. For example, if your USB drive is mounted to `/media/your_username/USB_NAME` and the file is named `Computerinfo.txt`, update the file opening line in your script to:

```python
with open('/media/your_username/USB_NAME/Computerinfo.txt', 'r') as file:
```

Replace `your_username` and `USB_NAME` with the actual username and the name of your USB drive.

2. **Save the Script on the USB Drive**: Save the modified script to the root of your USB drive or in a specific folder.

### Step 2: Make the Script Executable

1. **Open Terminal**: Navigate to the USB drive directory where the script is saved.

```bash
cd /media/your_username/USB_NAME
```

2. **Make Script Executable**: Run the following command to make your Python script executable. Replace [`extractor.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Frayfry%2Frepos%2Fgeneral_programs%2Fextractor.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/rayfry/repos/general_programs/extractor.py") with the name of your script.

```bash
chmod +x extractor.py
```

### Step 3: Create a Bash Runner (Optional)

If double-clicking doesn't run the script directly, you might need to create a simple bash script to run your Python script. This is because the file manager might not execute Python scripts directly for security reasons.

1. **Create a Bash Script**: In the same directory as your Python script, create a new file named `run_extractor.sh` with the following content:

```bash
#!/bin/bash
python /media/your_username/USB_NAME/extractor.py
```

2. **Make the Bash Script Executable**:

```bash
chmod +x run_extractor.sh
```

Now, you should be able to double-click `run_extractor.sh` to run your Python script. If double-clicking doesn't work, right-click the file and choose "Run in Terminal" or a similar option.

### Step 4: Running the Script

- **Double-Click**: If your system is configured to allow executing scripts by double-clicking, you might be able to run the Python script or the bash script directly by double-clicking it.
- **Terminal**: You can always run the script from the terminal:

```bash
./extractor.py
```

or if using the bash runner:

```bash
./run_extractor.sh
```

### Note:

- Ensure Python is installed on your system and accessible from the terminal.
- The path to the Python interpreter might vary. If `python` command doesn't work, try `python3`.
- The exact steps might vary based on your Linux distribution and its configuration.'''