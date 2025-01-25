# Welcome to this new environment
import streamlit as st
import os
import subprocess  # Use for executing shell commands
import time
import wave
import piper_installer

# Run installer
piper_installer.run_piper_installer()
# config parameters
config_dict = {"piper_folder ": "/home/user/piper_installation/piper",
               "out_folder": "output_files", "output_wav":"out_file",
               "hf_models": "/home/user/app/models_config"}

piper_folder = config_dict['piper_folder ']
out_file = config_dict['output_wav']
out_folder = config_dict['out_folder']
hf_models = config_dict['hf_models'] # --- new
#model_file = os.path.join(hf_root, "en_GB-alan-low.onnx")
os.chmod(hf_models, 0o755)


# Function to create a text file from the content entered in text area.
def create_txt_file(text_content, file_name):
    file_name = os.path.join(piper_folder, file_name)
    with open(file_name, "w") as f:
        f.write(text_content)
    return file_name

#example usage from piper github documentation
# echo 'Welcome to the world of speech synthesis!' | \
#   ./piper --model en_US-lessac-medium.onnx --output_file welcome.wav

# Function to format the piper command string and execute the same.
def run_piper_tts(text):
    command = "cat" + " " + text + " | " + " " "./piper" + " " + "--model "+ model_file + " " + "-f " + "./" + out_folder + "/" + out_file
    print(command)
    subprocess.run(command, shell=True, cwd=piper_folder)


#function to select Model file from root/models_config folder. 

def get_model_files(models_folder):
    try:
        return [f for f in os.listdir(models_folder) if f.endswith(".onnx")]
    except Exception as e:
        st.sidebar.error("Failed to fetch models from the directory")
        
#Modle selection side bar
models = get_model_files(hf_models)
model_file = st.sidebar.selectbox("select a.onnx Modle", options = models, format_func = lambda x: x if x else "No model found")
model_file = os.path.join(hf_models, model_file)
os.chmod(model_file, 0o755)
# st.sidebar.header("Model onnx file Selection")
# onnx_file = st.sidebar.file_uploader("Upload a .onnx Language Model", type=["onnx"])
txt_file = st.sidebar.file_uploader("Upload a .txt file for conversion", type=["txt"])

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
        st.success(f" 👍 Speech synthesized from file: {uploaded_file_path}")
####
col1, col2, col3, col4 = st.columns(4)
with col1:
    text_convert = st.button("📝Text to Audio")
if model_file and text_input.strip():
        run_piper_tts(text_file)
        st.success(f" 👍  Speech synthesized to:{piper_folder}\\{out_folder}\\{out_file}")
with col4:
    play_button = st.button("🔊 Make Audio")


if play_button:
    wav_path = os.path.join(piper_folder, out_folder, out_file)
    if os.path.exists(wav_path):
        st.info(f"Audio file ready: {wav_path}")

        # Add a download button for the WAV file
        with open(wav_path, "rb") as file:
            st.download_button(
                label="⏬ Download Audio File",
                data=file,
                file_name="output_audio.wav",
                mime="audio/wav"
            )

        # Optionally, render the audio player in the browser
        st.audio(wav_path, format='audio/wav')

        with wave.open(wav_path, 'rb') as wav_file:
            duration = wav_file.getnframes() / wav_file.getframerate()

        # Initialize progress bar
        progress_bar = st.progress(0)

        # Simulate playback progress
        steps = 100  # Number of updates
        sleep_time = duration / steps  # Time per progress bar step
        for step in range(steps):
            time.sleep(sleep_time)
            progress_bar.progress(step + 1)

        progress_bar.empty()  # Clear the progress bar
        st.success("👍 Playback simulation completed!")
    else:
        st.error("Audio file not found!")
