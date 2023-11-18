# [EBS]
[Amazon Elastic Block Store (Amazon EBS) is a scalable block storage service provided by Amazon Web Services (AWS). It offers high-performance, persistent block-level storage volumes that can be attached to Amazon EC2 instances.]

## Key-terms
* Solid state drive (SSD) volumes
* Hard disk drive (HDD) volumes
* Previous generation volumes

## Opdracht
# Exercise 1:
- 1-Navigate to the EC2 menu.
- 2-Create a t2.micro Amazon Linux 2 machine with all the default settings.
- 3-Create a new EBS volume with the following requirements:
  - Volume type: General Purpose SSD (gp3)
  - Size: 1 GiB
  - Availability Zone: same as your EC2
- 4-Wait for its state to be available.
# Exercise 2:
- 1-Attach your new EBS volume to your EC2 instance.
- 2-Connect to your EC2 instance using SSH.
- 3-Mount the EBS volume on your instance.
- 4-Create a text file and write it to the mounted EBS volume.
# Exercise 3:
- 1-Create a snapshot of your EBS volume.
- 2-Remove the text file from your original EBS volume.
- 3-Create a new volume using your snapshot.
- 4-Detach your original EBS volume.
- 5-Attach the new volume to your EC2 and mount it.
- 6-Find your text file on the new EBS volume.
### Gebruikte bronnen
[https://www.youtube.com/watch?v=VnO3Lz7Qr0U]
[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html]

### Ervaren problemen
[geen]

### Resultaat
[gelukt]
![EC2](/techgrounds-ZuhairBatha-main/techgrounds-ZuhairBatha/00_includes/AWS%201/AWS1-8.1.png)
![volume](../00_includes/AWS%201/AWS1-8.2.png)
![Attach](.././00_includes/AWS%201/AWS1-8.3.png)
![Mount](../00_includes/AWS%201/AWS1-8.4.png)
![Attached](.././00_includes/AWS%201/AWS1-8.5.png)
![Createfile](../00_includes/AWS%201/AWS1-8.6.png)
![snapshot](../00_includes/AWS%201/AWS1-8.7.png)
![Removefile](.././00_includes/AWS%201/AWS1-8.8.png)
![newvolume](../00_includes/AWS%201/AWS1-8.9.png)
