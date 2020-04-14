## COVID-19 Impact Estimator

### Tools used in the Challenge
* [Python](https://docs.python.org/3/) - The language used
* [Flask](http://flask.pocoo.org/) - Web framework to develop REST API
* [Pylint](https://www.pylint.org/) - Linting Library
* [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
* [Postman](https://www.postman.com/) - For Testing API endpoint

### Getting Started
* `git clone https://github.com/Levy-Naibei/covid19-impact-estimator.git`
* `cd covid19-impact-estimator`
* Create and activate virtual environment by `source (your virtual env)/bin/activate` on MAC/Linux 
  and `source (your virtual env)/Scripts/activate` on Windows
* Run `pip install -r requirements.txt`
* Run `python run.py` to start the server
* On Postman address bar put `localhost:5000/api/v1/on-covid-19` to consume the API
* Add input data in the body and send POST resquest
* Terminate the request url with `/json` or `/xml` and send POST request
* Terminate the request url with `/logs` and send GET request

### Heroku App
* https://covid-19-infections-estimator.herokuapp.com/

### Endpoints

|       Endpoint                             |               FUNCTIONALITY                             |
| ----------------------------------------   |:-------------------------------------------------------:|
| POST &emsp;&emsp;/api/v1/on-covid-19       | This will take input data and return estimation in json |
| POST &emsp;&emsp;/api/v1/on-covid-19/json  | This will take input data and return estimation in json |
| POST &emsp;&emsp;/api/v1/on-covid-19/xml   | This will take input data and return estimation in xml  |
| GET  &emsp;&emsp;/api/v1/on-covid-19/logs  | This will return runtime logs                           | 


### Authors
* **Levy Naibei** 

---
This app built with python is meant to help society and leaders prepare for the **real big problem** of COVID-19, which is **its impact on lives, health systems, supply chains, and the economy**: 
> 1.  Too many patients, not enough hospitals and beds. A serious shortage of ventilators, masks and other PPE - if *we don’t practice social distancing*.
> 2.  Job losses or freezes, low cash flow and low production (even for essentials like food). These and more from too many people being sick, a sizable number dying (including some of the best people in many fields), and many others affected by the impact of losing loved ones or a world operating in slow motion
---

