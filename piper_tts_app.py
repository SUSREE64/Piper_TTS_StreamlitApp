import streamlit as st
import os
import subprocess  # Use for executing shell commands
import winsound
import time
import wave

# config parameters
config_dict = {"piper_folder ": "D:\\piper_windows_amd64\\piper", "output_wav": "output.wav",
               "out_folder": "output_files"}
piper_folder = config_dict['piper_folder ']
out_file = config_dict['output_wav']
out_folder = config_dict['out_folder']


# Function to create a text file from the content entered in text area.
def create_txt_file(text_content, file_name):
    file_name = os.path.join(piper_folder, file_name)
    with open(file_name, "w") as f:
        f.write(text_content)
    return file_name


# Function tp format the piper command string and execute the same.
def run_piper_tts(text):
    command = "type" + " " + text + " | " + " " ".\\piper.exe" + " " + "-m " + ".\\models_configs\\" + model_file + " " + "-f " + ".\\" + out_folder + "\\" + out_file
    print(command)
    subprocess.run(command, shell=True, cwd=piper_folder)


# App Sidebar
st.sidebar.header("Model onnx file Selection")
onnx_file = st.sidebar.file_uploader("Upload a .onnx Language Model", type=["onnx"])
txt_file = st.sidebar.file_uploader("Upload a .txt file for conversion", type=["txt"])

if onnx_file:
    model_file = onnx_file.name
else:
    model_file = ""

# Main Panel
st.title("🗣️ Piper Text to Speech App")
st.write("Enter the text below to synthesize speech.")

text_input = st.text_area("Enter text to convert to speech:", height=200)
if not text_input.strip():
    st.warning("Please enter text to convert to speech.")
else:
    text_file = create_txt_file(text_input, "content.txt")

#####
if txt_file is not None:
    if st.sidebar.button("📁 Convert Uploaded File to Audio"):
        # Save uploaded file content to a new text file
        file_name = "uploaded_content.txt"
        uploaded_file_path = os.path.join(piper_folder, file_name)
        with open(uploaded_file_path, "wb") as f:
            f.write(txt_file.getbuffer())

        # Run Piper TTS for the uploaded file
        run_piper_tts(uploaded_file_path)
        st.success(f"Speech synthesized from file: {uploaded_file_path}")
####
col1, col2, col3, col4 = st.columns(4)
with col1:
    text_convert = st.button("📝Text to Audio")
if model_file and text_input.strip():
        run_piper_tts(text_file)
        st.success(f"Speech synthesized to:{piper_folder}\\{out_folder}\\{out_file}")
with col4:
    play_button = st.button("🔊 Play Audio")
if play_button:
    wav_path = os.path.join(piper_folder, out_folder, out_file)
    if os.path.exists(wav_path):
        st.info(f"Playing audio file: {wav_path}")

        with wave.open(wav_path, 'rb') as wav_file:
            duration = wav_file.getnframes() / wav_file.getframerate()

        # Initialize progress bar
        progress_bar = st.progress(0)

        # Play audio asynchronously
        winsound.PlaySound(wav_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

        # Update progress bar in sync with audio duration
        steps = 100  # Number of updates
        sleep_time = duration / steps  # Time per progress bar step
        for step in range(steps):
            time.sleep(sleep_time)
            progress_bar.progress(step + 1)

        winsound.PlaySound(None, winsound.SND_PURGE)  # Stop sound after completion
        progress_bar.empty()  # Clear the progress bar
        st.success("Playback completed!")
    else:
        st.error("Audio file not found!")
