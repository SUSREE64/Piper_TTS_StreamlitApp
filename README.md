# Piper_TTS_StreamlitApp
Streamlit application to Use Piper TTS for Text to Speech conversion. 
#### Installation and Running steps. 
Step1 : Install Piper from its git repository. https://github.com/rhasspy/piper/releases -- Download "piper_windows_amd64.zip" and unzip the folder content to your folder of choice. <br>
Under the extracted folder you can see a folder with name "piper" in which "piper.exe" is located. Under this folder create a folder "models_configs" to store the language models and thier config files.
Step2 : From Voices folder choose the files https://github.com/rhasspy/piper/blob/master/VOICES.md -- select the [Mode], [config] files to download <br>
Note for each voice two files with the same name one "onnx" another "Json" file with the same name are needed to be together in the same directory. <br>
Example :  "en_GB-alan-low.onnx" and "en_GB-alan-low.onnx(Json file)" : 
step2: In the app.py change the config_dict to suit your installed folders. <br>
ste3: Create a python or conda virtual environment with the name of your choice. <br>
step4: The requirements.txt show the necessary packages except streamlit all other packages are included in standard python installation. Make sure your enviroment has all the necessary packages<br>
step5: From your IDE of your choice at command Terminal run the command "streamlit run app.py"
This Opens up streamlit app interface as shown below. 
![image](https://github.com/user-attachments/assets/98370a20-220f-4a39-bc0d-8d647f16ea46)





