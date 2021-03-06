# scratch
Create and Deploy an API
This is the technical test for Scratchpay. Please do this on a public git repo of your choice and share it with your Scratchpay hiring contact.
The technical test will test your skills in accordance with what Scratchpay is looking for, so please treat it accordingly.

Step 1: API
This section is to verify your competency in writing code.
You will find a swagger spec defining an API that you must create. It is a simple user system with a single endpoint. Please use the specification and write an API in the language of your choosing. Keep in mind that you will need to store the user information.

Step 2: Local Setup
This step is to verify your competency in setting up a development workflow.
Create a local environment that can be used to verify the code. Please keep in mind that a large number of projects are done with various setups (Unix and Windows based), so on any local setup please take into consideration this limitation (i.e. make sure it works across platforms). There is a CSV file containing data that should be loaded in order to test your setup. Please think of a creative way to make loading the data easier.

Step 3: Containerization and Orchestration
This step is to test your understanding of containerization, automation and orchestration.
Please containerize your application and create the required manifests/configuration to deploy your application to a Kubernetes cluster. Please use best practices when setting this up (treat it as if it were going into production). Part of the process should include the automation of loading the data into the storage that you have chosen.
NB: Scratchpay is a Fintech company, so while we believe in innovation, this should not be at the cost of compromising on security.

**Local Setup**

Docker
To run the app locally on you machine, Kindly install docker and docker-compose.
in the docker-compose.yaml, run 'docker-compose up'

To build the docker image and push to the docker registry

in the app.Dockerfile and postgres.Dockerfile, run 'docker build -t app.Dockerfile .' and 'docker build -t postgres.Dockerfile .' 
                        or 
run ./dockerize.sh

**TO develop
Windows**
Please make sure you have python3 or py installed and in your PATH in the root of the code directory,

python3 -m pip install virtualenv
py -m venv env
.\env\Scripts\activate
pip install -r requirements.txt

**Linux/macOS**
Please make sure you have python3 or py installed and in your PATH in the root of the code directory,

python3 -m pip install virtualenv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

