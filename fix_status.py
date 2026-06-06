import os

vendor_files = [
    'jadeer.html', 'al_shaks.html', 'al_turq.html', 'dalel_aljawda.html',
    'modern_east.html', 'move_time.html', 'sadan.html',
    'safe_genset.html', 'safe_journey.html', 'khutut_alajyal.html'
]

for filename in vendor_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace Loaded & Outside with Loaded and Left
        content = content.replace('Loaded & Outside', 'Loaded and Left')
        content = content.replace('value="Loaded and Outside"', 'value="Loaded and Left"')
        content = content.replace('id="loaded_outside"', 'id="loaded_left"')
        content = content.replace('for="loaded_outside"', 'for="loaded_left"')
        content = content.replace('لوڈ شدہ - باہر', 'لوڈ شدہ - چلے گئے')
        
        # Replace & with and in other statuses
        content = content.replace('Loaded & Inside', 'Loaded and Inside')
        content = content.replace('Unloaded & Inside', 'Unloaded and Inside')
        content = content.replace('Unloaded & Outside', 'Unloaded and Outside')
        
        # Update Nearby Loading/Unloading to include Area
        content = content.replace('>Nearby Loading<', '>Nearby Loading Area<')
        content = content.replace('>Nearby Unloading<', '>Nearby Unloading Area<')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {filename}')

print('Done!')
