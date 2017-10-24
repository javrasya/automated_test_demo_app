# Training 1

In this training, it is aimed to create a test spec for a basic logging mechanism. It means, whenever somebody takes some actions such as clicking button, selecting an option from a dropbox. 
Every action should be logged. There is a user interface to take some actions and there is a REST web service to query on loggs. 

It is aimed to make sure that, loging mechanism is working properly.




## REST Endpoint

**Note:** Use `510` as application code. It is hardcoded.

```
http://zeynep.ahmetdal.org/training1/api/islem/uygulamaBazliDetaySorgu/?application_code=510&action_code=<actionCode>
```


## Should be Tested


* Go to http://zeynep.ahmetdal.org/

* Login with username: admin    password: 21haziran2014

* Click Training 1

* Take some listing actions and it will give you a action code

* Make request to the log query REST API with the url above and see everything is OK.

