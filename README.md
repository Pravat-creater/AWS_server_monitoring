# AWS_server_monitoring
# Production Server Monitoring & Incident Management System

This project simulates a real-world 24×7 IT Operations / Cloud Support environment.  
It continuously monitors server health, automatically detects issues based on defined thresholds, and generates timestamped incident logs.  
The same solution is designed to run both locally and on AWS EC2, making it cloud-ready.

---

## 🔍 Project Overview

In real production environments, servers must be monitored continuously to ensure high availability.  
Manual monitoring is inefficient, so organizations rely on automated systems to detect issues, raise incidents, and maintain logs for audit and compliance.

This project demonstrates how such a system can be built using Python.

---

## ⚙️ Key Features

- Continuous CPU monitoring using configurable thresholds  
- Automatic incident generation when CPU crosses the threshold  
- Timestamped incident logging for audit and tracking  
- Lightweight web dashboard to view live server health  
- Designed for deployment on AWS EC2  
- Simulates real 24×7 NOC / IT Support operations

---

## 🧠 How the System Works

1. The monitoring script continuously checks CPU usage.
2. A threshold (default: 20%) is defined for alerting.
3. When CPU usage exceeds the threshold:
   - An incident is triggered.
   - Incident details are logged with timestamp.
4. The dashboard displays real-time server metrics.
5. Logs can be reviewed for incident analysis and reporting.

---

## 🗂️ Project Structure




## 🛠️ Technologies Used

- Python 3
- Flask
- psutil
- Git & GitHub
- AWS EC2 (deployment-ready)

---

## ☁️ AWS Cloud Deployment (Overview)

This application can be deployed on an AWS EC2 instance:

- EC2 acts as the production server
- Python monitoring scripts run continuously
- Flask dashboard is exposed via EC2 public IP
- Security Groups control access (SSH & application ports)

This mirrors real-world cloud-based monitoring solutions.

---

## 🎯 Use Case Relevance

This project demonstrates hands-on experience with:

- Monitoring and maintaining production servers  
- Incident detection and logging  
- SOP and runbook-based operations  
- Cloud readiness and AWS fundamentals  
- 24×7 IT operations mindset  

---

## 🚀 Future Enhancements

- Email or Slack alerts for incidents  
- Disk and memory monitoring  
- Database and network monitoring  
- Storing logs in AWS S3  
- Role-based dashboard access  

---

## 👤 Author

Pravat  
Aspiring Cloud / IT Operations Engineer

---

## 📌 Note

This project is intended for learning and interview demonstration purposes and simulates real production monitoring behavior.
