# Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes

Source: https://www.youtube.com/watch?v=kBWCsHEcWnc&t=140s&ab_channel=CloudChamp

Objective: How to create Monitoring Application in Python using Flask and psutil on Kubernetes

- `Flask` is the Python web framework
-  `psutil` (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes

DevOps Project from scratch


![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/68c0f11a-c59b-4006-b258-7ae98e22db49)

### Prerequisites:

Programmatic access and AWS configured with CLI: 

- `Profile` > `Security credentials` > `Create Access Keys`
- from CLI:  `aws configure and to check the user's list: `aws iam list-users`

![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/d7a26ca6-de36-45eb-b988-fabb406757cc)

watch this if you are facing this issue - The issue resolved 

https://www.youtube.com/watch?v=u0JyzUGzvJA&ab_channel=r2schools

- checking whether Python, docker, and kubectl are installed or not :

  ![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/cab6bcb7-e0fa-4ba6-a38c-e2c072d61338)


-----------------

### 2) Running Python code locally
      
As we have Python already, we need to install the below modules:
- To install `psutil`: `pip3 install psutil`
- To install `Flask module`: `pip3 install flask` to avoid the flask module not being found 
- For running the requirements: `pip3 install -r requirements.txt`

Run the Python app file: 

![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/e52ad13f-601a-464d-8e52-b617684aa043)

Output : 

![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/cd1196b4-335b-4bb1-8d0e-e0d98aa593b2)

Adding few css styling to the UI : 
- using `render_template` module in the app.py file
- create `index.html` and pulling these css styles using render_template(index.html)

 ![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/4e29adf3-3293-48cd-84fa-319dc5e3396e)

--------------------

### 3) Containerize the App by creating Dockerfile:

- create `Dockerfile` which will create docker `image` and then will give the `container`

  ![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/62b3bbda-0452-4cff-b030-914dbd0e5f52)

