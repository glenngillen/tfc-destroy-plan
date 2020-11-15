# Terraform Cloud/Enterprise - Queue Destroy Plan

Within Terraform Cloud & Terraform Enterprise there's a issue with permissions where a person is unable to access the screen to queue a "destroy plan" unless they _also_ have permission to delete the entire workspace. These are actually seperate permissions though and the UI should grant access to the features independently.

API access to queue a destroy plan is still possible though. So in the interim (i.e., while we await a fix + release to the UI) here's a script that will allow someone to queue a destroy.

## Setup

Install the dependencies:

```bash
$ pip3 install -r requirements.txt
```

Make sure you've set the correct values for your TFC/TFE auth:

```bash
$ export TFE_URL=https://app.terraform.io/ TFE_ORG=Compu-Global-Hyper-Mega-Net TFE_TOKEN=token-goes-here
```

## Usage


And then run the script with the name of the workspace you want to queue a destroy plan for:

```bash
$ python3 destroy-plan.py my-workspace-name
```

