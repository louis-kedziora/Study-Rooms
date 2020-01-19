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
- Run install script './install.sh', this will install the packages needed for the script to run, chromium-browser, selenium, bs4, chrome web driver, and pip. Just input yes and y when needed.
- Then open the bashrc file with 'vi .bashrc' and at the bottom add these three lines replacing the information with your credentials:
    - export SRGROUP=*study group name*
    - export SRUSER=*netlink username*
    - export SRPASS=*netlink password*
- You will need to close the ssh connection and reopen it for the enviroment variables to take affect
- Now you can run the python script 'python3 study-rooms.py'
- This will only run it once so to automate it you need to use crontab
- Enter 'crontab -e' and choose vim or whichever editor you prefer.
- Then enter a line similar to this '1 8 * * * python3 /home/ubuntu/study-rooms.py'
- The first 5 characters indicates the time in which you want the script to run, mine for example runs the first minute of the 8th hour of the day, you may have to play around with the time to get it right because it is in UTC but the school opens bookings for the 7 days in the future every midnight.
- Save the file and you are fully automated!
