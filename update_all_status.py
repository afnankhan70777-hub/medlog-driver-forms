import os

vendor_files = [
    'al_shaks.html', 'al_turq.html', 'dalel_aljawda.html',
    'modern_east.html', 'move_time.html', 'sadan.html',
    'safe_genset.html', 'safe_journey.html', 'khutut_alajyal.html'
]

# New status section
new_status = '''            <div class="form-group">
                <label style="font-size: 16px;">📍 Current Status / موجودہ حالت</label>
                <div class="status-grid" style="grid-template-columns: 1fr 1fr;">
                    <div class="status-option">
                        <input type="radio" name="status" id="loaded_inside" value="Loaded and Inside">
                        <label for="loaded_inside" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">📦</span>
                            <strong>Loaded and Inside</strong><br>
                            <span style="font-size: 11px; opacity: 0.8;">لوڈ شدہ - اندر</span>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="loaded_left" value="Loaded and Left">
                        <label for="loaded_left" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🚛</span>
                            <strong>Loaded and Left</strong><br>
                            <span style="font-size: 11px; opacity: 0.8;">لوڈ شدہ - چلے گئے</span>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="unloaded_inside" value="Unloaded and Inside">
                        <label for="unloaded_inside" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">✅</span>
                            <strong>Unloaded and Inside</strong><br>
                            <span style="font-size: 11px; opacity: 0.8;">خالی - اندر</span>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="unloaded_outside" value="Unloaded and Outside">
                        <label for="unloaded_outside" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🚪</span>
                            <strong>Unloaded and Outside</strong><br>
                            <span style="font-size: 11px; opacity: 0.8;">خالی - باہر</span>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="nearby_loading" value="Nearby Loading Area">
                        <label for="nearby_loading" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">⏳</span>
                            <strong>Nearby Loading Area</strong><br>
                            <span style="font-size: 11px; opacity: 0.8;">لوڈنگ ایریا کے قریب</span>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="nearby_unloading" value="Nearby Unloading Area">
                        <label for="nearby_unloading" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🕐</span>
                            <strong>Nearby Unloading Area</strong><br>
                            <span style="font-size: 11px; opacity: 0.8;">لوڈ اتارنے والی جگہ کے قریب</span>
                        </label>
                    </div>
                </div>
            </div>'''

for filename in vendor_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the old status section and replace it
        # Look for the pattern from "Kahan Hain" to the end of status div
        start_marker = '<label style="font-size: 16px;">📍 Kahan Hain?'
        end_marker = '</div>\n            \n            <div class="form-group">\n                <label style="font-size: 16px;">🗺️'
        
        if start_marker in content:
            start_pos = content.find(start_marker)
            end_pos = content.find(end_marker, start_pos)
            
            if end_pos > start_pos:
                before = content[:start_pos]
                after = content[end_pos:]
                content = before + '<label style="font-size: 16px;">📍 Current Status / موجودہ حالت</label>' + new_status.split('</label>')[1] + after
                print(f'Updated: {filename}')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print('Done!')
