import os

def count_lines_of_code(directory: str) -> int:
    total_lines = 0

    for root, dirs, files in os.walk(directory):
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')

        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    total_lines += len(lines)
                print(f"File: {file_path} - {len(lines)} lines")

    return total_lines

project_directory = "/Users/micah/Downloads/NOSTR/nospy/nospy"
total_lines = count_lines_of_code(project_directory)
print(f"Total lines of code: {total_lines}")
