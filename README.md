# DirectoryMove
Python automation script that moves files from one directory to another

---

# File Organizer

This Python script organizes files in a specified source directory based on their types and moves them to designated folders in a destination directory.

## Usage

1. Clone the Repository
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Run the Script
   ```bash
   python organize_files.py
   ```

3. Specify Source and Destination Directories
 Open `organize_files.py` and modify the `source_dir` and `destination_dir` variables to point to your desired source and         destination directories.
   ```python
   source_dir = '/path/to/source_directory'
   destination_dir = '/path/to/destination_directory'
   ```

4. Execute the Script:**
   Run the script again after modifying the directories.
   ```bash
   python organize_files.py
   ```

 ##Customization

- The script categorizes files into the following types:
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.heic`
  - **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.zip`, `.pkg`, `.md`
  - **Videos**: `.mp4`, `.avi`, `.mkv`, `.mov`

- You can customize the file types and their corresponding destination folders by modifying the `file_types` dictionary in the script.

## Example

```python
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.heic'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.zip', '.pkg', '.md'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov']
}
```

## Requirements

- Python 3.x

## Note

- The script will create destination folders if they do not exist.

- Make sure to modify the `source_dir` and `destination_dir` variables to match your desired directories.





