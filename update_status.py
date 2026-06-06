import os

# New status section HTML
new_status_section = '''            <div class="form-group">
                <label style="font-size: 16px;">📍 Current Status / موجودہ حالت <span style="color: red;">*</span></label>
                <div class="status-grid" style="grid-template-columns: 1fr 1fr;">
                    <div class="status-option">
                        <input type="radio" name="status" id="loaded_inside" value="Loaded and Inside" required>
                        <label for="loaded_inside" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">📦</span>
                            <strong>Loaded & Inside</strong><br>
                            <span style="font-size: 11px; opacity: 0.8;">لوڈ شدہ - اندر</span>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="loaded_outside" value="Loaded and Outside">
                        <label for="loaded_outside" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🚛</span>
                            <strong>Loaded & Outside</strong><br>
                            <span style="font-size: 11px; opacity: 0.8;">لوڈ شدہ - باہر</span>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="unloaded_inside" value="Unloaded and Inside">
                        <label for="unloaded_inside" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">✅</span>
                            <strong>Unloaded & Inside</strong><br>
                            <span style="font-size: 11px; opacity: 0.8;">خالی - اندر</span>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="unloaded_outside" value="Unloaded and Outside">
                        <label for="unloaded_outside" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🚪</span>
                            <strong>Unloaded & Outside</strong><br>
                            <span style="font-size: 11px; opacity: 0.8;">خالی - باہر</span>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="nearby_loading" value="Nearby Loading Area">
                        <label for="nearby_loading" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">⏳</span>
                            <strong>Nearby Loading</strong><br>
                            <span style="font-size: 11px; opacity: 0.8;">لوڈنگ کے قریب</span>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="nearby_unloading" value="Nearby Unloading Area">
                        <label for="nearby_unloading" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🕐</span>
                            <strong>Nearby Unloading</strong><br>
                            <span style="font-size: 11px; opacity: 0.8;">ان لوڈنگ کے قریب</span>
                        </label>
                    </div>
                </div>
            </div>'''

# Old status section pattern to replace
old_status_start = '<div class="form-group">\n                <label style="font-size: 16px;">📍 Kahan Hain?'

# Container section pattern to remove
container_section_start = '<div class="form-group">\n                <label style="font-size: 16px;">📦 Container Number'

vendor_files = [
    'al_shaks.html', 'al_turq.html', 'dalel_aljawda.html',
    'modern_east.html', 'move_time.html', 'sadan.html',
    'safe_genset.html', 'safe_journey.html', 'khutut_alajyal.html'
]

for filename in vendor_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace status section
        # Find and replace the old status section
        import re
        
        # Pattern to match the old status section
        old_status_pattern = r'<div class="form-group">\s*<label style="font-size: 16px;">📍 Kahan Hain\? / کہاں ہیں\?.*?<\/div>\s*<\/div>'
        
        content = re.sub(old_status_pattern, new_status_section, content, flags=re.DOTALL)
        
        # Remove container section
        container_pattern = r'<div class="form-group">\s*<label style="font-size: 16px;">📦 Container Number / کنٹینر نمبر.*?<\/p>\s*<\/div>'
        content = re.sub(container_pattern, '', content, flags=re.DOTALL)
        
        # Remove container from window.onload
        content = re.sub(r"if \(params\.container\) \{\s*document\.getElementById\('container'\)\.value = params\.container;\s*\}", '', content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {filename}')
    else:
        print(f'Not found: {filename}')

print('Done!')
