import requests
import json
import os

from datetime import datetime
from src import ENV

# Configuration
GITHUB_TOKEN = ENV['GITHUB_TOKEN']
GITHUB_PROJECT_ID = ENV['GITHUB_PROJECT_ID']

# Asana configuration
ASANA_ACCESS_TOKEN = ENV['ASANA_ACCESS_TOKEN']
ASANA_WORKSPACE_ID = ENV['ASANA_WORKSPACE_ID']
ASANA_PROJECT_ID = ENV['ASANA_PROJECT_ID'] 

PROCESSED_ISSUES_FILE = ENV['PROCESSED_ISSUES_FILE']

# Get GitHub issues from the project using GraphQL API
def get_github_issues():
    query = """
    query {
      node(id: "%s") {
        ... on ProjectV2 {
          items(first: 100) {
            nodes {
              id
              content {
                __typename
                ... on Issue {
                  id
                  number
                  title
                  state
                  url
                  body
                  assignees(first: 10) {
                    nodes {
                      login
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    """ % GITHUB_PROJECT_ID

    headers = {
        "Authorization": f"bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.github.com/graphql",
        json={"query": query},
        headers=headers
    )

    data = response.json()
    
    if "data" not in data:
        print("GitHub API response (unexpected):", json.dumps(data, indent=2))
    return []
    
    # Extract and filter open issues
    open_issues = []
    try:
        for item in data['data']['node']['items']['nodes']:
            content = item.get('content')
            if content and content.get('__typename') == 'Issue' and content.get('state') == 'OPEN':
                open_issues.append({
                    'id': content.get('id'),
                    'number': content.get('number'),
                    'title': content.get('title'),
                    'description': content.get('body', ''),
                    'url': content.get('url'),
                    'assignees': [assignee['login'] for assignee in content.get('assignees', {}).get('nodes', [])]
                })
    except (KeyError, TypeError) as e:
        print(f"Error parsing GitHub response: {e}")
    
    return open_issues

# Create Asana task using requests library
def create_asana_task(issue):
    url = "https://app.asana.com/api/1.0/tasks"
    
    headers = {
        "Authorization": f"Bearer {ASANA_ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    task_data = {
        "data": {
            "name": f"GitHub #{issue['number']}: {issue['title']}",
            "notes": f"From GitHub Issue: {issue['url']}\n\n{issue.get('description', '')}",
            "workspace": ASANA_WORKSPACE_ID,
            "projects": [ASANA_PROJECT_ID]
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=task_data)
        response_json = response.json()
        
        if response.status_code == 201 or response.status_code == 200:
            if 'data' in response_json:
                task = response_json['data']
                print(f"Created Asana task for GitHub issue #{issue['number']}")
                return task
            else:
                print(f"Unexpected response format when creating task for issue #{issue['number']}")
                return None
        else:
            print(f"Error creating task for issue #{issue['number']}: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Exception creating task for issue #{issue['number']}: {str(e)}")
        return None

# Load already processed issues from file
def load_processed_issues():
    if os.path.exists(PROCESSED_ISSUES_FILE):
        with open(PROCESSED_ISSUES_FILE, 'r') as f:
            return json.load(f)
    return []

# Save processed issues to file
def save_processed_issues(processed_issues):
    with open(PROCESSED_ISSUES_FILE, 'w') as f:
        json.dump(processed_issues, f)

def main():
    print(f"Starting GitHub to Asana sync at {datetime.now().isoformat()}")
    
    # Load already processed issues
    processed_issues = load_processed_issues()
    print(f"Found {len(processed_issues)} previously processed issues")
    
    # Get GitHub issues
    github_issues = get_github_issues()
    print(f"Found {len(github_issues)} open GitHub issues")
    
    # Process new issues
    newly_processed = []
    
    for issue in github_issues:
        issue_id = issue['id']
        
        # Skip if already processed
        if issue_id in processed_issues:
            continue
            
        # Create corresponding Asana task
        asana_task = create_asana_task(issue)
        
        if asana_task:
            # Mark as processed
            newly_processed.append(issue_id)
    
    # Update processed issues list
    processed_issues.extend(newly_processed)
    save_processed_issues(processed_issues)
    
    print(f"Processed {len(newly_processed)} new issues")
    print(f"Sync completed at {datetime.now().isoformat()}")

if __name__ == "__main__":
    main()