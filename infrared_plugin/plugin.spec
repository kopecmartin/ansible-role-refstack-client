---
plugin_type: test
subparsers:
    refstack-client-ansible-role:
        description: OpenStack interoperability tests
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: OpenStack Interoperability Tests
              options:
                url_cirros_image:
                    type: Value
                    help: |
                      Path or link to cirros image.
                    default: http://download.cirros-cloud.net/0.3.5/cirros-0.3.5-x86_64-disk.img
                source_credentials:
                    type: Value
                    help: |
                      File or command to be sourced: keystonerc_admin/openrc admin admin.
                    default: None
                refstack_client_source:
                    type: Value
                    help: |
                      Destination where refstack-client will be cloned.
                    default: ~/refstack-client
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
                    default: None
                test_list:
                    type: Value
                    help: |
                      A path or an URL to a test list text file containing specific test cases.
                    default: None
