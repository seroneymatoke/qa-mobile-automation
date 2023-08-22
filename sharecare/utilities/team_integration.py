"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created by seroneymatoke
Date: 27.03.23
Purpose:
Implementation:
TestData:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import pymsteams

webhooks = {
    "prod": "https://sharecare.webhook.office.com/webhookb2/a4e031b8-8b5c-44fc-8fa3-0d0a7a51a0cd@4791286b-0707-4782-8dae-89fe4a320b09/IncomingWebhook/0f68409dcf094fb89f0186a2f073e161/8ddc14dd-8778-44be-89bf-423798a9218f",
    "stage": "https://sharecare.webhook.office.com/webhookb2/a4e031b8-8b5c-44fc-8fa3-0d0a7a51a0cd@4791286b-0707-4782-8dae-89fe4a320b09/IncomingWebhook/aa84775f32ff4fcc969c79ccd43eb8e2/8ddc14dd-8778-44be-89bf-423798a9218f",
    "uat": "https://sharecare.webhook.office.com/webhookb2/a4e031b8-8b5c-44fc-8fa3-0d0a7a51a0cd@4791286b-0707-4782-8dae-89fe4a320b09/IncomingWebhook/138cd5422a254198b4ecdf511d37d595/8ddc14dd-8778-44be-89bf-423798a9218f"
}
def push_to_teams(webhook, passed, branch, url):
    teams_message = pymsteams.connectorcard(webhook)
    cardsection = pymsteams.cardsection()
    cardsection.title(branch)
    cardsection.linkButton("Testrail Link", url)
    cardsection.text(
        "<ul>"
        "<li>Passed - "+str(passed) +"</li>"
        # "<li>Failed - "+str(failed) +" </li>"
        # "<li>Skipped - "+str(skipped) +" </li>"
        "<li>Retest - 0 </li>"
        "</ul>"
    )
    teams_message.summary("Test Results summary")
    teams_message.addSection(cardsection)
    teams_message.send()