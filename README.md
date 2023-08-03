# QL MLE Challenge

Here is my submission for the QL MLE Challenge. There have been some changes to *index.html*, and *static/sript.js*, so feel free to browse through those files and check the changes. Two additional files have been added to this directory, namely *.dockerignore* and *Dockerfile*, and they are for running the app on any environment (assuming docker is installed). Finally, *main.py* contains the backend API service that hosts the model, trains it, and returns the model parameters.


## Running The Web Application

Assuming that you are in the directory that contains the docker file, simply run this command *docker build . -t ql-mle-app* to create the *qle-mle-app* image. Next, run this command to create a container from the *qle-mle-app* image: *docker run -p 8000:8000 ql-mle-app*. Then finally, open the provided link at the terminal: either http://0.0.0.0:8000 or http://127.0.0.1:8000.

[Notes: the web application uses fastapi==0.100.0, and the most recent cpu version of pytorch (2.0.1)]