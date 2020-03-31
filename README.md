# Voice Command

Voice Command is a simple program to control your PC by your voice. It allows you to bind voice commands to keybindings.

## Installation

+ Install Python
+ Install pip
+ Run the following commands:

```shell
git clone https://github.com/SimonBrandner/VoiceCommand.git
cd VoiceCommand
python3 install.py
```

## Running

+ Run the following:

```shell
python3 main.py <config-file>
```

+ Example

```shell
python3 main.py configExamples/EliteDangerous.json
```

+ Say any of the voiceCommands. For example "show fps" and the key combination "ctrl+f" will be pressed.
+ For quiting say "quit"

## Examples

In the configExamples directory you can find example config files written in JSON.Currently there's just one for controlling your Elite Dangerous spaceship by voice.
