from gtts import gTTS
import os

# Create audio directory if it doesn't exist
os.makedirs('audio', exist_ok=True)

# Define the precise Urdu dialogues
audio_files = {
    # Empty Container Section
    'waiting_loading.mp3': 'لوڈ کرنے والی جگہ کے قریب انتظار کر رہے ہیں',
    'waiting_unloading.mp3': 'لوڈ اتارنے والی جگہ کے قریب انتظار کر رہے ہیں',
    'unloaded_inside.mp3': 'لوڈ اتار گیا مگر ابھی بھی اندر ہیں',
    
    # Loaded Container Section (new)
    'loaded_but_inside.mp3': 'لوڈ مل گیا مگر ابھی بھی اندر ہیں',
    'loaded_and_left.mp3': 'لوڈ مل گیا اور نکل گئے',
}

print("Generating audio files with precise Urdu dialogues...")
print("=" * 60)

for filename, text in audio_files.items():
    filepath = os.path.join('audio', filename)
    try:
        tts = gTTS(text=text, lang='ur', slow=False)
        tts.save(filepath)
        print(f"✅ Created: {filename}")
        print(f"   Text: {text}")
        print()
    except Exception as e:
        print(f"❌ Error creating {filename}: {e}")

print("=" * 60)
print("Audio generation complete!")
print("\nFiles created:")
for filename in audio_files.keys():
    filepath = os.path.join('audio', filename)
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        print(f"  - {filename} ({size} bytes)")
