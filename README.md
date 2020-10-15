# GVE_Devnet_Meraki_CICDPipeline
Meraki APIs as part of a CICD Pipeline 






| :exclamation:  External repository notice   |
|:---------------------------|
| This repository is now mirrored at "PLEASE UPDATE HERE - add External repo URL after code review is completed"  Please inform a https://github.com/gve-sw/ organization admin of any changes to mirror them to the external repo |

## Contacts
* Ramona Renner
* Jason Mah



## Introduction

This demonstration shows the use of Meraki APIs in conjunction with a CICD (Continuous Integration / Continuous Delivery) Pipeline. The workflow covers the creation and merging of a branch for proposed changes and the automatic deployment and testing in two networks – testing and production. Hereby, the changes will only be applied to the production network after successful deployment and testing in the testing network. 

The scenario for the demo is build around a customer who desires to improve and modernize the internal processes of network provisioning and management. Hereby the customer is interested in network programmability and NetDevOps methods due to the positive effects like time and cost optimization and error reduction.



## Pre-requisites

* Meraki Dashboard
* Dashboard API Key (Instructions shared in this document later)
* Two Meraki networks and their network IDs (Instructions shared in this document later)
* Cisco's "Meraki Small Business" Sandbox and its network ID (Instructions shared in this document later)
* GitLab Account
* Git installed (CLI with Git support)
* Google Chrome, Firefox or Microsoft Edge



## Business Use Case 

### IT Manager’s problem to be solved with this use case:  

* **Needs:** Improve and modernize internal network provisioning and management through network programmability and NetDevOps methods.
* **Challenge (WHY?):** Manual or limited automation leads to inconsistent configuration, inefficiency and complexity.
* **Solution:** A CICD pipeline to automate the testing and delivery of changes in conjunction with our Meraki Enterprise portfolio.
* **Business Outcomes:** More frequent and reliable delivery of changes. Furthermore, early testing and automation improves the change quality, and the use of a repository allows a centralized storing of all configurations.

![/IMAGES/0image.png](/IMAGES/overview.png)


## Getting Started

High Level Design Demo: 

![/IMAGES/0image.png](/IMAGES/highleveldesign.png)

The demonstration requires some pre-configuration steps locally and in GitLab, that are covered in the next section. 



## Pre-Configuration

### Reserve Sandbox

This demo uses a Cisco Sandbox to demonstrate local testing as part of the CICD pipeline. To reserve the **Meraki Small Business** Sandbox the following steps are required:

