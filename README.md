# python-selenium-browserstack
Run python tests on browserstack using the SDK.

## Prerequisite
```
python3 should be installed
```

## Setup
* Clone the repo
```
git clone https://github.com/Greninja28/Browser-stack-Selenium-test.git
``` 
* Install packages
```
pip3 install selenium==4.9.0
pip install pytest
```

## Set BrowserStack Credentials
* Add your BrowserStack username and access key in the flipkart.py fle.
* You can also export them as environment variables, `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY`:

  #### For Linux/MacOS
    ```
    export BROWSERSTACK_USERNAME=<browserstack-username>
    export BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
    ```
  #### For Windows
    ```
    setx BROWSERSTACK_USERNAME=<browserstack-username>
    setx BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
    ```

## Running tests
* Run sample test:
  - To run the sample test locally run:
    ```
    pytest flipkart.py
    ``` 
