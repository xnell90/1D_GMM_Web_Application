# 1D Gaussian Mixture Model Web Application

This is the source code for the simple web application that clusters a set of points on the real number line using gaussian mixture models.

## Running The Web Application

Simply run this command *docker build . -t 1d-gmm-app* to create the *1d-gmm-app* image. Next, run this command to create a container from the *1d-gmm-app* image: *docker run -p 8000:8000 1d-gmm-app*. Then finally, open the provided link at the terminal: either http://0.0.0.0:8000 or http://127.0.0.1:8000.