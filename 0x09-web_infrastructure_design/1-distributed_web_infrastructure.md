![alt text](https://i.postimg.cc/0Q1fzznL/1-Distributed-web-infrastructure.jpg)

# Distributed web infrastructure

### For every additional element, why are you adding it ?

We added an additional server and 1 load balancer when traffic starts to grow, and I mean really GROW , when millions of users at once are making requests for websites like Google and Facebook, one web server won’t be able to handle all these corresponding requests, so we have to use two servers. A new problem arises - when a user makes a request, will the content come from webserver 1 or web server 2?
These types of websites have a Load Balancer.

### What distribution algorithm your load balancer is configured with and how it works ?

Round Robin (most common) — Requests are distributed across the group of servers sequentially. Request 1 is directed to server 1, request 2 to server 2, and so forth.
Least Connections — Before redirecting a request to a server, the Load Balancer computes which server has the least connections, and then sends the request to there.
IP Hash — The IP address of the client is used to determine which server the request will be directed to. For example, all IP addresses from 100.100.100.100–400.400.400.400 will be sent to server 3. (IP Hash load balancing uses an algorithm that takes the source and destination IP address of the client and server to generate a unique hash key. This key is used to allocate the client to a particular server. They are assigned individually as they connect to the server and once assigned a certain server, the Client will always connect to that particular server)

### Is your load-balancer enabling an Active-Active or Active-Passive setup, explaining the difference between both ?

In an active-passive configuration, the server load balancer recognizes a failed node and redirects traffic to the next available node. In an active-active configuration, the load balancer spreads out the workload’s traffic among multiple nodes.

### How does a database Primary-Replica (Master-Slave) cluster works ?

Master-slave replication enables data from one database server (the master) to be replicated to one or more other database servers (the slaves). The master logs the updates, which then ripple through to the slaves. If the changes are made to the master and slave at the same time, it is synchronous.

### What is the difference between the Primary node and the Replica node in regard to the application ?

The difference between the Primary node and the Replica node in regard to the application is that-, the primary node is regarded as the authoritative source, and the replica node (also known as slave) databases are synchronized to it(Master).

### what the issues are with this infrastructure ?

There are multiple SPOF (Single Point Of Failure).
For example, if the Primary MySQL database server is down, the entire site would be unable to make changes to the site (including adding or removing users). The server containing the load balancer and the application server connecting to the primary database server are also SPOFs.
Security issues.
The data transmitted over the network isn't encrypted using an SSL certificate so hackers can spy on the network. There is no way of blocking unauthorized IPs since there's no firewall installed on any server.
No monitoring.
We have no way of knowing the status of each server since they're not being monitored.
