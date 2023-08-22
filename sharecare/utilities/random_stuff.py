import pymsteams

myTeamsMessage = pymsteams.connectorcard("https://sharecare.webhook.office.com/webhookb2/a4e031b8-8b5c-44fc-8fa3-0d0a7a51a0cd@4791286b-0707-4782-8dae-89fe4a320b09/IncomingWebhook/0f68409dcf094fb89f0186a2f073e161/8ddc14dd-8778-44be-89bf-423798a9218f")

cardsection = pymsteams.cardsection()

# Android SANITY | Terra | R-CANDI 4.32.0 (19448)
# cardsection.title("WLA|iOS Sanity|Ulysses|R-Candi 2.33.0(23145)")
# cardsection.title("SC | iOS SANITY | Venus | R-CANDI 2.35.0 (24359)")
cardsection.title("SC | Test Webhook")

cardsection.linkButton("Testrail Link", "test")

cardsection.text("<ul><li>Passed - 139 </li><li>Failed - 0 </li><li>Blocked - 0 </li><li>Irrelevant - 4 </li><li>Retest - 0 </li><li>Manual/Untested - 18 </li></ul>")

myTeamsMessage.summary("Test Results summary")

myTeamsMessage.addSection(cardsection)

myTeamsMessage.send()








