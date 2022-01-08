# Raspberry pi V2 Camera Test
## Hardware
1. Raspberry pi 3 model B
2. Raspberry pi Camera v2

## 1. Testing out the camera module
```bash
$ raspistill -o images/output.jpg
```
## 2. Clone the repository
```bash
$ git clone git@github.com:DanNduati/raspberry_pi_camera_tests.git 
```
## 3. Create python virtual environment and activate it
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```
## Install opencv
To make opencv installation less hectic i've create a bashscript that automates this so just run the script to install
```bash
$ chmod +x cv_install.sh
$ ./cv_install.sh
```

## Sample photos
<img src="images/image.jpg"></img>
<img src="images/output.jpg"></img>
