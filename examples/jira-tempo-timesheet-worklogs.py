# coding=utf-8
from atlassian import Jira
from pprint import pprint
import logging

jira = Jira(
    url='http://localhost:8080',
    username='admin',
    password='admin',
    advanced_mode=True  #  You can use it without advanced mode. 
    )

logging.basicConfig(level=logging.DEBUG)
# deprecated_issue_worklog = jira.tempo_timesheets_get_worklogs_by_issue("PROJ-1234")
latest_issue_worklog = jira.tempo_4_timesheets_find_worklogs(taskKey=["PROJ-1234"])
# pprint(deprecated_issue_worklog.json())
pprint(latest_issue_worklog.json())