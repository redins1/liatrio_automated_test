# CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Configuration
 * Running
 * Maintainers


## INTRODUCTION
------------

The liatrio automated test project is to validate the node js application is accessible and returns the expected data. This project
uses a jenkins build to manually run a pytest script using a URL variable since the Load Balancer DNS is dynamically created.  
Link to my Jenkins instance: http://3.231.42.49:8080/  


## REQUIREMENTS
------------
* A running node js application with an accessible URL (to get a successful test). 

* In a personal development instance on centos install the required software 
for both your personal and jenkins user (once Jenkins is installed):   
### Jenkins  
* **Version:** 2.319.2  
* **Plug-ins:**  

| Name         | Version|
|--------------|:-----:|
| Amazon ECR plugin (amazon-ecr) | 1.7|
| Amazon Web Services SDK :: EC2 (aws-java-sdk-ec2) | 1.12.131-302.vbef9650c6521|
| Amazon Web Services SDK :: ECR (aws-java-sdk-ecr) | 1.12.131-302.vbef9650c6521|
| Amazon Web Services SDK :: Minimal (aws-java-sdk-minimal) | 1.12.131-302.vbef9650c6521|
| Ant Plugin (ant) | 1.13|
| Apache HttpComponents Client 4.x API Plugin (apache-httpcomponents-client-4-api) | 4.5.13-1.0|
| Authentication Tokens API Plugin (authentication-tokens) | 1.4|
| Autofavorite for Blue Ocean (blueocean-autofavorite) | 1.2.4|
| Bitbucket Branch Source Plugin (cloudbees-bitbucket-branch-source) | 751.vda_24678a_f781|
| Bitbucket Pipeline for Blue Ocean (blueocean-bitbucket-pipeline) | 1.25.2|
| Blue Ocean (blueocean) | 1.25.2|
| Blue Ocean Core JS (blueocean-core-js) | 1.25.2|
| Blue Ocean Pipeline Editor (blueocean-pipeline-editor) | 1.25.2|
| Bootstrap 4 API Plugin (bootstrap4-api) | 4.6.0-3|
| Bootstrap 5 API Plugin (bootstrap5-api) | 5.1.3-4|
| Branch API Plugin (branch-api) | 2.7.0|
| Build Timeout (build-timeout) | 1.20|
| Caffeine API Plugin (caffeine-api) | 2.9.2-29.v717aac953ff3|
| Checks API plugin (checks-api) | 1.7.2|
| CloudBees AWS Credentials Plugin (aws-credentials) | 1.33|
| CloudBees Docker Build and Publish plugin (docker-build-publish) | 1.3.3|
| Command Agent Launcher Plugin (command-launcher) | 1.6|
| Common API for Blue Ocean (blueocean-commons) | 1.25.2|
| Config API for Blue Ocean (blueocean-config) | 1.25.2|
| Credentials Binding Plugin (credentials-binding) | 1.27.1|
| Credentials Plugin (credentials) | 1074.v60e6c29b_b_44b_|
| Dashboard for Blue Ocean (blueocean-dashboard) | 1.25.2|
| Design Language (jenkins-design-language) | 1.25.2|
| Display URL API (display-url-api) | 2.3.5|
| Display URL for Blue Ocean (blueocean-display-url) | 2.4.1|
| Docker API Plugin (docker-java-api) | 3.1.5.2|
| Docker Commons Plugin (docker-commons) | 1.18|
| Docker Pipeline (docker-workflow) | 1.27|
| Docker plugin (docker-plugin) | 1.2.6|
| Durable Task Plugin (durable-task) | 493.v195aefbb0ff2|
| ECharts API Plugin (echarts-api) | 5.2.2-2|
| Email Extension Plugin (email-ext) | 2.86|
| Events API for Blue Ocean (blueocean-events) | 1.25.2|
| Favorite (favorite) | 2.3.3|
| Folders Plugin (cloudbees-folder) | 6.17|
| Font Awesome API Plugin (font-awesome-api) | 5.15.4-5|
| GIT server Plugin (git-server) | 1.10|
| Git Pipeline for Blue Ocean (blueocean-git-pipeline) | 1.25.2|
| Git client plugin (git-client) | 3.11.0|
| Git plugin (git) | 4.10.3|
| GitHub API Plugin (github-api) | 1.301-378.v9807bd746da5|
| GitHub Branch Source Plugin (github-branch-source) | 2.11.4|
| GitHub Pipeline for Blue Ocean (blueocean-github-pipeline) | 1.25.2|
| GitHub plugin (github) | 1.34.1|
| Gradle Plugin (gradle) | 1.38|
| HTML Publisher plugin (htmlpublisher) | 1.28|
| Handy Uri Templates 2.x API Plugin (handy-uri-templates-2-api) | 2.1.8-1.0|
| JQuery3 API Plugin (jquery3-api) | 3.6.0-2|
| JSch dependency plugin (jsch) | 0.1.55.2|
| JUnit Plugin (junit) | 1.53|
| JWT for Blue Ocean (blueocean-jwt) | 1.25.2|
| Jackson 2 API Plugin (jackson2-api) | 2.13.1-246.va8a9f3eaf46a|
| Java JSON Web Token (JJWT) Plugin (jjwt-api) | 0.11.2-9.c8b45b8bb173|
| JavaBeans Activation Framework (JAF) API (javax-activation-api) | 1.2.0-2|
| JavaMail API (javax-mail-api) | 1.6.2-5|
| JavaScript GUI Lib: ACE Editor bundle plugin (ace-editor) | 1.1|
| JavaScript GUI Lib: Handlebars bundle plugin (handlebars) | 3.0.8|
| JavaScript GUI Lib: Moment.js bundle plugin (momentjs) | 1.1.1|
| Kubernetes CLI Plugin (kubernetes-cli) | 1.10.3|
| Kubernetes Client API Plugin (kubernetes-client-api) | 5.11.2-182.v0f1cf4c5904e|
| Kubernetes Credentials Plugin (kubernetes-credentials) | 0.9.0|
| Kubernetes plugin (kubernetes) | 1.31.3|
| LDAP Plugin (ldap) | 2.7|
| Lockable Resources plugin (lockable-resources) | 2.13|
| Mailer Plugin (mailer) | 408.vd726a_1130320|
| Matrix Authorization Strategy Plugin (matrix-auth) | 3.0|
| Matrix Project Plugin (matrix-project) | 1.20|
| Metrics Plugin (metrics) | 4.0.2.8.1|
| OWASP Markup Formatter Plugin (antisamy-markup-formatter) | 2.7|
| OkHttp Plugin (okhttp-api) | 4.9.3-105.vb96869f8ac3a|
| Oracle Java SE Development Kit Installer Plugin (jdk-tool) | 1.5|
| PAM Authentication plugin (pam-auth) | 1.6.1|
| Personalization for Blue Ocean (blueocean-personalization) | 1.25.2|
| Pipeline (workflow-aggregator) | 2.6|
| Pipeline Graph Analysis Plugin (pipeline-graph-analysis) | 188.v3a01e7973f2c|
| Pipeline SCM API for Blue Ocean (blueocean-pipeline-scm-api) | 1.25.2|
| Pipeline implementation for Blue Ocean (blueocean-pipeline-api-impl) | 1.25.2|
| Pipeline: API (workflow-api) | 1122.v7a_916f363c86|
| Pipeline: Basic Steps (workflow-basic-steps) | 2.24|
| Pipeline: Build Step (pipeline-build-step) | 2.15|
| Pipeline: Declarative (pipeline-model-definition) | 1.9.3|
| Pipeline: Declarative Extension Points API (pipeline-model-extensions) | 1.9.3|
| Pipeline: GitHub Groovy Libraries (pipeline-github-lib) | 1.0|
| Pipeline: Groovy (workflow-cps) | 2648.va9433432b33c|
| Pipeline: Input Step (pipeline-input-step) | 427.va6441fa17010|
| Pipeline: Job (workflow-job) | 1145.v7f2433caa07f|
| Pipeline: Milestone Step (pipeline-milestone-step) | 1.3.2|
| Pipeline: Model API (pipeline-model-api) | 1.9.3|
| Pipeline: Multibranch (workflow-multibranch) | 706.vd43c65dec013|
| Pipeline: Nodes and Processes (workflow-durable-task-step) | 1121.va_65b_d2701486|
| Pipeline: REST API Plugin (pipeline-rest-api) | 2.20|
| Pipeline: SCM Step (workflow-scm-step) | 2.13|
| Pipeline: Shared Groovy Libraries (workflow-cps-global-lib) | 552.vd9cc05b8a2e1|
| Pipeline: Stage Step (pipeline-stage-step) | 291.vf0a8a7aeeb50|
| Pipeline: Stage Tags Metadata (pipeline-stage-tags-metadata) | 1.9.3|
| Pipeline: Stage View Plugin (pipeline-stage-view) | 2.20|
| Pipeline: Step API (workflow-step-api) | 622.vb_8e7c15b_c95a_|
| Pipeline: Supporting APIs (workflow-support) | 813.vb_d7c3d2984a_0|
| Plain Credentials Plugin (plain-credentials) | 1.7|
| Plugin Utilities API Plugin (plugin-util-api) | 2.12.0|
| Popper.js 2 API Plugin (popper2-api) | 2.11.2-1|
| Popper.js API Plugin (popper-api) | 1.16.1-2|
| Pub-Sub "light" Bus (pubsub-light) | 1.16|
| REST API for Blue Ocean (blueocean-rest) | 1.25.2|
| REST Implementation for Blue Ocean (blueocean-rest-impl) | 1.25.2|
| Resource Disposer Plugin (resource-disposer) | 0.17|
| SCM API Plugin (scm-api) | 595.vd5a_df5eb_0e39|
| SSH Build Agents plugin (ssh-slaves) | 1.33.0|
| SSH Credentials Plugin (ssh-credentials) | 1.19|
| SSH server (sshd) | 3.1.0|
| Script Security Plugin (script-security) | 1131.v8b_b_5eda_c328e|
| Server Sent Events (SSE) Gateway Plugin (sse-gateway) | 1.24|
| Snakeyaml API Plugin (snakeyaml-api) | 1.29.1|
| Structs Plugin (structs) | 308.v852b473a2b8c|
| Terraform Plugin (terraform) | 1.0.10|
| Timestamper (timestamper) | 1.16|
| Token Macro Plugin (token-macro) | 267.vcdaea6462991|
| Trilead API Plugin (trilead-api) | 1.0.13|
| Variant Plugin (variant) | 1.4|
| Web for Blue Ocean (blueocean-web) | 1.25.2|
| Workspace Cleanup Plugin (ws-cleanup) | 0.40|
| bouncycastle API Plugin (bouncycastle-api) | 2.25|
| docker-build-step (docker-build-step) | 2.8|
| i18n for Blue Ocean (blueocean-i18n) | 1.25.2|
### python
* **Version:** 3.6 
* **Modules:** 

| Name         | Version|
|--------------|:-----:|
| pytest | 6.2.5 |
| pip | 21.3.1 |
| pytest-metadata | 1.11.0 |
| python-dateutil | 2.8.2 |
| requests | 2.27.1 |
| pytest-html | 3.1.1 |
| jsonschema | 3.2.0 |


## INSTALLATION
------------

Create a Jenkins pipeline to read the Jenkinsfile from the github repo on the correct branch.
Also, check the "Do not allow concurrent builds" and "GitHub project" checkboxes.  
Fill in the required info for the "GitHub project" check box.  


## CONFIGURATION
-------------

Configurable parameter:
 * String parameter in Jenkins to input the newly created URL of your application.  

## RUNNING
-------
Click on the newly created Jenkins job, click "Build now" or "Build with parameters"  

## MAINTAINERS
-----------

 * Philip Snider (https://github.com/redins1)