1. On the Cisco DevNet Site (https://developer.cisco.com/site/sandbox/), go to **Sandbox Catalog**

    ![/IMAGES/0image.png](/IMAGES/sandbox0.png)
    
2. Choose the preferred **[login type]** > login with your personal credentials

    ![/IMAGES/0image.png](/IMAGES/sandbox0.1.png)

3.	Find the **Meraki Small Business** Sandbox in the list > Click **Reserve** 

    ![/IMAGES/0image.png](/IMAGES/sandbox1.png)

2. Adapt the reservation **schedule** as preferred > click **Reserve**

    ![/IMAGES/0image.png](/IMAGES/sandbox2.png)

3. After clicking “Reserve”, you get redirected to the Sandbox Lab page and receive three emails within a few minutes. 
The emails:
    - **We Are Preparing Your Cisco DevNet Sandbox Lab**: informs you about the currently happening Sandbox setup
    - **Your Cisco DevNet Sandbox Lab is Ready**: indicates the successful sandbox setup 
    - **New Cisco Meraki Administrator Privileges**: prompts you to confirm newly granted administrative privileges to the "Devnet Sandbox" organization. To confirm the privileges, click on the **Confirm your addition to the organization** link in the email > press **Yes** on the page that opens > get redirected to Meraki Dashboard
    ![/IMAGES/0image.png](/IMAGES/sandbox3.png)
    ![/IMAGES/0image.png](/IMAGES/email2.png)


### Obtain Meraki API Key and Network IDs

For the setup of the local CICD repository (see section **Setup Local Repository and Testing**) the Meraki API key and network ID of the reserved Sandbox are required.
    
1. Obtain and note the **Meraki API Key** by following the instructions under https://developer.cisco.com/meraki/api/#!authorization/obtaining-your-meraki-api-key.

2. To obtain and note the **Network ID** execute the following steps: 
    
    2.1 Go to https://developer.cisco.com/meraki/api-v1/#!get-organizations > click **Configuration**
        ![/IMAGES/0image.png](/IMAGES/editor1.png)

    2.2 Add the Meraki Api key from step 1 in the **APIKey in header** field > press **Save**
        ![/IMAGES/0image.png](/IMAGES/editor2.png)

    2.3 Click **Run**   
        ![/IMAGES/0image.png](/IMAGES/editor3.png)
    
    2.4 Find the **"DevNet Sandbox"** name in the output data > make a note of the **id** of this organization
        ![/IMAGES/0image.png](/IMAGES/editor4.png)

    2.5 Go to https://developer.cisco.com/meraki/api-v1/#!get-organization-networks > enter the organization id from the last step in the **Organization Id** field > click **Run**
        ![/IMAGES/0image.png](/IMAGES/editor5.png)

    2.6 Find the network in the output that resembles the following format: **DNSM..-..xxxxxxx....**. It starts with **DNSM** and ends with your email address with masked middle section. > Take a note of the id of this output section. 
        ![/IMAGES/0image.png](/IMAGES/editor6.png)

For the preparation of GitLab (see section **Set Custom Environment Variables in GitLab**) furthermore the Meraki API Key and network ID of a testing and a production network is required. To retrieve this information execute the above steps again with these networks.


### Setup the Local Repository and Testing

This sections applies the Meraki API Key and network ID value of the sandbox, that were identified in the last section. 

In CLI:
1.	Create and activate a virtual environment for the project 
    ```python
    #WINDOWS:
    py -3 -m venv [add name of virtual environment here] 
    source [add name of virtual environment here]/Scripts/activate
    #MAC:
    python3 -m venv [add name of virtual environment here] 
    source [add name of virtual environment here]/bin/activate
    ```

2. Access the created virtual enviroment folder
    ```python
    cd [add name of virtual environment here] 
    ```

3.	Clone this Github repository into the virtual environment folder.
    ```python
    git clone [add github link here]
    ```
    For Github link: 
        In Github, click on the **Clone or download** button in the upper part of the page > click the **copy icon**
        ![/IMAGES/0image.png](/IMAGES/giturl.png)

4. Access the folder **GVE_Devnet_Meraki_CICDPipeline**
    ```python
    cd GVE_Devnet_Meraki_CICDPipeline
    ```

5.	Install dependencies
    ```python
    pip install -r requirements.txt
    ```

6.	Set local environment variables:
    ```python 
    export MERAKI_API_KEY= [add Meraki API key of reserved Meraki sandbox from "Obtain ..." section here]
    export NETWORK= [add network ID of reserved Meraki sandbox from "Obtain ..." section here]
    ```


### Create and Push to New GitLab Environment 

Beside setting up the local repository and testing environment, it is required to pre-configure the remote environment. 

1. In GitLab, go to **Projects** > **Your projects** > click **New project** 

    ![/IMAGES/0image.png](/IMAGES/gitlab1.png)

2. Click **Create blank project** > fill in preferred **[project name]** and other values > click **Create project** 

    ![/IMAGES/0image.png](/IMAGES/gitlab2.png)
    ![/IMAGES/0image.png](/IMAGES/gitlab3.png)

3. Return to the CLI, and execute the commands under the section **Push an existing Git repository** in GitLab

    ![/IMAGES/0image.png](/IMAGES/gitlab4.png)


### Set Custom Environment Variables in GitLab

This sections applies the Meraki API Key and network ID values of the testing and production network, that were identified in the section **Obtain Meraki API Key and Network IDs**. 

1.	In GitLab, go to **Settings** > **CICD** > **Variables** section

    ![/IMAGES/0image.png](/IMAGES/gitlab5.png)

2.	For all following variables do: 
    Click **Add Variable** > Fill in the key and value information, uncheck **protected** checkbox  > click **Add variable**

    ```python
    #Variable 1:
    Key: MERAKI_API_KEY
    Value: [add a Meraki API key in association with production and testing network here]
    Protect Variable: no
    Mask Variable: yes
    
    #Variable 2:
    Key: TESTING_NETWORK
    Value: [add network ID of testing network here]
    Protect Variable: no
    Mask Variable: yes
    
    #Variable 3:
    Key: PRODUCTION_NETWORK
    Value: [add network ID of production network here]
    Protect Variable: no
    Mask Variable: yes
    ```

    ![/IMAGES/0image.png](/IMAGES/gitlab6.png)
    ![/IMAGES/0image.png](/IMAGES/gitlab7.png)

### Create Production Branch in GitLab

In Gitlab, go to **Repository** > **Branches** > **New branch** > fill in the **Branch Name:** **production** (all lower case) > click **Create branch**

![/IMAGES/0image.png](/IMAGES/branch1.png)
![/IMAGES/0image.png](/IMAGES/branch2.png)
![/IMAGES/0image.png](/IMAGES/branch3.png)

### Configure GitLab Runner

GitLab uses GitLab runners to run the code defined in the pipeline definition file **gitlab-ci.yml**.

There are different types of runners available. An overview of the different options is provided in the GitLab documentation: https://gitlab.com/help/ci/runners/README.

Users that use a **self-managed GitLab instance**, can choose the most fitting option based on the documentation link shared above.

**GitLab.com users** can easily enable the shared GitLab runners by: 

1. In GitLab: go to the **Settings** > **CI/CD**.

![/IMAGES/0image.png](/IMAGES/runner1.png)
  
2. In **Runners** section > click **Allow shared runners**

![/IMAGES/0image.png](/IMAGES/runner2.png)


### Log into Dashboards for Local and Remote Testing

Part of the demonstration is to show the configuration value in the different networks before and after the change via CICD pipeline in the Meraki Dashboard. To open the Meraki Dashboard SSID page for the networks: 
    
1.1 Go to https://n40.meraki.com/ and login with your credentials.
    
1.2. For sandbox network: Open the SSID page for the network that resembles the following format: **DNSM..-..xxxxxxx....**. It starts with **DNSM** and ends with your email address with masked middle section. Afterwards, go to [Organization] > [Network] > **Wireless** > **SSIDs** 

1.3 For the other networks: Open the SSID page for the testing and production network in seperate windows or tabs. Therefore, go to [Organization] > [Network] > **Wireless** > **SSIDs** 

### Reset Demo After Execution for Next Run 

After running the demo, it is helpful to prepare it for the next run. Herefore, the following steps are recommended. 

1. Remove the created branch (e.g. configureSSID2) via the following commands: 

    ```python
    git checkout master
    git branch -d [add name of created branch here]
    ```

2. Delete the log files with the name format meraki_api__log_xxxxxxx.log

3. Pull newest changes from remote repository
  
     ```python
    git pull
    ```


## Demo Script

![/IMAGES/0image.png](/IMAGES/mary.png)

Hi, I am Mary, an IT administrator at Springfield Company. Currently, we execute most of our network provisioning and managment tasks manual or with limited automation. Due to a strong growth of our network in the last year, this has become more complex and inefficient. Furthermore, we are having issues with inconsistent configurations.

Fortunately, the Meraki Dashboard API makes it simple to perform these types of operations from a script and thereby enables us to use futher NetDevOps methods like a CICD Pipeline. 

I recently came across the "Meraki CICD Pipeline" sample code in the Cisco DevNet Code Exchange and I decided to give it a try.  

By following the pre-configuration instructions above, I was able to set up a CICD pipeline demo, that works in conjunction with our Meraki Portfolio. The demo covers the creation and merging of a branch for proposed changes and the automatic deployment and testing in two networks – testing and production. Hereby, the changes will only be applied to the production network after successful deployment and testing in the testing network. 

Let’s take a look at how it works in detail. 

### Configuration Values Before

Before we start, I will show you the current configuration of SSID 2 in the Meraki Dashboard of the different enviroments as reference. We come back to the Meraki Dashboard after running our Pipeline to see that the SSID configuration change was successfully applied. 

I already opened the Meraki Dashboard SSID page for all three networks in advance - for local testing, remote testing and production (see section: "Login Dashboards for Local and Remote Testing" for login instructions).

Local testing network: 
![/IMAGES/0image.png](/IMAGES/dashboardLocalBefore.png)

Remote testing network:
![/IMAGES/0image.png](/IMAGES/dashboardLocalBefore3.png)

Remote production network:
![/IMAGES/0image.png](/IMAGES/dashboardLocalBefore2.png)

As you can see SSID 2 is **Unconfigured** in all three Dashboard. (In case SSID 2 is already configured, mention the SSID name before and after the CICD pipeline execution to indicate that the value was changed.)


### Creating a New Branch

Let's now define the configuration we want to apply to SSID 2 via the CICD pipeline.

Herefore, we start by creating a new branch (e.g. configureSSID2) for our proposed changes via CLI and Git. 

    ```python
    git checkout -b [add name of new branch here]
    ```

![/IMAGES/0image.png](/IMAGES/cli1.png)

This command will create a new branch and automatically switch to it. A branch allows us to create our code on top of the master code base without having to be afraid of accidently impacting the master code.   

### Structure of the CICD Project

Before we start with the configuration change, I will shortly explain the structure of this project. Hereby, I already opened the code in an IDE.

The CICD repository is structured as followed:
* **config_ssid.json:** file with configuration values for wireless SSID
* **app.py:** script that executes the SSID update based on the configuration values
* **test.py:** script that executes junit test cases
* **gitlab-ci-yml:** CICD pipeline configuration file
* **requirements.txt:** contains all libs we need to install for our scripts
* **.gitignore:** prevents log files to be pushed to the repository

![/IMAGES/0image.png](/IMAGES/project.png)

### Changing the Configured SSID Name

As mentioned, I want to demonstrate the configuration of SSID 2 by using our CICD Pipeline. The configuration values that will be applied by the pipeline are stored in the **config_ssid.json** file. Let's furthermore change the name value to **New SSID Name** now to recognize our configuration more easily afterwards.

Instead of using this demo to configure a unconfigured SSID, we could also use it to change an existing configuration. Hereby, we would just need to change one or more values of the **config_ssid.json** . 

![/IMAGES/0image.png](/IMAGES/project2.png)

### Testing Locally

Before I push this change to the remote repository and thereby trigger the CICD pipeline, I want to test it locally. Herefore, I use a Cisco Meraki Sandbox, which I reserved in advance. I did also set the Meraki API key and network ID of the sandbox network as environement variables in my virtual environment.

The demo scripts will access these environment variables as needed. The Python scripts are the same throughout the pipeline. Only the environment variables differ depending on the pipeline stage and therefore cause the deployment and testing in different networks.

To apply the network change, I need to run the **app.py** with the following command in the CLI:
```python
python app.py
```
To run the testing script I simple execute the following command:
```python
python -m unittest test.Testing
```

In the output, we can then see that the deployment was executed and the test cases ran successfully.

![/IMAGES/0image.png](/IMAGES/cli1.2.png)

Let's also check the name in my Sandbox network via the Meraki Dashboard. 

![/IMAGES/0image.png](/IMAGES/dashboardLocalBefore4.png)

As we can see, the SSID 2 is configured and the name is **New SSID Name**. 

Since our test was successful, we can transfer our changes to the remote repository now. Therefore, we use the following CLI commands:

```python
git add config_ssid.json
git commit -m "[add custom comment here]"
git push --set-upstream origin [add name of proposed branch here]
```

![/IMAGES/0image.png](/IMAGES/cli2.png)

# Merge Proposed Changes into Master Branch

After pushing the proposed branch, it is available in our remote repository in GitLab. However, it is still seperate from the master code. 

To merge the branch into the master branch and thereby trigger the CICD pipeline, we create a merge request.

Herefore, we go to **Merge Requests** > **New Merge Request**. 

![/IMAGES/0image.png](/IMAGES/mergeintomaster0.png)

Then we choose the source branch **configureSSID2** and destination branch **master** for our request and click **Compare branches and continue**. 
In case you don't see a page, similar to the next picture, after clicking **New Merge Request**, check in the upper part of the page if a **"From configureSSID2 into master"** string is displayed. If the string contains different branches click the **Change branches** link next to the string.

![/IMAGES/0image.png](/IMAGES/mergeintomaster.png)
![/IMAGES/0image.png](/IMAGES/mergeintomaster0.2.png)

Since this is an demo, we only fill in the **Titel** field and click **Submit merge request**. Still, if you work in a developer team it is highly recommended to provide further information about your request by filling in more fields.

![/IMAGES/0image.png](/IMAGES/mergeintomaster2.png)

Usually one or more of your team members could check your merge request and trigger the merge by clicking **Merge** on this page. Again, since this is a demo, I will trigger the merge myself.

![/IMAGES/0image.png](/IMAGES/mergeintomaster3.png)


# Deployment and Testing in Testing Network

After the merge, the pipeline automatically starts to deploy and test the changes in the testing network.

We can see the stages of our pipeline on the **CI/CD** page. 

![/IMAGES/0image.png](/IMAGES/pipeline1.png)

This page does not only show us the status of our pipeline and stages but also allows us to access detailed information on each step of a stage. 
To view stage details, I simply click the **circle icon** in the **Stages** column. The first circle corresponds to the deployment stage, the second to the testing stage. 

![/IMAGES/0image.png](/IMAGES/pipeline2.png)

As you can see in the stage details, the GitLab Runner starts the deployment by spinning up a docker container with python 3.7 image. In this container it then installs all dependencies we specified in the requirements.txt. To set the environment variables for our container it accesses the corresponding GitLab custom environment variables (MERAKI_API_KEY and TESTING_NETWORK), which we did set via the GitLab UI in advance.
Last but not least, it executes our **app.py** script. 
All steps are defined in the **gitlab-ci.yml** file and are similar for all stages. Only the environment variable and script to execute, changes depending on the environment (testing, production) and stage (deployment, testing).

As we can see in the last line on the details view, the deployment finished successfully. 

![/IMAGES/0image.png](/IMAGES/gitlab8.png)

Let's go back to the **CICD** view and check the second stage by clicking the second circle.

![/IMAGES/0image.png](/IMAGES/pipeline3.png)

As mentioned, the steps in this stage are quite similar to the first stage. Only this time we execute the **test.py** instead of the **app.py** script and thereby start the junit tests. 

![/IMAGES/0image.png](/IMAGES/gitlab9.png)

As we can see in the output, both test cases ran successfully. 

At this point, we successfully deployed and tested our configuration change in the testing network. Let's check the SSID configuration in the Meraki Dashboard. 

![/IMAGES/0image.png](/IMAGES/dashboardaftertesting.png)

As we can see, the SSID 2 is configured and the name is **New SSID Name** in the testing network, too.


# Merge Proposed Changes into Production Branch

The configuration change was successfully deployed and tested in the local and remote testing enviroment. Thereby, we can trigger the deployment in the production environment now by creating a merge request again. 

Herefore, we go again to **Merge Requests**>**New Merge Request**. We choose the source branch **master** and destination branch **production** for our request and click **Compare branches and continue**. 

![/IMAGES/0image.png](/IMAGES/pipeline4.png)

Again, we fill in the **titel** field > click **Submit merge request** > **Merge**.

![/IMAGES/0image.png](/IMAGES/pipeline5.png)
![/IMAGES/0image.png](/IMAGES/pipeline6.png)

# Deployment and Testing in Production Network

As we can see on the **CICD** page, the second part of the pipeline already started after we merged the changes in the production branch. 

![/IMAGES/0image.png](/IMAGES/pipeline1.png)

The difference this time is, that the systems furthermore waits for a manually trigger to deploy the changes. Latter is an optional functionallity we can add as part of the pipeline. It can be useful, if you prefer to deploy changes only at planned times frames.

We manually trigger the deployment and testing in the production environment by clicking on the **circle** and **play** icon. 

![/IMAGES/0image.png](/IMAGES/pipeline7.png)

Afterwards, the stages excute the same tasks as we saw before - only the environment they are applied in differs due to different environment variables.  

Let us shortly wait for the stages to finish...

![/IMAGES/0image.png](/IMAGES/pipeline8.png)

Now we can check the change in the Meraki Dashboard for the production network. 

![/IMAGES/0image.png](/IMAGES/dashboardprodafter.png)

As we can see, the SSID 2 is configured and the name is **New SSID Name** in the production network, too.
 
We successfully changed the SSID of a Meraki Device by using a CICD pipeline and Meraki APIs!



### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)



### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)



### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)



#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.