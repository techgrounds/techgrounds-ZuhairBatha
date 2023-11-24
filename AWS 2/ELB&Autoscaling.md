# [ELB&Autoscaling]
*  Load Balancer is a service that automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, in multiple Availability Zones. This improves the availability and fault tolerance of your applications.
* Auto Scaling service that allows you to automatically adjust the number of instances in your application based on demand or a defined schedule. It helps ensure that you have the right amount of computing capacity to handle varying workloads while maintaining high availability. 
## Key-terms
 - 1 Load Balancer
 - 2 Auto Scaling 
## Opdracht
# Exercise 1
- 1-Launch an EC2 instance with the following requirements:
  - Region: Frankfurt (eu-central-1)
  - AMI: Amazon Linux 2
  - Type: t3.micro
  - User data:
    #!/bin/bash
    #Install Apache Web Server and PHP
    yum install -y httpd mysql php unzip
    #Download Lab files
    wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
    unzip lab-app.zip -d /var/www/html/
    #Turn on web server
    chkconfig httpd on
    service httpd start
- 2-Security Group: Allow HTTP
- 3-Wait for the status checks to pass.
- 4-Create an AMI from your instance with the following requirements:
  - Image name: Web server AMI
 # Exercise 2
- 1-Create an application load balancer with the following requirements:
  - Name: LabELB
  - Listener: HTTP on port 80
  - AZs: eu-central-1a and eu-central-1b
  - Subnets: must be public
  - Security Group:
  - Name: ELB SG
  - Rules: allow HTTP access
  - Target Group:
  - Name: LabTargetGroup
  - Targets: to be registered by Auto Scaling
 # Exercise 3
- 1-Create a launch configuration for the Auto Scaling group. It has to be identical to the server that is currently running.
- 1-Create an auto scaling group with the following requirements:
  - Name: Lab ASG
  - Launch Configuration: Web server launch configuration
  - Subnets: must be in eu-central-1a and eu-central-1b
  - Load Balancer: LabELB
  - Group metrics collection in CloudWatch must be enabled
  - Group Size:
  - Desired Capacity: 2
  - Minimum Capacity: 2
  - Maximum Capacity: 4
  - Scaling policy: Target tracking with a target of 60% average CPU utilisation
 # Exercise 4
- 1-Verify that the EC2 instances are online and that they are part of the target group for the load balancer.
- 2-Access the server via the ELB by using the DNS name of the ELB.
- 3-Perform a load test on your server(s) using the website on your server to activate auto scaling. There might be a delay on the creation of new servers in your fleet, depending on the settings on your Auto Scaling Group.
### Gebruikte bronnen
[https://www.youtube.com/watch?v=rw3Bcky0tSE]
[https://www.youtube.com/watch?v=TN_uNnZdF7g]

### Ervaren problemen
[geen]

### Resultaat
[gelukt]
![instance](/techgrounds-ZuhairBatha-main/techgrounds-ZuhairBatha/00_includes/AWS%202/AWS2-1.1.png)
![AMI](../00_includes/AWS%202/AWS2-1.2.png)
![ELB](.././00_includes/AWS%202/AWS2-1.3.png)
![applicationload](../00_includes/AWS%202/AWS2-1.4.png)
![templates](.././00_includes/AWS%202/AWS2-1.5.png)
![targetgroups](../00_includes/AWS%202/AWS2-1.6.png)
![Autoscailing](.././00_includes/AWS%202/AWS2-1.7.png)
![Autoscailing2](../00_includes/AWS%202/AWS2-1.8.png)
![Autoscailing3](.././00_includes/AWS%202/AWS2-1.9.png)
![Autoscailing4](../00_includes/AWS%202/AWS2-1.10.png)
![successful](.././00_includes/AWS%202/AWS2-1.11.png)
![healthy](../00_includes/AWS%202/AWS2-1.12.png)
![AccessDNS1](../00_includes/AWS%202/AWS2-1.13.png)
![AccessDNS2](.././00_includes/AWS%202/AWS2-1.14.png)
