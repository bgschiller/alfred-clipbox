set x to (path to home folder as string) & ".clipbox:recording.mov"

tell application "QuickTime Player"
      activate
      set newScreenRecording to new screen recording
      my putInMenuBar()
      repeat while exists newScreenRecording
          delay 1
      end repeat
      -- the recording has stopped

      export document 1 in (file x) using settings preset "720p"
      close document 1 saving no
      quit
end tell

on putInMenuBar()
      delay 1
      tell application "System Events"
            tell process "QuickTime Player"
                  set frontmost to true
                  key code 49
            end tell
      end tell
end putInMenuBar
