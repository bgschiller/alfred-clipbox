if [[ $1 == "selection" ]]
	then
		screencapture -i ~/.clipbox/capture.png && echo ~/.clipbox/capture.png
elif [[ $1 == "clipboard" ]]
	then
		osascript clip_text_or_file.applescript
elif [[ $1 == "recording" ]]
	then
		osascript screen_recording.applescript && ffmpeg -y -i ~/.clipbox/recording.mov -c copy -map 0 -movflags +faststart ~/.clipbox/recording.mp4 && echo ~/.clipbox/recording.mp4
fi
