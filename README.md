# Clipbox Alfred workflow

Take screenshots and video capture and upload to Trello. Put the link on your clipboard.

## Default Keybindings

| Keys            | Action                   |
| --------------- | ------------------------ |
| &#8984;&#8679;X | Take screenshot          |
| &#8984;&#8679;G | Begin screen recording   |
| &#8984;&#8679;C | Upload clipboard text    |

## Logging in to Trello

Run the `clipbox login` action to get an authorization token from clipbox:

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/58d49e6d363fb61d32be7235/ae1db9043ad8c4131f410ed71eef9ce4/capture.png)

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/58d499f720e1dc0d6cb1cb6e/1345cf7d17807334d760c0f7d6e9f736/capture.png)

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/58d49a68897f549b514f236e/c5ea99788d2e2c61008aee4888c7c48f/capture.png)

Now take the token and give it to the `clipbox authorize` action:

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/58d49a9b92bf98c9ee5aa2d0/1e0688bd337527ae8e157fb48e4b7c60/capture.png)

## Screen Recordings

Screen recordings will take a little while to encode, longer for long captures. They come out looking like this: [recording.webm](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/58d49c76940a4bc334c91549/ecf16e0820142d986acbb500eb20bd9d/recording.webm).

## Trello Board

All recordings are available on your Trello board:

![](https://trello-attachments.s3.amazonaws.com/58d428743111af1d0a20cf28/58d49d010cc52b13fe216a82/466b0cd6777c472705e13c29c9887078/capture.png)
