import os
from crewai_tools import BaseTool

class CustomWriterTool(BaseTool):
    name: str = "File Writer Tool"
    description: str = "A tool for writing content to files."
    
    # Hardcoded output directory
    output_directory: str = 'software'

    def _run(self, file_name: str, content: str) -> str:
        # Ensure the output directory exists
        os.makedirs(self.output_directory, exist_ok=True)
        
        # Construct the file path using os.path.join
        file_path = os.path.join(self.output_directory, file_name)
        
        try:
            # Write content to the file
            with open(file_path, 'w') as file:
                print(f'Writing "{file_path}"')
                file.write(content)
        except Exception as e:
            # Return error message if write fails
            return f"Error writing to file '{file_name}': {str(e)}"
        
        return f"File '{file_name}' written successfully."
