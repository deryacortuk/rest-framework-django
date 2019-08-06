# rest framework-django
API Guide-Rest Framework

Serializers allow complex data such as querysets and model instances to be converted to native 
Python datatypes that can then be easily rendered into JSON, XML or other content types.
Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the
incoming data.

https://www.django-rest-framework.org/api-guide/serializers/

https://simpleisbetterthancomplex.com/tutorial/2019/04/07/how-to-save-extra-data-to-a-django-rest-framework-serializer.html

Throttling


Throttling is similar to permissions, in that it determines if a request should be authorized. Throttles indicate a temporary state,
and are used to control the rate of requests that clients can make to an API.



Signals

Django includes a “signal dispatcher” which helps allow decoupled applications get notified when actions occur elsewhere in the framework.
In a nutshell, signals allow certain senders to notify a set of receivers that some action has taken place. They’re especially useful when
many pieces of code may be interested in the same events.

https://docs.djangoproject.com/en/2.2/topics/signals/

