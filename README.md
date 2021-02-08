[![GitHub](https://img.shields.io/github/license/MLH-Fellowship/LarynxCode)](https://github.com/MLH-Fellowship/LarynxCode/blob/master/LICENSE.txt)
![Maintenance](https://img.shields.io/maintenance/yes/2021)

[![GitHub issues](https://img.shields.io/github/issues/MLH-Fellowship/LarynxCode)](https://github.com/MLH-Fellowship/LarynxCode/issues)
[![GitHub forks](https://img.shields.io/github/forks/MLH-Fellowship/LarynxCode?style=social)](https://github.com/MLH-Fellowship/LarynxCode/network/members)
[![GitHub stars](https://img.shields.io/github/stars/MLH-Fellowship/LarynxCode?style=social)](https://github.com/MLH-Fellowship/LarynxCode/stargazers)

<br><br>

<p align="center">
       <img src="https://user-images.githubusercontent.com/49288068/107161201-2678fd00-69c1-11eb-9190-348f7a85b2c7.png" alt="LarynxCode logo" width="300" height="300" />
</p>

<br>

<p align="center">
   <strong>WELCOME TO LARYNXCODE</strong> : A CLI application that enables you to code using your voice
</p>

Coding is an integral part of a developer's life. Sometimes, due to continuous and rigorous coding without breaks, a person may develop a condition known as Repetitive Strain Injury(RSI), that restricts all finger movements. **How will you,then, finish that project that's due in 2 days ?**

**LarynxCode**, based on the functionalities of the dragonfly Python framework, is a CLI appliaction, that fires up voice enabled coding in you system. It also comes with a linked web application that is basic guide on the functions of a few basic commands.

<br>
<p align="center">
       <img src="https://user-images.githubusercontent.com/49288068/107162668-de5ed800-69ca-11eb-9830-fb67340d88b2.png" alt="CLI welcome" width="800" height="300" />
</p>

________________________________________________________________________________________________________________________________________________________________________

**COMMANDS :**

<p align="center">
       <img src="https://user-images.githubusercontent.com/49288068/107163484-bd4cb600-69cf-11eb-8919-1bea32e2a801.png" alt="CLI commands" width="800" height="300" />
</p>
<br>

1. ```enable-voice-coding --voice --start``` : Starts Caster and enables you to code via Windows Speech Recognition

Executing the command :

![Screenshot (447)](https://user-images.githubusercontent.com/49288068/107162897-24686b80-69cc-11eb-8b3e-fa755f57649d.png)

Coding using your voice : Writing print('name') via voice coding :

![Screenshot (448)](https://user-images.githubusercontent.com/49288068/107162928-61346280-69cc-11eb-8d15-a0c892ba0b30.png)

```enable-voice-coding``` help menu :

![Screenshot (449)](https://user-images.githubusercontent.com/49288068/107162964-a9ec1b80-69cc-11eb-80e1-dc65cbe57817.png)

<br><br>
2. ```chelp --casterhelp --google``` : Launches the voice coding commands guide

Executing the command :

![Screenshot (456)](https://user-images.githubusercontent.com/49288068/107163434-778fed80-69cf-11eb-9357-17f2aaa73624.png)

The webapp :

![Screenshot (450)](https://user-images.githubusercontent.com/49288068/107163456-90989e80-69cf-11eb-997d-5a68a173e50d.png)

![Screenshot (452)](https://user-images.githubusercontent.com/49288068/107163454-8ecedb00-69cf-11eb-8256-df129e9e78ce.png)

```chelp``` help menu :

![Screenshot (454)](https://user-images.githubusercontent.com/49288068/107163466-a4dc9b80-69cf-11eb-900a-f7287f92a37c.png)

________________________________________________________________________________________________________________________________________________________________________

**SYSTEM REQUIREMENTS :**

1. Python 2.7.18, 64/32 bit, Python 3.7.4 64 bit
2. Windows OS
3. Pre-trained Windows Speech Recognition GUI : Make sure you train your WSR 2-3 times properly.

**SETTING UP CASTER :**

1. Install dragonfly : ```pip install dragonfly2```
2. Follow the **[official docs](https://caster.readthedocs.io/en/latest/readthedocs/Installation/Windows/Windows_Speech_Recognition/)** only till step 2. LarynxCode automates the remaining setup and runs the algorithm. **NOTE :** Also, instead of installing at C:/Documents, install it in **C:/** directly
3. If you want to change rules/grammar, head over to C:/Caster/castervoice/rules to change the rules.

**SETTING UP LARYNXCODE :**

1. Download this repository as zip, Extract it at **C:/**
2. cd to the directory : ```cd LarynxCode\cli_scripts```
3. Setup a virtual environment : ```py -m virtualenv venv```, and activate it : ```venv\Scripts\activate```
4. Install required libraries : ```pip install -r requirements.txt```
5. Run LarynxCode : ```py voice_coding_cli.py enable-voice-coding --voice --start```  (refer to the commands explained above)

________________________________________________________________________________________________________________________________________________________________________

**SHORTCOMINGS AND FUTURE SCOPE :**

1. Curently runs only on Windows OS.
2. Windows Speech Recognition is poor in terms of identifying dictation, so it takes a lot of time and 5-6 attempts to get the correct command executed. In the future, we aim to shift to Dragon Naturally Speaking (DNS) speech recognition engine, which works the best in voice coding.
3. Voice coding is heavily dependant on Python 2.7.18 till date.

**SHOUTOUTS :**

**[Leshna Balara](https://github.com/leshnabalara)**, for collaborating with me to build the CLI. Shoutout to one of the most dedicated Pod mates ever.

**[Gabriel Cruz](https://github.com/gmelodie)**, for being an exceptional Pod leader. 

**CONTRIBUTE :**

Feel free to raise an Issue if you feel like improving our CLI. LarynxCode is open sourced under the [MIT License.](https://github.com/MLH-Fellowship/LarynxCode/blob/main/LICENSE)

To contribute to the web application (frontend/backend) : **[Raise an Issue at this repository](https://github.com/BALaka-18/LarynxCode_Guide_webapp)**

<br><br>

~ LarynxCode, developed by **[Balaka Biswas](https://github.com/BALaka-18)** and **[Leshna Balara](https://github.com/leshnabalara)**
