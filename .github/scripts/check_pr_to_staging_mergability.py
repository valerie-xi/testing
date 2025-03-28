import os
from github import Github

sha = os.environ["COMMIT_SHA"]
access_token = os.environ["ADMIN_TOKEN"]

g = Github(access_token)
repo = g.get_repo("valerie-xi/testing")
for pull in repo.get_pulls():
    if pull.base.ref == 'main':
        staging_to_production_pr_is_open = True
        break
else:
    staging_to_production_pr_is_open = False

if staging_to_production_pr_is_open:
    repo.get_commit(sha=sha).create_status(
        state="failure",
        description="A staging -> production pull request is currently in progress.",
        context="Merge eligibility"
    )
else:
    repo.get_commit(sha=sha).create_status(
        state="success",
        description="Can be merged.",
        context="Merge eligibility"
    )
