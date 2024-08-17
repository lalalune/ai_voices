import os
import sys
import whisper

def transcribe_files(directory):
    # Load the Whisper model
    model = whisper.load_model("base")

    # Get all .wav files in the directory
    wav_files = [f for f in os.listdir(directory) if f.endswith('.wav')]

    for filename in wav_files:
        wav_path = os.path.join(directory, filename)
        txt_filename = os.path.splitext(filename)[0] + '.txt'
        txt_path = os.path.join(directory, txt_filename)

        print(f"Transcribing: {filename}")

        # Transcribe the audio
        result = model.transcribe(wav_path)

        # Save the transcript
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(result["text"])

        print(f"Transcript saved: {txt_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <directory_path>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)
    
    transcribe_files(directory)
    print("Transcription completed.")