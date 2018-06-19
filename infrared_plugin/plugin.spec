---
plugin_type: test
subparsers:
    refstack-client-ansible-role:
        description: OpenStack interoperability tests
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: OpenStack Interoperability Tests
              options:
                aditional_tempestconf_params:
                    type: Value
                    help: |
                      Additional parameters to be passed to discover-tempest-config tool.
                    default: ''
                deployer_input:
                    type: Value
                    help: |
                      Path to a deployer-input file.
                    default: ''
                url_cirros_image:
                    type: Value
                    help: |
                      Path or link to cirros image.
                    default: http://download.cirros-cloud.net/0.3.5/cirros-0.3.5-x86_64-disk.img
                source_credentials:
                    type: Value
                    help: |
                      File or command to be sourced: keystonerc_admin/openrc admin admin.
                    default: ''
                private_key_path:
                    type: Value
                    help: |
                      If defined, results will be uploaded to the corresponding account.
                    default: ''
                private_key_path_src:
                    type: Value
                    help: |
                      If defined, the key is copied to the targeted machine to private_key_path location.
                    default: ''
                refstack_client_source:
                    type: Value
                    help: |
                      Destination where refstack-client will be cloned.
                    default: ~/refstack-client
                server:
                    type: Value
                    help: |
                      Server url where results will be uploaded.
                    default: https://refstack.openstack.org/api
                tempestconf_source:
                    type: Value
                    help: |
                      Destination where python-tempestconf will be cloned.
                    default: ~/python-tempestconf-job
                tempestconf_venv:
                    type: Value
                    help: |
                      Destination of virtualenv where python-tempestconf will be installed.
                    default: ~/.python-tempestconf-job_venv
                tempest_config_path:
                    type: Value
                    help: |
                      Destination of tempest configuration file to be used for running refstack tests.
                    default: ''
                test_list:
                    type: Value
                    help: |
                      A path or an URL to a test list text file containing specific test cases.
                    default: ''
                upload_results:
                    type: Bool
                    help: |
                      Whether results should be uploaded to a server or not.
                    default: True
                download_artifacts:
                    type: Bool
                    help: |
                      Whether artifacts should be downloaded to the host machine or not.
                    default: True
