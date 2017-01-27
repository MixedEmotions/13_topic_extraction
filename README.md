Topic Extraction Service
========================

Classifies the given text within a set of concepts, retrieved using an unique
service id and a language.

Installation
------------

Python 3 is necessary to run the service. Required libraries are:
* tornado

Configuring the service
-----------------------

The service is provided with an example taxonomy, but it is designed for having the final user providing its own.

The taxonomy should be in a python file, such as taxonomy.py. The format there is a json map. Its keys are the phrases to tag. They will be tag with all the tags that are in the value array for that tag.

Example:

    taxonomy = {
     'gerente': ['DIRECTIVOS'],
     'competidores': ['COMPETENCIA'],
     'jefe': ['DIRECTIVOS'],
     'publicidad': ['IMAGEN_DE_MARCA'],
     'opinion online': ['IMAGEN_DE_MARCA', 'COMPETENCIA'],
     'competidoras': ['COMPETENCIA'],
    }


Starting and stopping the service
---------------------------------

There is a script that starts and stops the service with the desired configuration:

	./launcher.sh start
	./launcher.sh stop

This same script contains the configuration for running the service with a given
number of separated processes, using the port range as defined.

Calling the service
-------------------

This service admits both GET and POST requests.

### Calling the service via GET

An example call would be:

	http://[ip_address]:[port]/?text=La tarifa de movistar es muy mala&lang=es

This call returns a JSON array with the matched concepts for the given text, language
and service, or "N/A" if there is not any match. E.g.:

    [
      "DIRECTIVOS"
    ]

### Calling the service via POST

The service expects a body with a text per line.


The response is a JSON response with a line per entry in the request. E.g.:

    {
      "response": [
        {
          "topics": [],
          "text": "some jefe"
        },
        {
          "topics": [],
          "text": "nada por aquí"
        },
        {
          "topics": [
            "DIRECTIVOS"
          ],
          "text": "otro jefe"
        }
      ]
    }

Creating a Docker Image
-----------------------
For creating a docker image, just configure your own taxonomy.py and run:

    docker build -t {name} .

## Acknowledgement

This topic extraction module was developed by [Paradigma Digital](https://en.paradigmadigital.com/). This development has been partially funded by the European Union through the MixedEmotions Project (project number H2020 655632), as part of the `RIA ICT 15 Big data and Open Data Innovation and take-up` programme.

![MixedEmotions](https://raw.githubusercontent.com/MixedEmotions/MixedEmotions/master/img/me.png) 

![EU](https://raw.githubusercontent.com/MixedEmotions/MixedEmotions/master/img/H2020-Web.png)

 http://ec.europa.eu/research/participants/portal/desktop/en/opportunities/index.html
