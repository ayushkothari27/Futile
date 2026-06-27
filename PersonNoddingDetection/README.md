# Person-Nodding-Counter

This is a very naive approach for head nod detection using the 68 Facial landmarks. The Facial landmarks are detected using dlib and openCV.
The average of the vertical displacement of these facial landmarks considering a gap of 5 frames is compared to the threshold value. 
The average of horizontal displacement is also taken into consideration so that it does not consider diagonal movement.

This is a very basic approach just for practising and may not yeild good results.
