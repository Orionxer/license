import os
import sys

print("")
print("##       ####  ######  ######## ##    ##  ######  ########") 
print("##        ##  ##    ## ##       ###   ## ##    ## ##      ") 
print("##        ##  ##       ##       ####  ## ##       ##      ") 
print("##        ##  ##       ######   ## ## ##  ######  ######  ") 
print("##        ##  ##       ##       ##  ####       ## ##      ") 
print("##        ##  ##    ## ##       ##   ### ##    ## ##      ") 
print("######## ####  ######  ######## ##    ##  ######  ########") 
print("")
print("Hello, Creative Commons and Open Source")

# define the color_print
def color_print(color, text):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'reset': '\033[0m'
    }
    color_code = colors.get(color.lower(), '')
    print(color_code + text + colors['reset'])

# The license path
license_path = './LICENSE'

# Check if the file exists
if not os.path.exists(license_path):
    color_print('red', "Not found valid LICENSE file, please check again")
    sys.exit()
else:
    # Read the file content
    with open(license_path, 'r') as file:
        content = file.read()

# Detect the license type
license_type = 'Unknown License'

if 'MIT License' in content:
    license_type = 'MIT'
elif 'GNU GENERAL PUBLIC LICENSE' in content:
    if 'Version 2' in content:
        license_type = 'GNU GPL-2.0'
    elif 'Version 3' in content:
        license_type = 'GNU GPL-3.0'
elif 'Apache License' in content:
    license_type = 'Apache'
elif 'This is free and unencumbered software' in content:
    # which means no rights reserved, AKA Public Domain
    license_type = 'Unlicense'
else:
    color_print('yellow', 'Unknown License')
    sys.exit()

color_print('green','The License in project root directory is : ' + license_type)