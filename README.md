# **Checkmarx One Scheduled Scan Automation Script**

## **Overview**
This Python script automates the scheduling and management of security scans in **Checkmarx One**. It allows users to:
- Retrieve a list of scheduled scans.
- Create a new scheduled scan for a project.
- Delete an existing scheduled scan.

## **Prerequisites**
1. **Python 3.x** installed on your system.
2. **Requests library** installed. You can install it using:
   ```
   pip install requests
   ```
3. A **valid** API key for Checkmarx One.
4. The configs.json file containing the required configuration details.
## Local Configuration
**Before running the script, create a configs.json** file in the same directory with the following format (replacing anything in <>):
```
{
    "API_KEY":"<api-key>",
    "TENANT_NAME":"<tenant-name>",
    "REGIONAL_AST_URL":"<REGIONAL_AST_URL>",
    "REGIONAL_IAM_URL":"<REGIONAL_IAM_URL>"
}
```
## Checkmarx Configuration
1. Ensure you have the project-id of the project you wish to schedule the scan for
2. Make sure under project settings for the project you have the remote url for the repository
3. Verify that the permissions of **view-schedule-scan** ie enabled for the user who is creating the scheduled scans.
## Usage
1. **Update the project_id**
Before running the script, update the project_id in the main function:
```
project_id = "<project-id>"
``` 
2. Also, make sure to update the scan schedule in the create_scheduled_scan function. The supported params are here: https://checkmarx.stoplight.io/docs/checkmarx-one-api-reference-guide/branches/main/c1i95l3w5ohqh-create-a-scan-schedule#request-body  **Make sure the branch name is valid for the project**

```
    scan_payload = {
        "start_time": "12:05",
        "frequency": "daily",
        "engines": ["sast"],
        "branch": "main",
        "tags": {"version": "initial", "priority": "high"}
    }
```

3. Replace "\<project-id>" with your actual Checkmarx project ID.

2. **Run the Script**
Execute the script using: 

```python main.py```
