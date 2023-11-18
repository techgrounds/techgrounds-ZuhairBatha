# [pvc]
[A virtual private cloud (VPC) is a secure, isolated private cloud hosted within a public cloud. VPC customers can run code, store data, host websites, and do anything else they could do in an ordinary private cloud, but the private cloud is hosted remotely by a public cloud provider.]

## Key-terms
[pvc, public and a private subnet, Ip, ]

## Opdracht
# Exercise 1
- 1-Allocate an Elastic IP address to your account.
- 2-Create a new VPC with the following requirements:
  - Region: Frankfurt (eu-central-1)
  - VPC with a public and a private subnet
  - Name: Lab VPC
  - CIDR: 10.0.0.0/16
- 3-Requirements for the public subnet:
  - Name: Public subnet 1
  - CIDR: 10.0.0.0/24
  - AZ: eu-central-1a
- 2-Requirements for the private subnet:
  - Name: Private subnet 1
  - CIDR: 10.0.1.0/24
  - AZ: eu-central-1a
# Exercise 2
- 1-Create an additional public subnet with the following requirements:
  - VPC: Lab VPC
  - Name: Public Subnet 2
  - AZ: eu-central-1b
  - CIDR: 10.0.2.0/24
- 2-Create an additional private subnet with the following requirements:
  - VPC: Lab VPC
  - Name: Private Subnet 2
  - AZ: eu-central-1b
  - CIDR: 10.0.3.0/24
- 3-View the main route table for Lab VPC. It should have an entry for the NAT gateway. Rename this route table to Private Route Table.
- 4-Explicitly associate the private route table with your two private subnets.
- 5-View the other route table for Lab VPC. It should have an entry for the internet gateway. Rename this route table to Public Route Table.
- 6-Explicitly associate the public route table to your two public subnets.
# Exercise 3
- 1-Create a Security Group with the following requirements:
  - Name: Web SG
  - Description: Enable HTTP Access
  - VPC: Lab VPC
  - Inbound rule: allow HTTP access from anywhere
  - Outbound rule: Allow all traffic
# Exercise 4:
- 1-Launch an EC2 instance with the following requirements:
  - AMI: Amazon Linux 2
  - Type: t3.micro
  - Subnet: Public subnet 2
  - Auto-assign Public IP: Enable
  - User data:
  #!/bin/bash
  #Install Apache Web Server and PHP
  yum install -y httpd mysql php unzip
  #Download Lab files
  wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/ 80-lab-vpc-web-server/lab-app.zip
  unzip lab-app.zip -d /var/www/html/
  #Turn on web server
  chkconfig httpd on
  service httpd start
- 2-Tag:
  - Key: Name
  - Value: Web server
  - Security Group: Web SG
  - Key pair: no key pair
- 3-Connect to your server using the public IPv4 DNS name.
### Gebruikte bronnen
[https://www.youtube.com/watch?v=gUesnoDzNr4]

### Ervaren problemen
[geen]

### Resultaat
[gelukt.]
![IP](/techgrounds-ZuhairBatha-main/techgrounds-ZuhairBatha/00_includes/AWS%201/wes1-10.1.png)
![VPC](../00_includes/AWS%201/wes1-10.2.png)
![table](.././00_includes/AWS%201/wes1-10.3.png)
![newsubnet](../00_includes/AWS%201/wes1-10.4.png)
![routetable](.././00_includes/AWS%201/wes1-10.5.png)
![rename](../00_includes/AWS%201/wes1-10.6.png)
![associate](.././00_includes/AWS%201/wes1-10.7.png)
![associateroutetable](../00_includes/AWS%201/wes1-10.8.png)
![publicroutetable](.././00_includes/AWS%201/wes1-10.9.png)
![publicassociate](../00_includes/AWS%201/wes1-10.10.png)
![publicassociateoutetable](.././00_includes/AWS%201/wes1-10.11.png)
![SecurityGroup](../00_includes/AWS%201/wes1-10.12.png)
![webserver](.././00_includes/AWS%201/wes1-10.13.png)
![Connecttoyourserver](../00_includes/AWS%201/wes1-10.14.png)
![table2](.././00_includes/AWS%201/wes1-10.15.png)