![alt text](https://i.postimg.cc/G2XRh0Ps/2-Secured-and-monitored-web-infrastructure.jpg)

## For every additional element, why you are adding it
A secure, encrypted, and monitored web infrastructure for the website www.foobar.com would typically consist of three servers: a load balancer, a web server, and a database server.

The load balancer would be responsible for distributing incoming traffic evenly across the web server and the database server, ensuring that the website can handle high levels of traffic without any downtime. The load balancer would also be responsible for encrypting traffic using Transport Layer Security (TLS) or Secure Sockets Layer (SSL), ensuring that all data transmitted between the user’s web browser and the website is secure and cannot be intercepted by third parties.

The web server would be responsible for hosting the website’s content and serving it to users who visit www.foobar.com. The web server would also be responsible for running any server-side scripts or applications that are needed to power the website, such as a content management system (CMS) or e-commerce platform.

The database server would be responsible for storing the website’s data, such as user information, product listings, and blog posts. The database server would also be responsible for providing the web server with the data it needs to generate dynamic web pages for the website.

To ensure that the web infrastructure is secure, it would be important to implement a number of security measures, such as firewalls, intrusion detection and prevention systems, and regular security updates and patches. It would also be important to regularly monitor the servers and the website to ensure that they are running smoothly and to identify and address any potential security vulnerabilities or performance issues.

## Firewall

A firewall is a security system designed to prevent unauthorized access to or from a private network. Firewalls can be hardware-based, software-based, or a combination of both. They are commonly used to protect corporate and home networks from external threats such as hackers, malware, and viruses. Firewalls use a set of rules to control incoming and outgoing network traffic and can be customized to fit the specific security needs of a network.

## Why is Traffic Served Over HTTPS?

HTTPS is a secure version of the HTTP protocol, which is the protocol used to transfer data over the web. When a website uses HTTPS, it means that all communication between the web server and the client’s web browser is encrypted and secure. This is important for a number of reasons, including protecting the privacy of users’ personal information and preventing attackers from intercepting and altering the data that is transmitted between the server and the client. Additionally, because HTTPS provides a secure connection, it helps to ensure the integrity of the data that is transmitted, which is important for ensuring that the information on a website is accurate and up-to-date.

## Monitoring

A monitoring tool is a type of software or hardware that is used to collect data about a system, network, or application. This data can be used to monitor the performance and health of the system, identify potential issues, and take corrective action as needed. Monitoring tools can provide valuable insights into the behavior and operation of a system, and can help ensure that it is running smoothly and efficiently. Some common types of monitoring tools include network monitoring tools, server monitoring tools, application performance monitoring tools, and website monitoring tools. These tools can be used to monitor a wide range of metrics, including availability, latency, throughput, error rates, and more.

## What to do to Monitor a Web Server’s QPS

If you want to monitor your web server’s QPS (queries per second), you can use a variety of tools to do so. Some popular tools for monitoring web server performance include:

1. Netdata: This is an open-source real-time performance monitoring tool that can be used to monitor a wide range of metrics, including QPS, on your web server.

2. Datadog: This is a cloud-based monitoring and analytics platform that can be used to monitor your web server’s performance, including QPS.

3. Prometheus: This is an open-source monitoring and alerting toolkit that can be used to monitor your web server’s QPS, as well as other metrics.

To use these tools, you will first need to install and configure them on your web server. Then, you can use their respective dashboards or APIs to monitor your web server’s QPS in real-time. You can also set up alerts to notify you if your web server’s QPS exceeds a certain threshold, so you can take action if necessary.

## Why Terminating SSL at the Load Balancer Level is an Issue

Terminating SSL at the load balancer level can cause a number of issues. For one, it can create a single point of failure, since all SSL traffic has to pass through the load balancer. This means that if the load balancer goes down, SSL traffic will no longer be able to pass through, potentially causing outages on your site. Additionally, terminating SSL at the load balancer level can create performance bottlenecks, since the load balancer now has to handle the additional processing required to encrypt and decrypt all SSL traffic. Finally, it can also make it more difficult to manage SSL certificates and keys, since they now all have to be managed centrally on the load balancer. For these reasons, many organizations prefer to terminate SSL at the web server level instead of the load balancer level.

## Why having only one MySQL server capable of accepting writes is an issue:

Having only one MySQL server that is capable of accepting writes can be problematic for a number of reasons. For one, it can create a single point of failure in your system. If that server goes down for any reason, your entire system will be unable to accept writes, which can cause significant disruption to your business. Additionally, having a single server that is responsible for accepting all writes can lead to performance bottlenecks, as the server may become overwhelmed by the volume of incoming write requests. This can cause your system to slow down or even crash. In order to avoid these problems, it is generally best to have multiple MySQL servers that are capable of accepting writes, so that your system is more resilient and can handle a higher volume of traffic.

## Why having servers with all the same components (database, web server and application server) might be a problem:

Having all the same components on multiple servers can lead to potential problems if one of those components experiences an issue or fails. If a server’s database, for example, goes down, it can take the rest of the system down with it. This can lead to decreased reliability and increased downtime for the system as a whole. It’s generally considered a best practice to have different servers for different components to increase reliability and reduce the impact of any potential issues. This way, if one server experiences an issue, it won’t take the entire system down with it.
