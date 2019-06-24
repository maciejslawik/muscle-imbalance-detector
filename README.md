# Muscle Imbalance Detector #

This Python3 application is a proof of concept of an app detecting muscle imbalances
in athletes during strength training. 

It uses a camera to capture frames of athlete's movement and processes the frames by
keypoints on the athlete's body.

## Technologies used ##

* Python 3
* OpenCV
* OpenPose

## Instalation

1. Run
    ```
    make install
    ```
2. Run

    ```
    make build
    ```
    
## Usage ##

To run the app use
```
python3 muscle-imbalance-detector.py
```

The app allows you to specify the capture time before starting the movement. After
pressing start you will have 10 seconds to prepare for the movement. You will hear
a beep every 1 second. Start the movement after you hear a double beep. You will hear
another double beep when capturing process finishes. 

Wait for a report.

## Screenshots  ##

![Alt text](docs/app.png?raw=true "App window")

### Clean & Push Jerk ###

![Alt text](docs/clean/2.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/3.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/4.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/5.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/6.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/7.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/8.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/9.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/10.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/11.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/12.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/13.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/14.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/15.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/16.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/17.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/18.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/19.jpg?raw=true "Clean & Push Jerk")
![Alt text](docs/clean/20.jpg?raw=true "Clean & Push Jerk")

### Snatch ###

![Alt text](docs/snatch/4.jpg?raw=true "Snatch")
![Alt text](docs/snatch/5.jpg?raw=true "Snatch")
![Alt text](docs/snatch/6.jpg?raw=true "Snatch")
![Alt text](docs/snatch/7.jpg?raw=true "Snatch")
![Alt text](docs/snatch/8.jpg?raw=true "Snatch")
![Alt text](docs/snatch/9.jpg?raw=true "Snatch")
![Alt text](docs/snatch/10.jpg?raw=true "Snatch")
![Alt text](docs/snatch/11.jpg?raw=true "Snatch")
![Alt text](docs/snatch/12.jpg?raw=true "Snatch")
![Alt text](docs/snatch/13.jpg?raw=true "Snatch")