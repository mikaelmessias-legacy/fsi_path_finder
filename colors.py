import platform

blue, green, yellow, yellow_bg, red, reset = '', '', '', '', '', ''

if(platform.system() == "Linux"):
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    yellow_bg = '\033[47;1;33m'
    blue = '\033[34m'
    reset = '\033[0;0m'
