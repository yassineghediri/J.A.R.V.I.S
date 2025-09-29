import os
from groq import Groq  



# Applications List

applications = {
    "Browser": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
    "Firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
    "Chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "Edge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "Opera": "C:\\Program Files\\Opera\\launcher.exe",

    "Word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "Excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    "PowerPoint": "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    "Notepad": "C:\\Windows\\system32\\notepad.exe",
    "Calculator": "C:\\Windows\\system32\\calc.exe",
    "Paint": "C:\\Windows\\system32\\mspaint.exe",
    "Snipping Tool": "C:\\Windows\\system32\\SnippingTool.exe",
    "WordPad": "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe",

    "Spotify": "C:\\Users\\%USERNAME%\\AppData\\Roaming\\Spotify\\Spotify.exe",
    "VLC": "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
    "Movies": "C:\\Program Files\\WindowsApps\\Microsoft.ZuneVideo_8wekyb3d8bbwe\\Video.UI.exe",
    "Windows Media Player": "C:\\Program Files\\Windows Media Player\\wmplayer.exe",

    "Command Prompt": "C:\\Windows\\system32\\cmd.exe",
    "PowerShell": "C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
    "Task Manager": "C:\\Windows\\system32\\Taskmgr.exe",
    "File Explorer": "C:\\Windows\\explorer.exe",
    "Registry Editor": "C:\\Windows\\regedit.exe",
    "Control Panel": "C:\\Windows\\system32\\control.exe",

    "Teams": "C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart \"Teams.exe\"",
    "Zoom": "C:\\Users\\%USERNAME%\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe",
    "Discord": "C:\\Users\\%USERNAME%\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    "Skype": "C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe",
    "Slack": "C:\\Users\\%USERNAME%\\AppData\\Local\\slack\\slack.exe"
}

# API Keys
weather_key = os.environ.get("WEATHER_SECRET")
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
pushbullet_secret = os.environ.get("PUSHBULLET_SECRET")