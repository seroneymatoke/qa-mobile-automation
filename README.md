## Sharecare Mobile Automation Framework - Zeus
Test automation scripts for sanity and smoke for iOS/Android.

### Framework description
______
The Keyword driven framework uses the following modules
- Appium
- Behave
- Testrail reporting
- SauceLabs integration for cloud devices testing.

### Installation
______
####
For this installation to run successfully you need Python 3

Installation instructions are as below
- Download python >3.10 from python.org and follow instructions as recommended
- Updating from 3.x > 3.10 via homebrew https://www.freecodecamp.org/news/python-version-on-mac-update/

#### Clone the repository
- Clone the repository from [github](https://github.com/Sharecare/qa-mobile-zeus) preferably from master branch.

#### To install dependencies

#### From PyPI
```
pip3 install -r requirements.txt
```

#### Mac OS certificate issues
Once in a while some packages may throw an exception as below

```
verify error:num=20:unable to get local issuer certificate
```
When this occurs run the command below

```
/Applications/Python\ 3.x/Install\ Certificates.command
```

### Executing Tests
____
#### Running test  for behave

##### Quick check to verify everything works
```
 behave -k -v sharecare/features --tags=ss -D platform=cloud_ios -D env=STAGE -D app_version=2.35.0_Experimental -D build=24282 -D release=Venus -D label=SC -D market=US
```


##### Sanity
```
 behave -k -v sharecare/features --tags=sanity_android -D platform=cloud_ios -D env=STAGE -D app_version=2.35.0_Experimental -D build=24282 -D release=Venus -D label=SC -D market=US```
```

Configurable params
- tags == sanity/smoke
- platform == cloud_android/cloud_ios/ios_simulator/android_device/ios_device
- env=STAGE/UAT
- market=US/BR
- app_version=application version
- release = release_name e.g. Quirinus/Rhea
- build = build_number
- app_type = R-Candi/Beta-UAT/Alpha etc
- label = SC for sharecare and CF for WLA

PS: Remember to change config to match running environment configs/config.py

Remember to setup the following parameters in you Enviromnent
TESTRAIL_USERNAME=username
TESTRAIL_PASSWORD=password
SAUCE_USERNAME=user
SAUCE_KEY=access key

PS: For running locally on your device you'd need the following tools
- Android: ADB, Appium Server
- iOS: Appium Server, Xcode

The instances have to be running for a successful execution.


### Scenarios Covered
To be updated


### Test Reports
____
The test report can be accessed from the testrail matching the parameters above.

### Pending
- CICD integration
- Autodeploy on SL
- Containerization most probably docker


### @todo - Add doc for Prod
### Coding standards
____
The code conforms to the following standards.

1. [PEP8](https://www.python.org/dev/peps/pep-0008/)
2. Function names conforms to what they implement.
3. All classes are documented.


