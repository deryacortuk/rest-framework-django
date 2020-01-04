## What is REST?
REST means [Representational state transfer](http://en.wikipedia.org/wiki/Representational_state_transfer) which essentially refers to a style of web architecture that has many underlying characteristics and governs the behavior of clients and servers. REST APIs are based on URIs (uniform resource identifier) and the HTTP protocol. REST APIs can exchange data in either JSON or XML format, although many REST APIs send data as JSON.
REST API allows you to interact with Parse from anything that can send an HTTP request. See [Parse REST Definition](https://www.parse.com/docs/rest) for examples of this.

REST technology is generally preferred to the more robust Simple Object Access Protocol (SOAP) technology because REST leverages less [bandwidth](https://searchnetworking.techtarget.com/definition/bandwidth), making it more suitable for internet usage. An API for a website is [code](https://whatis.techtarget.com/definition/code) that allows two software programs to communicate with each another . The API spells out the proper way for a developer to write a program requesting services from an operating system or other application.
## Guiding Principles of REST

-   **Stateless**  
    This means that there is no necessary session is held between a client and server. Data received from the server can be used by the client independently. This allows for short, discrete operations, and even offline caching of data. This makes REST a natural fit for HTTP operations in which requests are intended to be singular and short-lived.
- **Client-Server** 
There should be a clear delineation between the client and server. UI and request-gathering concerns are the client’s domain. Data access, workload management and security are the server’s domain. This loose coupling of the client and server enables each to be developed and enhanced independent of the other.
-  **Uniform Interface**  
    REST APIs are meant to be self-describing, uniform in their definition, and each operation separated by a different endpoint or URL. In practical terms, most REST APIs implement classic CRUD (Create, Read, Update, Delete) operations against a data model. This uniformity allows developers to easily learn the usage pattern of each API.
    
  - **Cacheable**
Data and responses need to be cached to improve the performance of the app on the client’s side. It also improves the scalability of the server since caching reduces the load. Caching can be done on either the server side or the client side.

- **Layered system** 
The layered system style allows an architecture to be composed of hierarchical layers by constraining component behavior such that each component cannot “see” beyond the immediate layer with which they are interacting.

## The Makings Of A Request

There are four major components of a request:  

1.  **The Endpoint** – The endpoint is the URL that you are requesting. It’s structure includes the root-endpoint, the path (which determines the resource you’re requesting for), and the query parameters.
2.  **The Method** – The method refers to what action you want to take, whether it’s just looking at the resource, updating the resource, replacing the resource, or deleting the resource.
3.  **The Headers** – The headers can be used for several purposes, including providing a summary about the body content or providing authentication. Headers provide information to both the server and the client.
4.  **The Data** – The data refers to the information you want to send to the server. It’s only used if you’re altering or deleting the resource.

## Classes – HTTP Status Codes[](https://kinsta.com/blog/http-status-codes/#classes--http-status-codes)

The list of HTTP status codes are divided into 5 classes:

-   **100’s**: Informational codes indicating that the request initiated by the browser is continuing.
-   **200’s**: Success codes returned when browser request was successfully received, understood, and processed by the server.
-   **300’s**: Redirection codes returned when a new resource has been substituted for the requested resource.
-   **400’s**: Client error codes indicating that there was a  [problem with the request](https://kinsta.com/knowledgebase/400-bad-request/).
-   **500’s**: Server error codes indicating that the request was accepted, but that an error on the server prevented the fulfillment of the request.

## List of HTTP Status Codes[](https://kinsta.com/blog/http-status-codes/#list-of-http-status-codes)

There are  over 40 different server status codes. However, there are really fewer than a dozen that you’ll run into on a regular basis. If you’re running a website, get a good handle on these codes and you’ll understand what you’re up against the vast majority of times that a HTTP status code rears it’s head. Check out the list of HTTP status codes below:

### 200 Status Code

-   **200: “Everything is OK.”**  This is the code that is delivered when a web page or resource acts exactly the way it’s expected to.

### 300 Status Codes

-   **301: “The requested resource has been moved permanently.”**  This code is delivered when a web page or resource has been permanently replaced with a different resource. 
-   **302: “The requested resource has moved, but was found.”**  This code is used to indicate that the requested resource was found, just not at the location where it was expected. It is used for temporary URL redirection.
-   **304: “The requested resource has not been modified since the last time you accessed it.”**  This code tells the browser that resources stored in the browser cache haven’t changed. It’s used to speed up web page delivery by reusing previously downloaded resources.

### 400 Status Codes

-   **401: “Unauthorized”** or **“Authorization Required.”** This is returned by the server when the target resource lacks valid authentication credentials. 

**

## Django REST Framework

[Django REST framework](https://www.django-rest-framework.org/)  is a open source, mature and well supported Python/Django library that aims at building sophisticated web APIs. It is flexible and fully-featured toolkit with modular and customizable architecture that makes possible development of both simple, turn-key API endpoints and complicated REST constructs.

Main advantages of Django REST framework:

-   Simplicity, flexibility, quality, and test coverage of source code.
-   Powerful serialization engine compatible with both ORM and non-ORM data sources.
-   Pluggable and easy to customise emitters, parsers, validators and authenticators.
-   Generic classes for CRUD operations.
-   Clean, simple, views for Resources, using Django's new class based views.
-   Support for ModelResources with out-of-the-box default implementations and input validation (optional support for forms as input validation).
-   HTTP response handling, content type negotiation using HTTP Accept headers.
-   Pagination simplifies the process of returning paginated data in a way that can then be rendered to arbitrary media types.
-   Publishing of metadata along with query sets.
-   Permission classes and throttling management 
