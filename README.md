# refstack-client-infrared-plugin

## About
It's an ansible playbook for running [refstack-client](https://github.com/openstack/refstack-client).
It can be useful in automation where this role can be for example included in other playbooks.
The role is importable to [Infrared](https://github.com/redhat-openstack/infrared.git) as an infrared
plugin, so right after Infrared deploys the environment, this role can be executed to ensure the
deployment is working by passing refstack tests.

## Role Variables

| Variable name                | Required | Default                                                             | Type    | Description                                                                     |
|------------------------------|----------|---------------------------------------------------------------------|---------|---------------------------------------------------------------------------------|
| aditional_tempestconf_params | False    | None                                                                | String  | Aditional arguments to passed to discover-tempest-config tool.                  |
| deployer_input               | False    | None                                                                | String  | Pat to a deployer input file.                                                   |
| url_cirros_image             | False    | http://download.cirros-cloud.net/0.3.5/cirros-0.3.5-x86_64-disk.img | String  | Path or link to cirros image.                                                   |
| source_credentials           | True     | None                                                                | String  | File or command to be sourced: keystonerc_admin/openrc admin admin.             |
| private_key_path             | False    | None                                                                | String  | If defined, results will be uploaded to the corresponding account.              |
| refstack_client_source       | False    | ~/.refstack-client                                                  | String  | Destination where refstack-client will be cloned.                               |
| server                       | False    | https://refstack.openstack.org/api                                  | String  | Server url where results will be uploaded.                                      |
| tempestconf_source           | False    | ~/.python-tempestconf                                               | String  | Destination where python-tempestconf will be cloned.                            |
| tempestconf_venv             | False    | ~/.python-tempestconf/job_venv                                      | String  | Destination of virtualenv where python-tempestconf will be installed.           |
| tempest_config_path          | False    | None                                                                | String  | Destination of tempest configuration file to be used for running refstack tests.|
| test_list                    | False    | None                                                                | String  | A path or an URL to a test list text file containing specific test cases.       |
| upload_results               | False    | True                                                                | Bool    | Whether results should be uploaded to a server or not.                          |

## Example
To run the role from the repository:
```
$ git clone https://github.com/kopecmartin/refstack-client-ansible-role.git
$ cd refstack-client-ansible-role
$ mkdir roles && ln -s $(pwd) roles/refstack-client-ansible-role
```
Then create a `playbook.yaml`:
```
---
- hosts: localhost
  vars:
    source_credentials: ~/overcloudrc
  roles:
    - refstack-client-ansible-role
```
And run it:
```
$ ansible-playbook playbook.yaml
```


## Usage with Infrared

Run the following steps to run the plugin:
1. Install infrared and add refstack-client-ansible-role plugin by providing the url to this repo:
    ```
    (infrared)$ ir plugin add https://github.com/kopecmartin/refstack-client-ansible-role.git --src-path infrared_plugin
    ```
2. You can verify that the plugin is imported by:
    ```
    (infrared)$ ir plugin list
    ```
3. From infrared directory symlink roles path:
    ```
    $ ln -s $(pwd)/plugins $(pwd)/plugins/refstack-client-ansible-role/infrared_plugin/roles
    ```
4. Run the plugin:
    ```
    (infrared)$ ir refstack-client-ansible-role
    ```
