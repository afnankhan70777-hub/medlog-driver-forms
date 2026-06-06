import os

# Read jadeer.html
with open('jadeer.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New Filled Container section
filled_section = '''            <div class="form-group">
                <label style="font-size: 16px; background: #e3f2fd; padding: 10px; border-radius: 8px; display: block; margin-bottom: 15px;">
                    📦 Filled Container / بھرا ہوا کنٹینر
                </label>
                <div class="status-grid" style="grid-template-columns: 1fr 1fr;">
                    <div class="status-option">
                        <input type="radio" name="status" id="waiting_emptying" value="Waiting Nearby Emptying Container Area">
                        <label for="waiting_emptying" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">⏳</span>
                            <strong>Waiting Nearby Emptying</strong><br>
                            <strong style="font-size: 12px; color: #333;">خالی کرنے کے قریب انتظار</strong>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="waiting_loading_filled" value="Waiting Nearby Loading Area">
                        <label for="waiting_loading_filled" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🕐</span>
                            <strong>Waiting Nearby Loading</strong><br>
                            <strong style="font-size: 12px; color: #333;">لوڈنگ کے قریب انتظار</strong>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="loaded_inside" value="Loaded and Inside">
                        <label for="loaded_inside" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">📦</span>
                            <strong>Loaded and Inside</strong><br>
                            <strong style="font-size: 12px; color: #333;">لوڈ شدہ - اندر</strong>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="loaded_outside" value="Loaded and Outside">
                        <label for="loaded_outside" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🚛</span>
                            <strong>Loaded and Outside</strong><br>
                            <strong style="font-size: 12px; color: #333;">لوڈ شدہ - باہر</strong>
                        </label>
                    </div>
                </div>
            </div>'''

# New Empty Container section
empty_section = '''            <div class="form-group">
                <label style="font-size: 16px; background: #e8f5e9; padding: 10px; border-radius: 8px; display: block; margin-bottom: 15px;">
                    🔄 Empty Container / خالی کنٹینر
                </label>
                <div class="status-grid" style="grid-template-columns: 1fr 1fr;">
                    <div class="status-option">
                        <input type="radio" name="status" id="waiting_loading_empty" value="Waiting Nearby Loading Area">
                        <label for="waiting_loading_empty" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">⏳</span>
                            <strong>Waiting Nearby Loading</strong><br>
                            <strong style="font-size: 12px; color: #333;">لوڈنگ کے قریب انتظار</strong>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="waiting_unloading" value="Waiting Nearby Unloading Area">
                        <label for="waiting_unloading" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">🕐</span>
                            <strong>Waiting Nearby Unloading</strong><br>
                            <strong style="font-size: 12px; color: #333;">ان لوڈنگ کے قریب انتظار</strong>
                        </label>
                    </div>
                    <div class="status-option">
                        <input type="radio" name="status" id="unloaded_inside" value="Unloaded but Inside">
                        <label for="unloaded_inside" style="font-size: 13px; padding: 12px 8px;">
                            <span style="font-size: 20px; display: block; margin-bottom: 5px;">✅</span>
                            <strong>Unloaded but Inside</strong><br>
                            <strong style="font-size: 12px; color: #333;">خالی ہوا - اندر ہے</strong>
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

# Find and replace both sections
# Find Filled Container section
filled_start = '<label style="font-size: 16px; background: #e3f2fd;'
filled_end = '</div>\n            \n            <div class="form-group">\n                <label style="font-size: 16px; background: #e8f5e9;'

if filled_start in content and filled_end in content:
    start_pos = content.find(filled_start)
    end_pos = content.find(filled_end, start_pos)
    
    if end_pos > start_pos:
        before = content[:start_pos]
        after = content[end_pos:]
        content = before + filled_section + '\n            \n            ' + after
        print('Updated Filled Container section')

# Find Empty Container section  
empty_start = '<label style="font-size: 16px; background: #e8f5e9;'
empty_end = '</div>\n                </div>\n            </div>\n            \n            <div class="form-group">\n                <label style="font-size: 16px;"'

if empty_start in content:
    start_pos = content.find(empty_start)
    # Find the end of this section
    end_marker = '</div>\n            \n            <div class="form-group">\n                <label style="font-size: 16px;">🗺️'
    end_pos = content.find(end_marker, start_pos)
    
    if end_pos > start_pos:
        before = content[:start_pos]
        after = content[end_pos:]
        content = before + empty_section + '\n            \n            ' + after
        print('Updated Empty Container section')

with open('jadeer.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')
