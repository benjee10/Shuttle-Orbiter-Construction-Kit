#Modify the cfg text for each part.
import os

folder_path = r'C:\Games\KSP\1.12.5 Stock\GameData\Benjee10_shuttleOrbiter\Parts'
field_name_1 = 'title'
field_name_2 = 'description'
field_name_3 = 'name'

for dirpath, dirnames, filenames in os.walk(folder_path):
    folder_name = os.path.basename(dirpath)
    for filename in filenames:
        if filename.endswith('.cfg'):
            with open(os.path.join(dirpath, filename), 'r') as file:
                content = file.read()
                lines = content.split('\n')
                field_value_3 = ''
                found_field_1 = False
                found_field_2 = False
                found_field_3 = False
                flag = False
                for i, line in enumerate(lines):
                    if field_name_1 in line and not found_field_1:
                        lines[i] = f'\ttitle = #LOC_{field_value_3}_title'
                        found_field_1 = True
                    if field_name_2 in line and not found_field_2:
                        lines[i] = f'\tdescription = #LOC_{field_value_3}_description'
                        found_field_2 = True
                    if flag == False:
                        if field_name_3 in line and not found_field_3:
                            field_value_3 = line.split('=')[1].strip()
                            found_field_3 = True
                            flag = True
                    if found_field_1 and found_field_2 and found_field_3:
                        break
                content = '\n'.join(lines)
            with open(os.path.join(dirpath, filename), 'w') as file:
                file.write(content)

