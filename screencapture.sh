if [[ $1 == "selection" ]]
	then
		screencapture -i ~/.clipbox/capture.png && echo ~/.clipbox/capture.png
elif [[ $1 == "clipboard" ]]
	then
		osascript clip_text_or_file.applescript
elif [[ $1 == "recording" ]]
	then
		osascript screen_recording.applescript && /usr/local/bin/ffmpeg -y -i ~/.clipbox/recording.mov -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis ~/.clipbox/recording.webm && echo ~/.clipbox/recording.webm
fi
