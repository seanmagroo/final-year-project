# final-year-project



Dependencies:

Python3

Flask

Node.js + npm

DeSmuME with Lua scripting

Pokémon Renegade Platinum



Installation:

python -m pip install flask

npm install



Running the Application:

Start DeSmuME emulator, load Renegade Platinum and run Lua/party\_reader in the emulators Lua scripting interface



Run the Backend:

open terminal in backend folder, enter this command: python -m flask --app api run



Run the Frontend:

open a seperate terminal in frontend folder, enter this command: npm run dev

You can also try this command if the previous does not work: npm.cmd run dev



Open the App:

http://localhost:5173



Keep emulator, Lua script, backend and frontend running while using the tracker



Testing without DeSmuME:

&#x09;Two sample Pokémon parties are provided in Lua/data as sample1.json and sample2.json.



&#x09;To test without DeSmuME

&#x09;	1.Start backend and front end as instructed above

&#x09;	2.Move live\_data.json to Lua/data/liveDataSamples

&#x09;	3.copy either sample1.json or sample2.json into Lua/data folder and rename it to: live\_data.json

&#x09;	4.Frontend will display the new data set in the UI



NOTE:	The Renegade Platinum ROM and DeSmuMe emulator is not included with this application.



&#x09;DOWNLOAD AT YOUR OWN DISCRETION

&#x09;A copy of the DeSmuME emulator can be obtained from: http://desmume.org/

&#x09;Pokémon Platinum ROM can be patched to Renegade Platinum using the patcher in the following google drive: https://drive.google.com/drive/folders/1gM7nse4qGKJMkcvlQwf5wPVbXwPcC4XV



&#x09;Due to copyright reasons, I cannot provide a download link for a Pokémon Platinum ROM





