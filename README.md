# Getting started with Azure Machine Learning

[![License: MIT](https://img.shields.io/badge/License-MIT-2D677F.svg?style=flat)](https://opensource.org/licenses/MIT)

## UCL Data science hackathon 
- [Getting started with Azure Machine Learning](#getting-started-with-azure-machine-learning)
  - [UCL Data science hackathon](#ucl-data-science-hackathon)
  - [🛠 Setup Steps](#%f0%9f%9b%a0-setup-steps)
    - [1. Create an Azure account 👉🏼 here](#1-create-an-azure-account-%f0%9f%91%89%f0%9f%8f%bc-here)
    - [2. Make sure to redeem your $100 pass as described in the intro session](#2-make-sure-to-redeem-your-100-pass-as-described-in-the-intro-session)
    - [3. Create Azure Machine Learninge Resources with the Deploy to Azure Button below](#3-create-azure-machine-learninge-resources-with-the-deploy-to-azure-button-below)
    - [4. Create Additional Resources Needed](#4-create-additional-resources-needed)
      - [Create Compute Targets](#create-compute-targets)
      - [Optional Kuberetes Cluster](#optional-kuberetes-cluster)
  - [📖 Content](#%f0%9f%93%96-content)
    - [🔖 Intro to Azure Machine Learning service](#%f0%9f%94%96-intro-to-azure-machine-learning-service)
    - [☁ Deploying to the cloud](#%e2%98%81-deploying-to-the-cloud)
    - [⚡️ Advanced experimentation techniques in AML](#%e2%9a%a1%ef%b8%8f-advanced-experimentation-techniques-in-aml)
  - [📄 License](#%f0%9f%93%84-license)
  - [🙏🏼 Acknowledgments](#%f0%9f%99%8f%f0%9f%8f%bc-acknowledgments)

## 🛠 Setup Steps

### 1. Create an Azure account 👉🏼 [here](https://azure.microsoft.com/en-us/free/?WT.mc_id=amldemo-github-trallard)

### 2. Make sure to redeem your $100 pass as described in the intro session

### 3. Create Azure Machine Learninge Resources with the Deploy to Azure Button below
<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fcassieview%2Fignite-learning-paths-training-aiml%2Fmaster%2Faiml30%2Fdeploy.json" rel="nofollow">
 <img src="https://camo.githubusercontent.com/9285dd3998997a0835869065bb15e5d500475034/687474703a2f2f617a7572656465706c6f792e6e65742f6465706c6f79627574746f6e2e706e67" data-canonical-src="http://azuredeploy.net/deploybutton.png" style="max-width:100%;">
</a>

### 4. Create Additional Resources Needed
Once you have created the base Azure Machine Learning Service Workspace we need to add additional compute resources.

#### Create Compute Targets
*  Create `Machine Learning Compute`
    * Click on the nav `Compute`
    * Click `New`
    * Enter a name for the resource
    * Select `Machine Learning Compute` from the dropdown
    * Select the machine size
    * Enter the min and max nodes (recommend min of 0 and max of 5)
    * Click `Create`
    ![Create Compute](https://globaleventcdn.blob.core.windows.net/assets/aiml/aiml30/CreateMlCompute.gif)

* Create Notebook Virtual Machine
    * Click on the `Notebook VM` nav
    * Click `New`
    * Give the notebook a unique name
    * Select the VM size (NC6 is always good)
    * Click `Create`
    ![Create VM](https://globaleventcdn.blob.core.windows.net/assets/aiml/aiml30/CreateNotebookVM.gif)

#### Optional Kuberetes Cluster
* Create Kubernetes Compute
    * Click on the nav `Compute`
    * Click `New`
    * Enter a name for the resource
    * Select `Kubernetes Service` from the dropdown
    * Click `Create`
    ![Create Kubernetes](https://globaleventcdn.blob.core.windows.net/assets/aiml/aiml30/CreateKubService.gif)

##  📖 Content

### 🔖  Intro to Azure Machine Learning service

This demo introduce attendees to the basics of Azure Machine Learning service. Concepts such as a workspace, compute environment, data stores, experiments, etc. will be introduced in preparation for a machine learning experiment in the cloud.

Intro to Azure Machine Learning service
Logical Layout vs Physical Resources
Tour through Datasources, Compute, Experiments etc

The goal of this demo is to create an Azure Machine Learning (AML) workspace and compute environment in order to run an experiment in the cloud. 

:sparkles: Check the demo 👉🏼 [here](./digits-cloudrun)

### ☁ Deploying to the cloud

This demo focuses on creating a model that can be deployed and later accessed through an endpoint.  This builds on the previous demo created and is ultimately deployed in as an Azure Container instance.

:sparkles: Check the demo 👉🏼 [here](./digits-cloud-deploy)


### ⚡️ Advanced experimentation techniques in AML

These demos focus on advanced techniques available for experimentation in Azure Machine Learning service: hyperparameter tuning, automatic machine learning.

These features are designed to create agility in the data science process by automating several repetitive tasks associated with starting a new project.

:sparkles:  Check the hyperparameters demo 👉🏼 [here](./hyperparameters)

:sparkles: Check the automl demo 👉🏼 [here](./automl-digits)

## 📄 License
This work is licensed under the [MIT OSI license](https://opensource.org/licenses/MIT).

## 🙏🏼 Acknowledgments

The demos were deeply inspired and adapted from previous work done by Seth Juarez and Cassie Brevieu ([cloud-scale](https://github.com/cloudscaleml)).