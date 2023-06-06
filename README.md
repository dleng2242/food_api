
# Meal Suggestion API

Demo API that returns a meal suggestion given a type of food, e.g. "stew". 

The main aim of this repo is to build a REST API in python with Flask.


A REST APIs allow other programs to interface in a structured way
and are very common. REST stands for representable state transfer.
REST APIs are the standard way to interact with another application, 
but here I just used to fetch data from my "app". 


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
steps up to signing into Azure. For me the base URL was 
`http://127.0.0.1:7071`. 


* Install azure functions Core Tools 
* Install `azure-functions` to the conda environment (should already be in requirements.txt)
* Run `func init` within the conda environment in the project folder
* Check the http routePrefix extension is in the `host.json`
* Check you have get, put, delete, and/or post in the methods defined in `functions.json`
* Run `func start` to first run locally
* Sign into Azure in VS Code
* Create the functions app from VS Code as in the docs below
    * Read [Quickstart: Create a function in Azure with Python using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration)
    * Select the options in the drop down as you go
    * The name then becomes part of your URL so choose carefully! 
    * Some are already defined in the functions.json
* Deploy to Azure (cloud with up arrow icon)
* Select subscription, and then the functions app you just made
* Once deployed try it out, the URL is in this form:
    * `http://<FunctionAppName>.azurewebsites.net/food/soup`
* Look at the Application Insights for live metrics, logs, usage, etc. 



## Notes

You could use Docker to deploy but wasn't needed here. It is left for 
interest or if you want to test it yourself. 

To build the docker image, first install Docker, and then run
`docker build -t flask_docker .`. The `-t` means tag and specifies
the "name:tag" of the image to build.
You can then run the container using 
`docker run -d -p 5000:5000 flask_docker`, where `-d` means detached,
and the `-p` is used to define the ports. During development
this was connecting the default flask port 5000 to 5000, but running
through the Azure Functions sdk you might need to change it to `-p 7071:7071`
or similar. You will need to change these if you were to deploy the app in 
a production environment. 


## Resources

* [Tech with Tim REST API video](https://www.youtube.com/watch?v=GMppyAPbLYk)
* [Developing RESTful APIs with Python and Flask](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
* [Azure Functions docs](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash)
* [Using Flask Framework with Azure Functions Sample](https://learn.microsoft.com/en-us/samples/azure-samples/flask-app-on-azure-functions/azure-functions-python-create-flask-app/)
* [Work with Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash)
* [Quickstart: Create a function in Azure with Python using Visual Studio Code](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration)


