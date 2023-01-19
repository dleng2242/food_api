
# Meal Suggestion API

Demo API that returns a meal suggestion given a type of food, e.g. "stew". 

The main aim of this repo is to build a REST API in python with Flask.


A REST API allows other programs to interface in a structured way. 
REST stands for representable state transfer. API stands for application
interface. Often they are used to retrieve or update information stored
in a database behind another application, but here the data is just stored
in memory for now. 


## Quick Start

You can request a meal idea using the following format
`<base url>/food/<food type>/<number>`.
The number argument is optional, defaulting to returning one item. 
Putting the number 0 will return all food items of that food type.

For example, you could run:
* `requests.get(BASE + "/food/stew")` - to get one stew suggestion
* `requests.get(BASE + "/food/stew/2")` - to get two stew suggestions
* `requests.get(BASE + "/food/stew/0")` - to see all available stews in the data

You can also add or delete data:
* `requests.put(BASE + "/food/stew", data={"food_item": "lentil stew"})`
* `requests.delete(BASE + "/food/stew", data={"food_item": "lentil stew"})`

Check out the `tests/test.py` file for more examples. 


## Steps to deploy

This was deployed using Azure Functions.

You can clone and run locally if desired. Create a virtual environment 
and install the packages from the requirements.txt and follow the below
steps up to the Azure stuff. 


* Install azure functions Core Tools 
* Install `azure-functions` to the conda environment (should already be in requirements.txt)
* Run `func init` within the conda environment in the project folder
* Check the http routePrefix extension is in the `host.json`
* Check you have get, put, delete, and/or post in the methods defined in `functions.json`
* Run `func start` to first run locally
* Sign into Azure in VS Code
* Create the functions app from VS Code as in the docs below
    * Select the options in the drop down as you go
    * Some are already defined in the functions.json
* Deploy to Azure (cloud with up arrow icon)
* Select subscription, and the the functions app you just made
* Once deployed try it out, the URL is in this form:
    * `http://<FunctionAppName>.azurewebsites.net/food/soup`
* Look at the Application Insights for live metrics, logs, usage, etc. 


## Notes

The Dockerfile works but wasn't needed for deployment. 

To build the docker image, first install Docker, and then run
`docker build -t flask_docker .`. The `-t` means tag and specifies
the "name:tag" of the image to build.
You can then run the container using 
`docker run -d -p 5000:5000 flask_docker`. The `-d` means development,
and the `-p` is used to define the ports. 


## Resources

* [Tech with Tim REST API video](https://www.youtube.com/watch?v=GMppyAPbLYk)
* [Developing RESTful APIs with Python and Flask](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
* [Azure Functions docs](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash)
* [Sample Flask app in Azure Functions](https://learn.microsoft.com/en-us/samples/azure-samples/flask-app-on-azure-functions/azure-functions-python-create-flask-app/)
* [Using Flask on Azure](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Cpython%2Cportal%2Cbash#start)
* [Create a function in Azure with python](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration)


