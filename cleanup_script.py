# Windows Temporary File Cleanup Script
# SomeRandomStranger123
# 3/25/2020

import os

# Function to clean the C drive
def clean_C():
    try: 
        os.chdir("C:\\")  # Change directory to C drive
    except:
        print("No drive")
    else:
        # Check for temporary files (.tmp, .dmp, .hdmp) and log them
        os.system("cmd /c dir ~*.* /s >> C:\\Tmp_check_Log.txt 2>>&1")
        os.system("cmd /c dir *.tmp* /s >> C:\\Tmp_Check_Log.txt 2>>&1")
        os.system("cmd /c dir *.dmp* /s >> C:\\Tmp_Check_Log.txt 2>>&1")
        os.system("cmd /c dir *.hdmp* /s >> C:\\Tmp_Check_Log.txt 2>>&1")
        
        # Attempt to delete temporary files and log deletion status
        os.system("cmd /c del ~*.* /s >> C:\\Tmp_Clean_Log.txt 2>>&1")
        os.system("cmd /c del *.tmp* /s >> C:\\Tmp_Clean_Log.txt 2>>&1")
        os.system("cmd /c del *.dmp* /s >> C:\\Tmp_Clean_Log.txt 2>>&1")
        os.system("cmd /c del *.hdmp* /s >> C:\\Tmp_Clean_Log.txt 2>>&1")

# Function to clean the E drive
def clean_E():
    try: 
        os.chdir("E:\\")  # Change directory to E drive
    except:
        print("No drive")
    else:
        # Check for temporary files (.tmp, .dmp, .hdmp) and log them
        os.system("cmd /c dir ~*.* /s >> C:\\Tmp_check_Log.txt 2>>&1")
        os.system("cmd /c dir *.tmp* /s >> C:\\Tmp_Check_Log.txt 2>>&1")
        os.system("cmd /c dir *.dmp* /s >> C:\\Tmp_Check_Log.txt 2>>&1")
        os.system("cmd /c dir *.hdmp* /s >> C:\\Tmp_Check_Log.txt 2>>&1")
        
        # Attempt to delete temporary files and log deletion status
        os.system("cmd /c del ~*.* /s >> C:\\Tmp_Clean_Log.txt 2>>&1")
        os.system("cmd /c del *.tmp* /s >> C:\\Tmp_Clean_Log.txt 2>>&1")
        os.system("cmd /c del *.dmp* /s >> C:\\Tmp_Clean_Log.txt 2>>&1")
        os.system("cmd /c del *.hdmp* /s >> C:\\Tmp_Clean_Log.txt 2>>&1")

# Function to clean the F drive
def clean_F():
    try: 
        os.chdir("F:\\")  # Change directory to F drive
    except:
        print("No drive")
    else:
        # Check for temporary files (.tmp, .dmp, .hdmp) and log them
        os.system("cmd /c dir ~*.* /s >> C:\\Tmp_check_Log.txt 2>>&1")
        os.system("cmd /c dir *.tmp* /s >> C:\\Tmp_Check_Log.txt 2>>&1")
        os.system("cmd /c dir *.dmp* /s >> C:\\Tmp_Check_Log.txt 2>>&1")
        os.system("cmd /c dir *.hdmp* /s >> C:\\Tmp_Check_Log.txt 2>>&1")
        
        # Attempt to delete temporary files and log deletion status
        os.system("cmd /c del ~*.* /s >> C:\\Tmp_Clean_Log.txt 2>>&1")
        os.system("cmd /c del *.tmp* /s >> C:\\Tmp_Clean_Log.txt 2>>&1")
        os.system("cmd /c del *.dmp* /s >> C:\\Tmp_Clean_Log.txt 2>>&1")
        os.system("cmd /c del *.hdmp* /s >> C:\\Tmp_Clean_Log.txt 2>>&1")

# Clean drives C, E, and F
clean_C()
clean_E()
clean_F()
