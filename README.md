# Study Rooms Script

### Requirements
1. Need to be a student at Univeristy of Victoria or have a netlink account
2. An Amazon account which will act as a AWS account. This is not necessary as you could put it on any other type of service but I found this is to be the easiest path, and these instructions are done on an EC2 instantance.

### Instructions
- Download the "study-rooms.py" file.
- Login and create an EC2 instance on AWS. THE AMI needs to be an Ubuntu Server' (https://www.guru99.com/creating-amazon-ec2-instance.html)
- Transfer the "study-rooms.py" and the "install.sh" files to the instance:
    - scp -i path/to/key file/to/copy user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com:path/to/destination
- SSH into the newly created instance. (https://aws.amazon.com/blogs/compute/new-using-amazon-ec2-instance-connect-for-ssh-access-to-your-ec2-instances/)
- 
