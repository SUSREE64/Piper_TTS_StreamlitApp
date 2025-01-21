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

This app has two ways of converting text to speach. 1. From the Text Area where in you type the text that needs to be converted to Audio 2. You can upload a *.txt file to convert that to Audio file. <br>
First from the upload/browse .onnx Language Model file uploader. Select the .onnx file. Next if you wish to upload the file, make sure the Text area is empty. Once you choose the file *.txt file and upload<br>

![image](https://github.com/user-attachments/assets/eba3709a-9a8c-466f-946a-9e4e3f193213)
You will see a Button visible "Convert Uploaded file to Audio". Click this to generate Audio file. 
![image](https://github.com/user-attachments/assets/80a1c4b3-4c55-4da2-9a44-c1834217a53e) 
Now the green Message appears indicating the speech synthesized from file "path\*.txt" Now the audio file is created and stored in a folder inside the piper folder /out_files/output.wav. 
This file gets written ( Over written) each time the Audio file is generated either from txt file upload or from the text area text. <br>
You can click the Play Audio button to Listen to the output.wav file. 

Optionally, if you want to save the file to another location etc, you can do so with Windows File browser. 




