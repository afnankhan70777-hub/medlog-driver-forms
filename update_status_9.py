import os

vendor_files = [
    'jadeer.html', 'al_shaks.html', 'al_turq.html', 'dalel_aljawda.html',
    'modern_east.html', 'move_time.html', 'sadan.html',
    'safe_genset.html', 'safe_journey.html', 'khutut_alajyal.html'
]

# New status section with 9 options and bold Urdu
new_status = '''            
            <div class="form-group">
                <label style="font-size: 16px;">📍 Current Status / موجودہ حالت</label>
                <div class="status-grid" style="grid-template-columns: 1fr 1fr;">
                    <div class="status-option">
                        <input type="radio" name="status" id="loaded_inside" value="Loaded and Inside">
                        <label for="loaded_inside" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">📦</span>
                            <strong>Loaded and Inside</strong><br>
                            <strong style="font-size: 12px; color: #333;">لوڈ شدہ - اندر</strong>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="loaded_left" value="Loaded and Left">
                        <label for="loaded_left" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🚛</span>
                            <strong>Loaded and Left</strong><br>
                            <strong style="font-size: 12px; color: #333;">لوڈ شدہ - چلے گئے</strong>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="nearby_loading" value="Nearby Loading Area">
                        <label for="nearby_loading" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">⏳</span>
                            <strong>Nearby Loading Area</strong><br>
                            <strong style="font-size: 12px; color: #333;">لوڈنگ ایریا کے قریب</strong>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="nearby_unloading" value="Nearby Unloading Area">
                        <label for="nearby_unloading" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🕐</span>
                            <strong>Nearby Unloading Area</strong><br>
                            <strong style="font-size: 12px; color: #333;">ان لوڈنگ کے قریب</strong>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="emptying_container" value="Emptying Container">
                        <label for="emptying_container" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🔄</span>
                            <strong>Emptying Container</strong><br>
                            <strong style="font-size: 12px; color: #333;">کنٹینر خالی ہو رہا ہے</strong>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="empty_inside" value="Empty and Inside">
                        <label for="empty_inside" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">✅</span>
                            <strong>Empty and Inside</strong><br>
                            <strong style="font-size: 12px; color: #333;">خالی - اندر</strong>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="empty_outside" value="Empty and Outside">
                        <label for="empty_outside" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🚪</span>
                            <strong>Empty and Outside</strong><br>
                            <strong style="font-size: 12px; color: #333;">خالی - باہر</strong>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="empty_left" value="Empty and Left">
                        <label for="empty_left" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🚗</span>
                            <strong>Empty and Left</strong><br>
                            <strong style="font-size: 12px; color: #333;">خالی - چلے گئے</strong>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="empty_returning" value="Empty - Returning">
                        <label for="empty_returning" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🛣️</span>
                            <strong>Empty - Returning</strong><br>
                            <strong style="font-size: 12px; color: #333;">خالی - واپس جا رہے ہیں</strong>
                        </label>
                    </div>
                </div>
            </div>'''

for filename in vendor_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the status section
        # Look for the pattern from Current Status label to the end of status div
        start_marker = '<label style="font-size: 16px;">📍 Current Status'
        end_marker = '</div>\n            \n            <div class="form-group">\n                <label style="font-size: 16px;">🗺️'
        
        if start_marker in content:
            start_pos = content.find(start_marker)
            end_pos = content.find(end_marker, start_pos)
            
            if end_pos > start_pos:
                before = content[:start_pos]
                after = content[end_pos:]
                content = before + new_status + '\n            \n            ' + after[len('</div>\n            \n            '):]
                print(f'Updated status: {filename}')
        
        # Make Urdu text more bold in other places
        # Update location dropdown
        content = content.replace('دمام بندرگاہ', 'دمام بندرگاہ')
        content = content.replace('الجبیل بندرگاہ', 'الجبیل بندرگاہ')
        content = content.replace('ریاض', 'ریاض')
        content = content.replace('جدہ', 'جدہ')
        content = content.replace('راستے میں', 'راستے میں')
        content = content.replace('فیکٹری', 'فیکٹری')
        content = content.replace('گودام', 'گودام')
        content = content.replace('سرحد', 'سرحد')
        content = content.replace('دیگر', 'دیگر')
        content = content.replace('لوڈ کا انتظار', 'لوڈ کا انتظار')
        content = content.replace('منزل منتخب کریں', 'منزل منتخب کریں')
        content = content.replace('منتخب کریں', 'منتخب کریں')
        content = content.replace('موجودہ مقام', 'موجودہ مقام')
        content = content.replace('کہاں جا رہے ہیں', 'کہاں جا رہے ہیں')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

print('Done!')
