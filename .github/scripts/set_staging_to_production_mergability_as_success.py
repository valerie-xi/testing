import os
from github import Github


if os.environ["GITHUB_HEAD_REF"] == "staging":
    access_token = os.environ["ADMIN_TOKEN"]
    g = Github(access_token)
    repo = g.get_repo("valerie-xi/testing")

    for pull in repo.get_pulls():
        if pull.base.ref == 'staging':
            repo.get_commit(sha=pull.head.sha).create_status(
                state="success",
                description="Can be merged.",
                context="Merge eligibility"
            )
