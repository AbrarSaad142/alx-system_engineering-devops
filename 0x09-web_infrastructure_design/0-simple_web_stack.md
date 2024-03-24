![alt text](https://i.postimg.cc/zvzGp18x/Untitled-1.jpg)

### What is a server ?

This is a piece of computer hardware or software that provides functionality for other programs or devices.

### What is the role of the domain name ?

The domain name enables users to access websites, without having to know the associated IP addresses of the websites.

### What type of DNS record www is in www.foobar.com ?

Www is a CNAME (Canonical Name) DNS record -type in www.foobar.com since it also points to the same IP address as foobar.com and if the IP address changes we can only record changes in the DNS A record of foobar.com.

### What is the role of the web server ?

To accept requests made by the browser through HTTP, process the request by responding with HTML content.

### What is the role of the application server ?

To act as a host for the user’s business logic while facilitating access to and performance of the business application.

### What is the role of the database ?

To allow the management,creation,updating, and retrieval of records.the database also gives structure to business information.

### What is the server using to communicate with the computer of the user requesting the website ?

Communication between the client and the server occurs over the internet network through the TCP/IP protocol suite

## The issues are with this infrastructure:

### SPOF

Single Point Of Failure is a part of the system that, if it fails the whole entire system stops from working.
The above infrastructure has no redundancy that can help in avoiding SPOFs,any single failure in any part of the system will cause all the system to stop.

### Downtime when maintenance needed (like deploying new code web server needs to be restarted)

Downtime will occur because we only have one server and one database , that is used to make the deployment and maintenance hence no way users will access the website in that period.

### Cannot scale if too much incoming traffic

Can not scale if there is too much incoming traffic because no second server in the system shares loads and the system will be overloaded.
