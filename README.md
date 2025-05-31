# Windows Temporary File Cleanup Script

**Author:** SomeRandomStranger123 
**Date:** 3/25/2020  

## Description:

This script is designed to clean up temporary files (.tmp, .dmp, .hdmp) from specified drives (C, E, and F) on a Windows system. It utilizes Python and system commands to locate and delete these temporary files.

## Usage:

1. **Ensure Python is installed**: This script requires Python to be installed on your system.

2. **Run the script**: Execute the script by running the Python file (`cleanup_script.py`).

3. **Check log files**: The script will generate two log files:
    - `Tmp_check_Log.txt`: Logs the temporary files found.
    - `Tmp_Clean_Log.txt`: Logs the deletion status of temporary files.

4. **Review log files**: Review the log files to ensure that temporary files were located and deleted successfully.

## Important Note:
- Ensure that you have appropriate permissions to delete files on the specified drives.
- This script is designed for Windows systems and may not work on other operating systems.
- Use caution when running scripts that delete files, as it may affect system stability if used incorrectly.
