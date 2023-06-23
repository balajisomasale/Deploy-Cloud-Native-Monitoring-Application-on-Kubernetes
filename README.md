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
- run the command to create an image: `docker build -t my-flask-app .`

  ![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/62b3bbda-0452-4cff-b030-914dbd0e5f52)

![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/5957f927-e0d2-4987-903c-eeab840afe24)

- Creating the Docker container by using : `docker run -p 5000:5000 edc7297738d9` :: `docker run image_id`

  ![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/3937128f-e8a4-4dce-9938-18400f7ead66)
  
- Docker desktop :

  ![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/f08fa8ab-6e3f-465d-8cb6-caa32102da91)


--------------------------------

### 4) Create ECR(Amazon Elastic Container Registry) repository using Python Boto3 and pushing Docker Image to ECR

Amazon Elastic Container Registry : 

![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/94b72b69-6734-44e6-bb2a-be1b333ff7f3)

```
- we can directly `create repository` from UI in AWS management console but it will be much better if we can directly use this by using `AWS BOTO3 module`
  https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
-  Documentation for ECR module : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html
-  For creating repo : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr/client/create_repository.html

```

Running the BOTO3.py file : 

```
- After writing the script, we can use : `pip3 install boto3` to install and then run the python file.

  ![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/cc19c77f-532f-47e7-8b69-e323ac5a9cc8)

- ECR repo is created from boto3 python script :

  ![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/fa78456b-8aaf-471f-a313-7b27359f386f)

- use `push commands` tab in the ECR UI for this repo:

   ![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/e192a270-8232-4595-95c4-c0a79f0856e6)

- After running the `suggested push commands`; we can see the `docker image` inside the ECR repo :

  ![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/f562f115-6d8d-4aa6-ada1-22e8e58b9dda)
```

-----------------------------------------------------------------

## Create EKS (Elastic Kubernetes Service) cluster and Nodegroups

![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/c7768d20-a13d-466b-b7ef-2d8136380a57)

Cluster is created : 

![image](https://github.com/balajisomasale/Deploy-Cloud-Native-Monitoring-Application-on-Kubernetes/assets/35003840/2fa957a7-6be9-4f3c-9db6-d1f0dd7b88ea)

Creating a Node group from EKS > compute : 

stuck at creating a Node group where roles are not getting created even after specified and cannot see that role in the drop down 

https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html


-----------------------------------------------------------------

After configuring nodes in EKS; we will move to

 ## Kubernetes Deployment from vscode.

```
- To use `Kubernetes` with Python code, we need `Kubernetes client` to deploy and manage services.
- Before that, we need to install `pip3 install Kubernetes`
- Run the `eks.py` file: `python eks.py` 


### Create deployment and service

```jsx
from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
api_client = client.ApiClient()

# Define the deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="my-flask-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-flask-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "my-flask-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-flask-container",
                        image="568373317874.dkr.ecr.us-east-1.amazonaws.com/my-cloud-native-repo:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)

# Create the deployment
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)

# Define the service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="my-flask-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "my-flask-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

# Create the service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)
```

make sure to edit the name of the image on line 25 with your image Uri.

- Once you run this file by running “python3 eks.py” deployment and service will be created.
- Check by running following commands:

```jsx
kubectl get deployment -n default (check deployments)
kubectl get service -n default (check service)
kubectl get pods -n default (to check the pods)
```

Once your pod is up and running, run the port-forward to expose the service

kubectl port-forward service/<service_name> 5000:5000
