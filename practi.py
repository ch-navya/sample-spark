import psycopg2
import json
import requests
import os
conn = psycopg2.connect(database=os.getenv('DB_DATABASE'),host=os.getenv('DB_HOST'),user=os.getenv('DB_USER'),password=os.getenv('DB_PASS'),port=os.getenv('DB_PORT'))
cursor=conn.cursor()
def insert_license(license):
    if license is None:
        insert_qu= "insert into license(key,name,spdx_id,url,node_id)values(%s,%s,%s,%s,%s)"
        insert_va= (None,None,None,None,None)
        cursor.execute(insert_qu,insert_va)
    else:
        cursor.execute("insert into license(key,name,spdx_id,url,node_id) values(%s,%s,%s,%s,%s)",(license['key'],license['name'],license['spdx_id'],license['url'],license['node_id']))
        cursor.execute("select * from license")
        result = cursor.fetchall()
        for row in result:
            print(row[0],row[1],row[2],row[3],row[4],row[5]) 
def insert_owner(owner):
    cursor = conn.cursor()
    cursor.execute("insert into owner(login,id,node_id,avatar_url,gravatar_id,url,html_url,followers_url,following_url,gists_url,starred_url,subscriptions_url,organizations_url,repos_url,events_url,received_events_url,type,site_admin) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(owner['login'],owner['id'],owner['node_id'],owner['avatar_url'],owner['gravatar_id'],owner['url'],owner['html_url'],owner['followers_url'],owner['following_url'],owner['gists_url'],owner['starred_url'],owner['subscriptions_url'],owner['organizations_url'],owner['repos_url'],owner['events_url'],owner['received_events_url'],owner['type'],owner['site_admin']))
    cursor.execute("select * from owner")
    result = cursor.fetchall()
    print(result)
    

def insert_repo(repos):
    cursor = conn.cursor()
    cursor.execute("insert into item(id,node_id,name,full_name,private,html_url,description,fork,url,forks_url,keys_url,collaborators_url,teams_url,hooks_url,issue_events_url,events_url,assignees_url,branches_url,tags_url,blobs_url,git_tags_url,git_refs_url,trees_url,statuses_url,languages_url,stargazers_url,contributors_url,subscribers_url,subscription_url,commits_url,git_commits_url,comments_url,issue_comment_url,contents_url,compare_url,merges_url,archive_url,downloads_url,issues_url,pulls_url,milestones_url,notifications_url,labels_url,releases_url,deployments_url,created_at,updated_at,pushed_at,git_url,ssh_url,clone_url,svn_url,homepage,size,stargazers_count,watchers_count,language,has_issues,has_projects,has_downloads,has_wiki,has_pages,has_discussions,forks_count,mirror_url,archived,disabled,open_issues_count,allow_forking,is_template,web_commit_signoff_required,topics,visibility,forks,open_issues,watchers,default_branch,score) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(repos['id'],repos['node_id'],repos['name'],repos['full_name'],repos['private'],repos['html_url'],repos['description'],repos['fork'],repos['url'],repos['forks_url'],repos['keys_url'],repos['collaborators_url'],repos['teams_url'],repos['hooks_url'],repos['issue_events_url'],repos['events_url'],repos['assignees_url'],repos['branches_url'],repos['tags_url'],repos['blobs_url'],repos['git_tags_url'],repos['git_refs_url'],repos['trees_url'],repos['statuses_url'],repos['languages_url'],repos['stargazers_url'],repos['contributors_url'],repos['subscribers_url'],repos['subscription_url'],repos['commits_url'],repos['git_commits_url'],repos['comments_url'],repos['issue_comment_url'],repos['contents_url'],repos['compare_url'],repos['merges_url'],repos['archive_url'],repos['downloads_url'],repos['issues_url'],repos['pulls_url'],repos['milestones_url'],repos['notifications_url'],repos['labels_url'],repos['releases_url'],repos['deployments_url'],repos['created_at'],repos['updated_at'],repos['pushed_at'],repos['git_url'],repos['ssh_url'],repos['clone_url'],repos['svn_url'],repos['homepage'],repos['size'],repos['stargazers_count'],repos['watchers_count'],repos['language'],repos['has_issues'],repos['has_projects'],repos['has_downloads'],repos['has_wiki'],repos['has_pages'],repos['has_discussions'],repos['forks_count'],repos['mirror_url'],repos['archived'],repos['disabled'],repos['open_issues_count'],repos['allow_forking'],repos['is_template'],repos['web_commit_signoff_required'],repos['topics'],repos['visibility'],repos['forks'],repos['open_issues'],repos['watchers'],repos['default_branch'],repos['score']))
    cursor.execute("select * from item")
    result = cursor.fetchall()
    print(result)
    conn.commit()
    
page=(input("enter page num:"))
for i in range(1,page+1):
  url = "https://api.github.com/search/repositories?sort=stars&order=desc&q=created%3A%3E2022-11-01&per_page=100&'page='"+str(i)


responce = requests.get(url)
data = responce.json()
repos = data['items']


for repo in repos:
   license = repo['license']
   owner = repo['owner']
   insert_license(license)
   insert_owner(owner)
   insert_repo(repo)   

