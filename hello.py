import os
import sys

# Set 1 to enable the welcome print
welcome_print = 1

if welcome_print:
    print("")
    print("##       ####  ######  ######## ##    ##  ######  ########") 
    print("##        ##  ##    ## ##       ###   ## ##    ## ##      ") 
    print("##        ##  ##       ##       ####  ## ##       ##      ") 
    print("##        ##  ##       ######   ## ## ##  ######  ######  ") 
    print("##        ##  ##       ##       ##  ####       ## ##      ") 
    print("##        ##  ##    ## ##       ##   ### ##    ## ##      ") 
    print("######## ####  ######  ######## ##    ##  ######  ########") 
    print("")
    print("Hello, Creative Commons and Open Source\n")

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
elif 'BSD' in content:
    license_type = 'BSD '
    if '2-Clause' in content:
        license_type += '2-Clause'
    elif '3-Clause' in content:
        license_type += '3-Clause'
elif 'Apache License' in content:
    license_type = 'Apache-'
    if 'Version 2' in content:
        license_type += '2.0'
elif 'Mozilla Public License' in content:
    license_type = 'MPL-'
    if 'Version 2' in content:
        license_type += '2.0'
elif 'Eclipse Public License' in content:
    license_type = 'EPL-'
    if 'Version 2' in content:
        license_type += '2.0'
elif 'GNU' in content:
    license_type = 'GNU '
    if 'GNU AFFERO GENERAL PUBLIC LICENSE' in content:
        license_type += 'AGPL-'
        if 'Version 3' in content:
            license_type += '3.0'
    elif 'GNU LESSER GENERAL PUBLIC LICENSE':
        license_type += 'LGPL-'
        if 'Version 2.1' in content:
            license_type += '2.1'
        elif 'Version 3' in content:
            license_type += '3.0'
    elif 'GNU GENERAL PUBLIC LICENSE' in content:
        license_type += 'GPL-'
        if 'Version 2' in content:
            license_type += '2.0'
        elif 'Version 3' in content:
            license_type += '3.0'
elif 'This is free and unencumbered software' in content:
    # which means no rights reserved, AKA Public Domain
    license_type = 'Unlicense'
elif 'Creative Commons' in content:
    if 'CC0 1.0 Universal' in content:
        license_type = 'CC0-1.0'
    elif 'Attribution 4.0 International' in content:
        license_type = 'CC-BY-4.0'
else:
    color_print('yellow', 'Unknown License')
    sys.exit()

color_print('green','The License in project root directory is : ' + license_type)