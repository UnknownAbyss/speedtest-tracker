# speedtest-tracker
Speedtest python file that stores speedtests over time. Then you can use the second to show a graph of all your speedtest data over one session

# Requirements
python 3.8

tkinter 
-install however you can

pip install matplotlib speedtest-cli json

# How to use
Clone the git repository to wherever you want. 

To get speeds- 
From the directory run the testSpeeds.py file and let it run for some time. It will take speedtests every interval of time(default:5mins) and store them in a json file in the JSON folder
Each time a reading is successful, you will get a success message in terminal

After you have enough readings, run the getGraph.py file. In the UI you will see a list of all the files you have stored in the middle. just type the name of the one you want to access in the text box and press the button.
Note:- The filename with the higher number is the file with the most recent readings
