# [EC2]
[Amazon Elastic Compute Cloud (Amazon EC2) is a web service provided by Amazon Web Services (AWS) that allows users to rent virtual servers, known as instances]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
# Exercise 1
- 1-Navigate to the EC2 menu.
- 2-Launch an EC2 instance with the following requirements:
  - AMI: Amazon Linux 2 AMI (HVM), SSD Volume Type
  - Instance type: t2.micro
  - Default network, no preference for subnet
  - Termination protection: enabled
  - User data:
#!/bin/bash
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<h1>Hello From Your Web Server!</h1>' > /var/www/html/index.html
- 3-Root volume: general purpose SSD, Size: 8 GiB
- 4-New Security Group:
  - Name: Web server SG
  - Rules: Allow SSH, HTTP and HTTPS from anywhere
 # Exercise 2
- 1-Wait for the Status Checks to get out of the initialization stage. When you click the Status Checks tab, you should see that the System reachability and the Instance reachability checks have passed.
- 2-Log in to your EC2 instance using an ssh connection.
- 3-Terminate your instance.
### Gebruikte bronnen
[https://www.youtube.com/watch?v=0Gz-PUnEUF0]

### Ervaren problemen
[geen]

### Resultaat
[gelukt]
![EC2](../00_includes/AWS%201/AWS1-6.1.png)
![webserver](.././00_includes/AWS%201/AWS1-6.2.png)
![ssh](../00_includes/AWS%201/AWS1-6.3.png)
![Terminate](.././00_includes/AWS%201/AWS1-6.4.png)
