# Study Rooms Script

### Requirements
1. Need to be a student at Univeristy of Victoria or have a netlink account
2. An Amazon account which will act as a AWS account. This is not necessary as you could put it on any other type of service but I found this is to be the easiest path, and these instructions are done on an EC2 instantance.

### Instructions
- Download the "study-rooms.py" file.
- Login and create an EC2 instance on AWS. THE AMI needs to be an Ubuntu Server' (https://www.guru99.com/creating-amazon-ec2-instance.html)
- Transfer the "study-rooms.py" and the "install.sh" files to the instance:
    - scp -i path/to/key file/to/copy user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com:path/to/destination
- SSH into the newly created instance. Replace ec2-user with ubuntu. (https://aws.amazon.com/blogs/compute/new-using-amazon-ec2-instance-connect-for-ssh-access-to-your-ec2-instances/)
- Run install script './install.sh', this will install the packages needed for the script to run, chromium-browser, selenium, bs4, chrome web driver, and pip.
- Then open the bashrc file with 'vi .bashrc' and at the bottom add these three lines replacing the information with your credentials
    - export SRGROUP=*study group name*
    - export SRUSER=*netlink username*
    - export SRPASS=*netlink password*
