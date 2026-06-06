import os

# Read current file
with open('jadeer.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the position after the truck info div
marker = '</div>'
# Find the end of the truck div
pos = content.find('</div>', content.find('id="truck"'))
pos = content.find('</div>', pos + 6)  # Find the next closing div

# Get the part before status sections (up to and including truck div)
before = content[:pos + 6]

# Find where the location section starts
location_start = content.find('<div class="form-group">', content.find('empty_offloaded_outside'))
location_start = content.find('<div class="form-group">', location_start + 1)

# Get the part from location section onwards
after = content[location_start:]

# New two-column status sections
new_sections = '''
            
            <!-- Two Column Layout for Status Sections -->
            <div class="form-group" style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                <!-- Empty Container Section (Left) -->
                <div>
                    <label style="font-size: 14px; background: #e8f5e9; padding: 10px; border-radius: 8px; display: block; margin-bottom: 10px; text-align: center;">
                        🔄 Empty Container<br>خالی کنٹینر
                    </label>
                    <div class="status-grid" style="grid-template-columns: 1fr;">
                        <div class="status-option">
                            <input type="radio" name="status" id="waiting_loading_empty" value="Waiting Nearby Loading Area">
                            <label for="waiting_loading_empty" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">⏳</span>
                                <strong>Waiting Nearby Loading</strong><br>
                                <strong style="font-size: 11px; color: #333;">لوڈنگ کے قریب انتظار</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="waiting_unloading" value="Waiting Nearby Unloading Area">
                            <label for="waiting_unloading" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">🕐</span>
                                <strong>Waiting Nearby Unloading</strong><br>
                                <strong style="font-size: 11px; color: #333;">ان لوڈنگ کے قریب انتظار</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="unloaded_inside" value="Unloaded but Inside">
                            <label for="unloaded_inside" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">✅</span>
                                <strong>Unloaded but Inside</strong><br>
                                <strong style="font-size: 11px; color: #333;">خالی ہوا - اندر</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="empty_left" value="Empty and Left">
                            <label for="empty_left" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">🚗</span>
                                <strong>Empty and Left</strong><br>
                                <strong style="font-size: 11px; color: #333;">خالی - چلے گئے</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="empty_returning" value="Empty - Returning">
                            <label for="empty_returning" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">🛣️</span>
                                <strong>Empty - Returning</strong><br>
                                <strong style="font-size: 11px; color: #333;">خالی - واپس</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="loaded_but_inside" value="Loaded but Inside">
                            <label for="loaded_but_inside" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">📦</span>
                                <strong>Loaded but Inside</strong><br>
                                <strong style="font-size: 11px; color: #333;">لوڈ شدہ - اندر</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="loaded_and_left" value="Loaded and Left">
                            <label for="loaded_and_left" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">🚚</span>
                                <strong>Loaded and Left</strong><br>
                                <strong style="font-size: 11px; color: #333;">لوڈ شدہ - چلے گئے</strong>
                            </label>
                        </div>
                    </div>
                </div>
                
                <!-- Filled Container Section (Right) -->
                <div>
                    <label style="font-size: 14px; background: #e3f2fd; padding: 10px; border-radius: 8px; display: block; margin-bottom: 10px; text-align: center;">
                        📦 Filled Container<br>بھرا ہوا کنٹینر
                    </label>
                    <div class="status-grid" style="grid-template-columns: 1fr;">
                        <div class="status-option">
                            <input type="radio" name="status" id="waiting_emptying" value="Waiting Nearby Emptying Container Area">
                            <label for="waiting_emptying" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">⏳</span>
                                <strong>Waiting Nearby Emptying</strong><br>
                                <strong style="font-size: 11px; color: #333;">خالی کرنے کے قریب انتظار</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="waiting_loading_filled" value="Waiting Nearby Loading Area">
                            <label for="waiting_loading_filled" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">🕐</span>
                                <strong>Waiting Nearby Loading</strong><br>
                                <strong style="font-size: 11px; color: #333;">لوڈنگ کے قریب انتظار</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="loaded_inside" value="Loaded and Inside">
                            <label for="loaded_inside" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">📦</span>
                                <strong>Loaded and Inside</strong><br>
                                <strong style="font-size: 11px; color: #333;">لوڈ شدہ - اندر</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="loaded_outside" value="Loaded and Outside">
                            <label for="loaded_outside" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">🚛</span>
                                <strong>Loaded and Outside</strong><br>
                                <strong style="font-size: 11px; color: #333;">لوڈ شدہ - باہر</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="empty_left_filled" value="Empty and Left">
                            <label for="empty_left_filled" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">🚗</span>
                                <strong>Empty and Left</strong><br>
                                <strong style="font-size: 11px; color: #333;">خالی - چلے گئے</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="empty_returning_filled" value="Empty - Returning">
                            <label for="empty_returning_filled" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">🛣️</span>
                                <strong>Empty - Returning</strong><br>
                                <strong style="font-size: 11px; color: #333;">خالی - واپس</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="waiting_returning_empty" value="Waiting Nearby Returning Empty Container Area">
                            <label for="waiting_returning_empty" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">🔄</span>
                                <strong>Waiting Nearby Returning</strong><br>
                                <strong style="font-size: 11px; color: #333;">خالی واپسی کے قریب</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="empty_offloaded_inside" value="Empty Container Offloaded but Inside">
                            <label for="empty_offloaded_inside" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">📍</span>
                                <strong>Empty Offloaded Inside</strong><br>
                                <strong style="font-size: 11px; color: #333;">خالی اتارا - اندر</strong>
                            </label>
                        </div>
                        <div class="status-option">
                            <input type="radio" name="status" id="empty_offloaded_outside" value="Empty Container Offloaded and Outside">
                            <label for="empty_offloaded_outside" style="font-size: 12px; padding: 10px 5px;">
                                <span style="font-size: 18px; display: block; margin-bottom: 3px;">🚪</span>
                                <strong>Empty Offloaded Outside</strong><br>
                                <strong style="font-size: 11px; color: #333;">خالی اتارا - باہر</strong>
                            </label>
                        </div>
                    </div>
                </div>
            </div>'''

# Combine
new_content = before + new_sections + after

# Write back
with open('jadeer.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated jadeer.html with two-column layout')
