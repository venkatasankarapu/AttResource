import requests
import json
from werkzeug.wrappers import Response
import pprint
from flask import Flask


app = Flask(__name__)


@app.route("/issues", methods =['GET'])
def get_all_open_issues():
    url = "https://api.github.com/orgs/att/repos?type=public"
    response = []
    get_public_repos = requests.get(url,
                                    headers={"Authorization":
                                             "Basic ZGV2aWthLjUyMEBnbWFpbC5jb206ZGV2aWthMTIz"})
    public_repos_json = get_public_repos.json()

    for item in public_repos_json:
        url_item = "https://api.github.com/repos/att/"+item['name']+"/issues?state=open"
        repo_issues = requests.get(url_item, headers={"Authorization": "Basic ZGV2aWthLjUyMEBnbWFpbC5jb206ZGV2aWthMTIz"}).json()
        repo_info = {}
        repo_info['repository name:'] = item['name']
        repo_info['repository_id'] = item['id']
        iss_list = []
        for issue in repo_issues:
            issue_info = method_name(issue)
            issue_comments = requests.get(issue['comments_url'], headers={"Authorization": "Basic ZGV2aWthLjUyMEBnbWFpbC5jb206ZGV2aWthMTIz"}).json()
            iss_comments = []
            for issue_comment in issue_comments:
                method_getissues(iss_comments, issue_comment)
            issue_info['comments'] = iss_comments
            iss_list.append(issue_info)
        repo_info['issues'] = iss_list
        response.append(repo_info)

    (json.dumps(response, indent=2))

    return Response(json.dumps(response,indent=2),mimetype='application/json')


def method_getissues(iss_comments, issue_comment):
    comment = {}
    comment['comment_id'] = issue_comment['id']
    comment['comment_created_at'] = issue_comment['created_at']
    comment['comment_body'] = issue_comment['body']
    comment['comment_user_id'] = issue_comment['user']['id']
    iss_comments.append(comment)


def method_name(issue):
    issue_info = {}
    issue_info['issue_id'] = issue['id']
    issue_info['issue_number'] = issue['number']
    issue_info['issue_title'] = issue['title']
    issue_info['issue_description'] = issue['body']
    issue_info['issue_created_at'] = issue['created_at']
    issue_info['issue_created_by_user'] = issue['user']['id']
    issue_info['issue_status'] = issue['state']
    return issue_info


#Response(xml, mimetype='text/xml')
#get_all_open_issues()

if __name__ == '__main__':
    app.run(port=9898,debug=True)