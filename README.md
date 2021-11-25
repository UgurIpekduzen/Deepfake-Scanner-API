# Deepfake-Scanner-API

## Installation
Make sure you have a nvidia gpu with cuda support. Scanner can run both on Windows and Linux.

### On Linux
+ Clone the repo or download it as a zip and extract to a directory.
+ Download the [pre-trained model](https://download.deepware.ai/weights.zip) pre-trained model and place it in the weights directory.

### Docker
+ Make sure you installed Docker Engine on your device. If you don't have it, you can make the installation by following the steps from [this page](https://docs.docker.com/engine/install/ubuntu/).
+ After the installation, open your terminal and run those commands: 
  + `$ cd Deepfake-Scanner-API`
  + `$ docker build .`
  + `$ docker -p run 8000:8000 <container-id>`
  
