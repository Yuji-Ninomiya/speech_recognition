# speech_recognition
This is the research at University of Salento 2017.

1. Install ROS packages

if there is no directory, at first you have to make that:see http://wiki.ros.org/catkin/Tutorials/create_a_workspace

2. In your Catkin workspace, install the package with the following commands.

```bash
student@vaio:~$ cd ~/catkin_ws/src
student@vaio:~$ git clone https://github.com/Yuji-Ninomiya/speech_recognition.git speech_recognition
student@vaio:~$ rosmake speech_recognition
student@vaio:~$ cd .. && catkin_make
```
```bash
student@vaio:~$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
student@vaio:~$ source ~/.bashrc
```

3. Also you have to install the package:  rwt_speech_recognition packages:  see
https://github.com/tork-a/visualization_rwt/tree/hydro-devel/rwt_speech_recognition (It should be installed the same directoly you made that named 'catkin_ws').

	You need to make the following changes to files in this package to use Italian recognition.

```bash
Add file "it-IT.json" to "visualization_rwt/rwt_speech_recognition/www/locale". Please move to there from my repositoly named "speech_recognition/www/locale".

Change the file "visualization_rwt/rwt_speech_recognition/www/i18n.js", line.26
	var lang = l || 'jp-JP';  ===>  var lang = l || 'it-IT';

Add sentence to "index.html" in "visualization_rwt/rwt_speech_recognition/www/", line 28
	<li data-value="it-IT"><a href="#">Italian</a></li>


change the file "visualization_rwt/rwt_speech_recognition/www/rwt_speech_recognition.js", line 46
	speech_recog.lang = 'ja-JP';  ===>  speech_recog.lang = 'it-IT';
```

### How to use

1. Open terminal and separate that.
2. Connect to the robot with bluetooth. Please refer to here:https://github.com/TakakiNishio/al5d/tree/master/src/python
3. On each terminals, type these commands.

```bash
roscore
roslaunch rwt_speech_recognition speech_recognition.launch
rosrun speech_recognition ss_recognition.py
rosrun speech_recognition simple_movement.py
```
