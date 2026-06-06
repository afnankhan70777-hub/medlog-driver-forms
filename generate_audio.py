from gtts import gTTS
import os

# Create audio directory if not exists
os.makedirs('audio', exist_ok=True)

# Audio files to generate
audio_files = {
    # Empty Container Section
    'waiting_loading.mp3': 'لوڈنگ کے قریب انتظار کر رہے ہیں',
    'waiting_unloading.mp3': 'ان لوڈنگ کے قریب انتظار کر رہے ہیں',
    'unloaded_inside.mp3': 'خالی ہوا، اندر ہے',
    'empty_left.mp3': 'خالی ہے، چلے گئے',
    'empty_returning.mp3': 'خالی ہے، واپس جا رہے ہیں',
    'loaded_but_inside.mp3': 'لوڈ شدہ، اندر ہے',
    'loaded_and_left.mp3': 'لوڈ شدہ، چلے گئے',
    
    # Filled Container Section
    'waiting_emptying.mp3': 'خالی کرنے کے قریب انتظار کر رہے ہیں',
    'waiting_loading_filled.mp3': 'لوڈنگ کے قریب انتظار کر رہے ہیں',
    'loaded_inside.mp3': 'لوڈ شدہ، اندر ہے',
    'loaded_outside.mp3': 'لوڈ شدہ، باہر ہے',
    'empty_left_filled.mp3': 'خالی ہے، چلے گئے',
    'empty_returning_filled.mp3': 'خالی ہے، واپس جا رہے ہیں',
    'waiting_returning.mp3': 'خالی کنٹینر واپسی کے قریب انتظار کر رہے ہیں',
    'offloaded_inside.mp3': 'خالی اتارا، اندر ہے',
    'offloaded_outside.mp3': 'خالی اتارا، باہر ہے',
}

print("Generating Urdu audio files...")
print("=" * 50)

for filename, text in audio_files.items():
    filepath = os.path.join('audio', filename)
    try:
        # Create gTTS object with Urdu language
        tts = gTTS(text=text, lang='ur', slow=False)
        # Save the audio file
        tts.save(filepath)
        print(f"✅ Created: {filename}")
    except Exception as e:
        print(f"❌ Error creating {filename}: {e}")

print("=" * 50)
print("Done! Audio files saved in audio/ folder")
print(f"Total files created: {len(audio_files)}")
