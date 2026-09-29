 

````
# Project 1 - Scalable Web Application using AWS ALB and Auto Scaling

## 1. Project Objective

The objective of this project is to build a scalable and highly available web application on AWS.

The application is deployed on Amazon EC2 instances and uses an Application Load Balancer (ALB) to distribute incoming requests across multiple healthy EC2 instances.

An Auto Scaling Group (ASG) maintains the required number of EC2 instances and can replace unhealthy or terminated instances.

---

## 2. AWS Services Used

- Amazon EC2
- Application Load Balancer (ALB)
- Target Group
- Auto Scaling Group
- Launch Template
- Amazon Machine Image (AMI)
- Amazon VPC
- Security Groups
- Availability Zones
- EC2 Instance Metadata Service (IMDSv2)

---

## 3. Architecture

```text
                    Internet User
                         |
                         v
              Application Load Balancer
                         |
                         v
                   Target Group
                    /         \
                   /           \
                  v             v
             EC2 Instance 1   EC2 Instance 2
              AZ: 1a           AZ: 1b
                   \           /
                    \         /
                     Auto Scaling
                         |
                    Desired: 2
                    Minimum: 2
                    Maximum: 3
````

---

## 4. Application

The web application is developed using Python Flask.

The application displays information about the EC2 instance handling the request, including:

-  Instance ID 
-  Availability Zone 
-  Hostname 
-  Application health status 

This helps demonstrate that the Application Load Balancer can distribute requests between different EC2 instances.

---

## 5. Implementation Steps

### Step 1 - Create EC2 Instance

An Amazon Linux 2023 EC2 instance was created using the t3.micro instance type.

The Flask application was deployed on the EC2 instance.

The application runs on port 5000.

---

### Step 2 - Configure Flask Application

A Flask web application was created with a `/` route.

The application uses EC2 Instance Metadata Service (IMDSv2) to retrieve:

-  Instance ID 
-  Hostname 
-  Availability Zone 

The application listens on:

```
```

```
0.0.0.0:5000
```

---

### Step 3 - Configure Systemd Service

A systemd service was created so that the Flask application starts automatically and restarts if the application stops.

Service name:

```
```

```
scalable-web-app.service
```

---

### Step 4 - Create AMI

An Amazon Machine Image (AMI) was created from the configured EC2 instance.

The AMI contains the Flask application and its configuration.

This AMI is used as the base image for new instances launched by the Auto Scaling Group.

---

### Step 5 - Create Launch Template

A Launch Template was created using the custom AMI.

Configuration includes:

-  Instance type: t3.micro 
-  Amazon Linux 2023 
-  Key pair 
-  Security Group 
-  Root EBS volume 

A newer Launch Template version was created after updating the application UI.

---

### Step 6 - Create Target Group

A Target Group was created for the EC2 instances.

Configuration:

```
```

```
Protocol: HTTP
Port: 5000
Health Check Path: /
```

The Target Group checks whether the application is healthy before sending traffic to an instance.

---

### Step 7 - Create Application Load Balancer

An internet-facing Application Load Balancer was created.

The ALB is configured across two Availability Zones:

```
```

```
ap-south-1a
ap-south-1b
```

The ALB listens on:

```
```

```
HTTP : 80
```

Incoming requests are forwarded to the Target Group on port 5000.

---

### Step 8 - Create Auto Scaling Group

An Auto Scaling Group was created using the Launch Template.

Configuration:

```
```

```
Desired Capacity: 2
Minimum Capacity: 2
Maximum Capacity: 3
```

The Auto Scaling Group uses two Availability Zones for better availability.

---

### Step 9 - Configure Health Checks

The Auto Scaling Group uses EC2 and ELB health checks.

If an instance becomes unhealthy or is terminated, the Auto Scaling Group can launch a replacement instance.

---

### Step 10 - Test Load Balancing

The Application Load Balancer DNS name was opened in a browser.

The application displayed the instance information.

After refreshing the page, requests were observed reaching different EC2 instances in different Availability Zones.

This verified that the ALB was distributing traffic across healthy instances.

---

### Step 11 - Test Auto Scaling Self-Healing

One EC2 instance managed by the Auto Scaling Group was intentionally terminated.

The Auto Scaling Group detected that the desired capacity was no longer available and launched a replacement instance.

The replacement instance was registered with the Target Group and became healthy.

This demonstrated the self-healing capability of the Auto Scaling Group.

---

## 6. Security Configuration

Security best practices were followed during implementation.

-  HTTP port 80 is exposed through the Application Load Balancer. 
-  EC2 application port 5000 accepts traffic only from the ALB Security Group. 
-  SSH access is restricted instead of being open to the entire internet. 
-  IMDSv2 is required for EC2 metadata access. 
-  AWS credentials and private keys are not stored in the GitHub repository. 
-  The EC2 private application port is not directly exposed to the internet. 

---

## 7. Testing and Validation

The following tests were performed:

### Test 1 - Application Test

The Flask application was accessed successfully through the load balancer.

### Test 2 - Load Balancer Test

Refreshing the application showed different EC2 instance information, demonstrating traffic distribution.

### Test 3 - Target Health Test

Both EC2 instances were shown as healthy in the Target Group.

### Test 4 - Auto Scaling Test

After terminating an instance, the Auto Scaling Group launched a replacement instance automatically.

---

## 8. Expected Result

The final application provides:

-  Highly available web application 
-  Traffic distribution using ALB 
-  Multiple EC2 instances 
-  Automatic instance replacement 
-  Deployment across multiple Availability Zones 
-  Health checks through the Target Group 
-  Secure communication between ALB and EC2 instances 

---

## 9. Project Structure

```
```

```
Project-1-Scalable-Web-Application/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── screenshots/
│
└── README.md
```

---

## 10. How to Access the Application

Open the Application Load Balancer DNS name in a web browser.

Example:

```
```

```
http://<ALB-DNS-NAME>
```

The application displays the EC2 instance information handling the request.

---

## 11. Key Learnings

Through this project, I learned:

-  How to deploy a Flask application on EC2 
-  How Application Load Balancer distributes traffic 
-  How Target Groups perform health checks 
-  How Auto Scaling maintains EC2 capacity 
-  How Launch Templates are used to launch instances 
-  How AMIs are used for repeatable deployments 
-  How Availability Zones improve application availability 
-  How Security Groups control network access 
-  How EC2 IMDSv2 provides instance metadata 
-  How AWS architecture can be designed for scalability and availability 

---

## 12. Conclusion

This project demonstrates a scalable and highly available AWS web application architecture using Amazon EC2, Application Load Balancer, Target Groups, Auto Scaling Groups, AMIs, Launch Templates, and multiple Availability Zones.

The project also demonstrates traffic distribution, health checking, and automatic replacement of EC2 instances. 
