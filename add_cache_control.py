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
        
        # Add cache-control meta tags after charset
        old_meta = '<meta charset="UTF-8">'
        new_meta = '''<meta charset="UTF-8">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">'''
        
        content = content.replace(old_meta, new_meta)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {filename}')

print('Done!')
