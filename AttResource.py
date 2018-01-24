import json
import requests
from flask import Flask
from werkzeug.wrappers import Response

app = Flask(__name__)

"""Gets organization all open issues along with issue comments from public GIT repositories.
   Returns : Json object with issues group by repository name
 """
@app.route("/issues", methods=['GET'])
def get_all_open_issues():
    public_repos_json = get_public_repos_by_org("att")
    response = []
    for item in public_repos_json:
        repo_info = {}
        repo_info['repository name:'] = item['name']
        repo_info['repository_id'] = item['id']
        repo_info['issues'] = get_open_issues_by_repo_name(item['name'])
        response.append(repo_info)
    return Response(json.dumps(response, indent=2), mimetype='application/json')


"""Gets all open issues for a repository using repo name
 Returns: Returns issues. For simplicity basic Authorization has been used
 and this will be replaced with  other authz types for deployment"""
def get_open_issues_by_repo_name(repo_name):
    repo_issues = requests.get("https://api.github.com/repos/att/" + repo_name + "/issues?state=open",
                               headers={"Authorization": "Basic ZGV2aWthLjUyMEBnbWFpbC5jb206ZGV2aWthMTIz"}).json()
    iss_list = []
    for issue in repo_issues:
        issue_info = {}
        issue_info['issue_id'] = issue['id']
        issue_info['issue_number'] = issue['number']
        issue_info['issue_title'] = issue['title']
        issue_info['issue_description'] = issue['body']
        issue_info['issue_created_at'] = issue['created_at']
        issue_info['issue_created_by_user'] = issue['user']['id']
        issue_info['issue_status'] = issue['state']
        issue_info['comments'] = get_issue_comments(issue['comments_url'])
        iss_list.append(issue_info)
    return iss_list


""" Get all comments for an issue by issue nummber.
  Returns: Returns list of comments of an issue """
def get_issue_comments(issue_comments_url):
    issue_comments = requests.get(issue_comments_url, headers={
        "Authorization": "Basic ZGV2aWthLjUyMEBnbWFpbC5jb206ZGV2aWthMTIz"}).json()
    iss_comments = []
    for issue_comment in issue_comments:
        comment = {}
        comment['comment_id'] = issue_comment['id']
        comment['comment_created_at'] = issue_comment['created_at']
        comment['comment_body'] = issue_comment['body']
        comment['comment_us er_id'] = issue_comment['user']['id']
        iss_comments.append(comment)
    return iss_comments


"""Gets all public GIT repositories for an organization
 Returns organization's public repository list """
def get_public_repos_by_org(org_name):
    url = "https://api.github.com/orgs/" + org_name + "/repos?type=public"
    get_public_repos = requests.get(url, headers={"Authorization": "Basic ZGV2aWthLjUyMEBnbWFpbC5jb206ZGV2aWthMTIz"})
    return get_public_repos.json()


if __name__ == '__main__':
    app.run(port=9898, debug=True)
