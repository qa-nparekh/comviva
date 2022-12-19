import json

import requests


def update_recored(report_data, runby):
    url = "http://localhost/automation/api/save-user-report"

    automation_report_data = json.dumps(report_data)
    payload = {
        'json_response': automation_report_data, 'user_id': runby}
    print(payload)
    files = [

    ]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
