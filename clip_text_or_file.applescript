tell application "System Events"
    set activeApp to name of first application process whose frontmost is true
    if "Finder" is in activeApp then
        do shell script "echo $(osascript -l JavaScript -e \"decodeURI(Application('Finder').selection()[0].url()).replace(/^file[:]\\/\\//, '')\")"
    else
        do shell script "pbpaste > ~/.clipbox/clip.txt && echo ~/.clipbox/clip.txt"
    end if
end tell
