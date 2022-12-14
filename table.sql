CREATE TABLE owner(
    owner_id SERIAL NOT NULL PRIMARY KEY,
    login TEXT,
    id INT,
    node_id TEXT,
    avatar_url TEXT,
    gravatar_id TEXT,
    url TEXT,
    html_url TEXT,
    followers_url TEXT,
    following_url TEXT,
    gists_url TEXT,
    starred_url TEXT,
    subscriptions_url TEXT,
    organizations_url TEXT,
    repos_url TEXT,
    events_url TEXT,
    received_events_url TEXT,
    type VARCHAR(100),
    site_admin BOOLEAN
);

CREATE TABLE license(
    license_id SERIAL NOT NULL PRIMARY KEY,
    key  TEXT,
    name TEXT,
    spdx_id TEXT,
    url TEXT,
    node_id TEXT
);
CREATE TABLE item( item1_id SERIAL NOT NULL PRIMARY KEY,
                  id INT,
                  node_id TEXT,
                  name TEXT,
                  full_name TEXT,
                  private bool,
                  html_url TEXT,
                  description TEXT,
                  fork BOOLEAN,
                  url TEXT,
                  forks_url TEXT,
                  keys_url TEXT,
                  collaborators_url TEXT,
                  teams_url TEXT,
                  hooks_url TEXT,
                  issue_events_url TEXT,
                  events_url TEXT,
                  assignees_url TEXT,
                  branches_url TEXT,
                  tags_url TEXT,
                  blobs_url TEXT,
                  git_tags_url TEXT,
                  git_refs_url TEXT,
                  trees_url TEXT,
                  statuses_url TEXT,
                  languages_url TEXT,
                  stargazers_url TEXT,
                  contributors_url TEXT,
                  subscribers_url TEXT,
                  subscription_url TEXT,
                  commits_url TEXT,
                  git_commits_url TEXT,
                  comments_url TEXT,
                  issue_comment_url TEXT,
                  contents_url TEXT,
                  compare_url TEXT,
                  merges_url TEXT,
                  archive_url TEXT,
                  downloads_url TEXT,
                  issues_url TEXT,
                  pulls_url TEXT,
                  milestones_url TEXT,
                  notifications_url TEXT,
                  labels_url TEXT,
                  releases_url TEXT,
                  deployments_url TEXT,
                  created_at TIMESTAMP,
                  updated_at timestamp,
                  pushed_at timestamp,
                  git_url TEXT,
                  ssh_url TEXT,
                  clone_url TEXT,
                  svn_url TEXT,
                  homepage TEXT,
                  size int,
                  stargazers_count int,
                  watchers_count int,
                  language TEXT,
                  has_issues BOOLEAN,
                  has_projects BOOLEAN,
                  has_downloads BOOLEAN,
                  has_wiki BOOLEAN,
                  has_pages BOOLEAN,
                  has_discussions BOOLEAN,
                  forks_count INT,
                  mirror_url TEXT,
                  archived BOOLEAN,
                  disabled BOOLEAN,
                  open_issues_count INT,
                  allow_forking BOOLEAN,
                  is_template BOOLEAN,
                  web_commit_signoff_required BOOLEAN,
                  visibility TEXT,
                  forks INT,
                  open_issues INT,
                  watchers INT,
                  default_branch TEXT,
                  score INT,
topics TEXT [],
                  owner_id SERIAL NOT NULL REFERENCES owner(owner_id),
                  license_id SERIAL NOT NULL REFERENCES license(license_id)
);
select * from owner
select * from license
select * from item
truncate table license,item,owner
drop table owner,item,license
select distinct(id) from owner