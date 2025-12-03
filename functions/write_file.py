import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    # Normalize file_path and join to get full target path
    normalized_file_path = os.path.normpath(file_path)
    target_file = os.path.abspath(os.path.join(working_directory, normalized_file_path))
    
    # Check if target is inside working_directory (more robust cross-platform)
    if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        # Create full directory tree for the target file (includes working_directory and subdirs)
        file_dir = os.path.dirname(target_file)
        os.makedirs(file_dir, exist_ok=True)
        
        # Write to the full target path
        with open(target_file, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    
    