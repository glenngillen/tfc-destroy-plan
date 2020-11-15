import os
import sys
from terrasnek.api import TFC

def queue_destroy_run(api, workspace_name):
    workspace = api.workspaces.show(workspace_name)
    if workspace == None:
        print('Error: unable to find a workspace named ' + workspace_name)
        exit(1)
    workspace_id = workspace["data"]["id"]
    payload = {
        "data": {
            "attributes": {
                "is-destroy": True
            },
            "relationships": {
                "workspace": {
                    "data": {
                        "id": workspace_id
                    }
                }
            }
        }
    }
    run = api.runs.create(payload)
    if run == None:
        print('Error: Unable to queue destroy plan. The provided token probably does not have "apply" permission.')
        exit(1)
    run_id = run["data"]["id"]
    return run_id

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 destroy-plan.py [workspace-name]')
        print('')
        print('Please also ensure that the following environment variables are set to the appropriate values for your TFE install:')
        print(' * TFE_TOKEN')
        print(' * TFE_URL')
        print(' * TFE_ORG')
        exit(1)
    TFE_TOKEN = os.getenv("TFE_TOKEN", None)
    TFE_URL = os.getenv("TFE_URL", None)
    TFE_ORG = os.getenv("TFE_ORG", None)

    api = TFC(TFE_TOKEN, url=TFE_URL)
    api.set_org(TFE_ORG)

    destroy_run_id = queue_destroy_run(api, sys.argv[1])
    print('Successfully queued destroy plan')