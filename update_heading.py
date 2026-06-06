import os

vendor_files = [
    'al_shaks.html', 'al_turq.html', 'dalel_aljawda.html',
    'modern_east.html', 'move_time.html', 'sadan.html',
    'safe_genset.html', 'safe_journey.html', 'khutut_alajyal.html'
]

for filename in vendor_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace location label
        content = content.replace(
            '<label style="font-size: 16px;">🗺️ Location / مقام <span style="color: red;">*</span></label>',
            '<label style="font-size: 16px;">🗺️ Current Location / موجودہ مقام</label>'
        )
        
        # Remove required from location
        content = content.replace('name="location" required style=', 'name="location" style=')
        
        # Update placeholder
        content = content.replace(
            '<option value="">-- Select Location / مقام منتخب کریں --</option>',
            '<option value="">-- Select / منتخب کریں --</option>'
        )
        
        # Remove required from status
        content = content.replace('value="Loaded and Inside" required>', 'value="Loaded and Inside">')
        
        # Find location select end and add heading to
        marker = '</select>\n            </div>\n            \n            <div class="form-group">\n                <label style="font-size: 16px;">📸'
        if marker in content:
            heading_section = '''</select>
            </div>
            
            <div class="form-group">
                <label style="font-size: 16px;">🎯 Heading To / کہاں جا رہے ہیں</label>
                <select name="heading_to" style="font-size: 16px;">
                    <option value="">-- Select Destination / منزل منتخب کریں --</option>
                    <option value="Dammam Port">⚓ Dammam Port / دمام بندرگاہ</option>
                    <option value="Jubail Port">⚓ Jubail Port / الجبیل بندرگاہ</option>
                    <option value="Riyadh">🏙️ Riyadh / ریاض</option>
                    <option value="Jeddah">🏙️ Jeddah / جدہ</option>
                    <option value="Factory">🏭 Factory / فیکٹری</option>
                    <option value="Warehouse">🏢 Warehouse / گودام</option>
                    <option value="Border">🛂 Border / سرحد</option>
                    <option value="Waiting for Load">⏳ Waiting for Load / لوڈ کا انتظار</option>
                    <option value="Other">📍 Other / دیگر</option>
                </select>
            </div>
            
            <div class="form-group">
                <label style="font-size: 16px;">📸'''
            
            content = content.replace(marker, heading_section)
            print(f'Updated: {filename}')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print('Done!')
