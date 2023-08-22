import os

basic_tokens = {"us": {"qa": os.environ.get("QA_US"),
                       "stage": os.environ.get("STAGE_US"),
                       "uat": os.environ.get("UAT"),
                       "prod": "???"}}

