import pip

_all_ = [
    "pynput>=1.6.8",
    "pyaudio>=0.2.11",
    "speechrecognition>=3.8.1"
]

windows = []

linux = []

darwin = []

def install(packages):
    for package in packages:
        pip.main(['install', package])

if __name__ == '__main__':

    from sys import platform

    install(_all_) 
    if (platform == 'windows' or platform == 'win32'):
        install(windows)
    if platform.startswith('linux'):
        install(linux)
    if platform == 'darwin': 
        install(darwin)