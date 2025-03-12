import requests
import json

def get_default_configs(config_file: str = 'configs.json') -> dict:
    """Load default configurations from a JSON file."""
    with open(config_file, 'r') as file:
        return json.load(file)

def get_auth_token(regional_iam: str, tenant_name: str, api_key: str) -> str:
    """Retrieve an authentication token from Checkmarx One."""
    url = f"{regional_iam}/auth/realms/{tenant_name}/protocol/openid-connect/token"
    data = {
        'grant_type': 'refresh_token',
        'client_id': 'ast-app',
        'refresh_token': api_key
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    
    print(f"Error fetching token: {response.status_code}, {response.text}")
    return None  # Return None if authentication fails

def retrieve_scheduled_scan_list(regional_ast_url: str, headers: dict) -> dict:
    """Retrieve the list of scheduled scans."""
    url = f"{regional_ast_url}/api/projects/schedules"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    
    print(f"Error retrieving scheduled scans: {response.status_code}, {response.text}")
    return None

def create_scheduled_scan(regional_ast_url: str, headers: dict, project_id: str) -> dict:
    """Create a new scheduled scan for a project."""
    url = f"{regional_ast_url}/api/projects/schedules/{project_id}"
    scan_payload = {
        "start_time": "12:05",
        "frequency": "daily",
        "engines": ["sast"],
        "branch": "main",
        "tags": {"version": "initial", "priority": "high"}
    }

    response = requests.post(url, json=scan_payload, headers=headers)
    if response.status_code in [200, 201]:
        return response.json()
    
    print(f"Error creating scheduled scan: {response.status_code}, {response.text}")
    return None

def delete_scheduled_scan(regional_ast_url: str, headers: dict, project_id: str) -> bool:
    """Delete an existing scheduled scan."""
    url = f"{regional_ast_url}/api/projects/schedules/{project_id}"

    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        return True  # Deletion successful
    
    print(f"Error deleting scheduled scan: {response.status_code}, {response.text}")
    return False

if __name__ == '__main__':
    configs = get_default_configs()
    auth_token = get_auth_token(
        regional_iam=configs.get('REGIONAL_IAM_URL'),
        tenant_name=configs.get('TENANT_NAME'),
        api_key=configs.get('API_KEY')
    )

    if not auth_token:
        exit("Failed to retrieve authentication token. Exiting.")

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json; version=1.0"
    }

    project_id = "<project-id>"

    #scheduled_scans = retrieve_scheduled_scan_list(regional_ast_url=configs.get('REGIONAL_AST_URL'), headers=headers)
    #delete_success = delete_scheduled_scan(regional_ast_url=configs.get('REGIONAL_AST_URL'), headers=headers, project_id=project_id)
    
    #if delete_success:
    #    print(f"Deleted scheduled scan for project {project_id}")

    #create_scheduled_scan_response = create_scheduled_scan(regional_ast_url=configs.get('REGIONAL_AST_URL'), headers=headers, project_id=project_id)
    
    #if create_scheduled_scan_response:
    #    print(f"Created scheduled scan for project {project_id}")

