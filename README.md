# refstack-client-infrared-plugin

## About
It's an ansible playbook for running [refstack-client](https://github.com/openstack/refstack-client).
It can be useful in automation where this role can be included in other playbooks.
The role is importable to [Infrared](https://github.com/redhat-openstack/infrared.git) as an infrared
plugin, so right after Infrared deploys an environment, this role can be executed to ensure the
deployment is working by passing refstack tests.

## Required Role Variables
| Variable name                | Required | Default                                                             | Type   | Description                                                                      |
|------------------------------|----------|---------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------|
| private_key_path             | True if upload_results is True    | None                                       | String | Results are uploaded to the corresponding account.                                                      |
| source_admin_credentials     | only if accounts_path not defined | None                                       | String | File or command to be sourced for admin credentials.                                                    |
| source_credentials           | True     | None                                                                | String | File or command to be sourced: keystonerc_admin/openrc admin admin.                                     |

## Optional Role Variables

| Variable name                | Required | Default                                                             | Type   | Description                                                                      |
|------------------------------|----------|---------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------|
| accounts_path                | False    | None                                                                | String | Path to a tempest accounts file.                                                                        |
| additional_tempestconf_params| False    | None                                                                | String | Additional arguments to passed to discover-tempest-config tool.                                         |
| deployer_input               | False    | None                                                                | String | Pat to a deployer input file.                                                                           |
| dest_dir *                   | False    | pwd                                                                 | String | Local directory where the files will be stored.                                                         |
| download_artifacts           | False    | True                                                                | Bool   | Whether artifacts should be downloaded to the host or not.                                              |
| guideline                    | False    | 2019.06                                                             | String | Specific guideline                                                                                      |
| private_key_path_src *       | False    | None                                                                | String | If defined, the key defined by the param is copied to the targeted machine to private_key_path location.|
| refstack_client_source       | False    | ~/.refstack-client                                                  | String | Destination where refstack-client will be cloned.                                                       |
| server                       | False    | https://refstack.openstack.org/api                                  | String | Server url where results will be uploaded.                                                              |
| tempest_config_path          | False    | None                                                                | String | Destination of tempest configuration file to be used for running refstack tests.                        |
| tempest_tag                  | False    | refstack-client's default                                           | String | Tempest will be cloned and checkouted to this specific tag.                                             |
| test_list                    | False    | None                                                                | String | A path or an URL to a test list text file containing specific test cases.                               |
| upload_results               | False    | True                                                                | Bool   | Whether results should be uploaded to a server or not.                                                  |
| url_cirros_image             | False    | http://download.cirros-cloud.net/0.4.0/cirros-0.4.0-x86_64-disk.img | String | Path or link to cirros image.                                                                           |

**\* it's a local path, the path on a machine, the playbook is executed from**

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
    source_admin_credentials: ~/overcloudrc_admin
    private_key_path: ~/.ssh/id_rsa
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

### Example
```
(infrared)$ ir refstack-client-ansible-role \
                 --source_credentials /home/stack/overcloudrc \
                 --source_admin_credentials /home/stack/overcloudrc \
                 --deployer_input /home/stack/ir-tempest-deployer-input.conf \
                 --private_key_path /home/stack/refstack_key \
                 --private_key_path_src $(pwd)/refstack_key
```

In the example above `tempest_config_path` is not defined, so `source_admin_credentials` are a required parameter
because the role will try to generate an `accounts.yaml` before generating a `tempest.conf`.
