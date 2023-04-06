# Subtitle Time Shifter
This project aims to facilitate subtitle adjustment in videos. Specifically, it allows subtitles to be moved backwards in time. This is useful when a movie is split into two parts and the subtitle timing needs to be adjusted to match the start of the second part of the video.

## Usage
To use this project, you can follow the steps below:

1. Install Python 3 if it's not already installed on your system.

2. Clone or download the project to your local machine.

3. Open a terminal or command prompt and navigate to the project directory.

4. Run the command **'python main.py'** followed by the arguments:

~~~
-H, --hour: number of hours to shift the subtitle times by
-M, --minute: number of minutes to shift the subtitle times by
-S, --second: number of seconds to shift the subtitle times by
-MS, --millisecond: number of milliseconds to shift the subtitle times by
~~~

For example, to shift the subtitle times by 1 hour and 30 minutes, 45 seconds, 354 milliseconds, you can run the command:

~~~
python main.py input.srt -H 1 -M 30 -S 45 -MS 354
~~~

5. The new subtitle file with adjusted times will be saved to the output file path specified.