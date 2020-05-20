---
# This file and main.yml are required by Infrared project
config:
  plugin_type: test
  entry_point: main.yml
  roles_path: ../
subparsers:
  refstack-client-ansible-role:
    description: OpenStack interoperability tests
    include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
    groups:
      - title: OpenStack Interoperability Tests
        options:
          accounts_path:
            type: Value
            help: |
              Path to a tempest accounts file.
          additional_tempestconf_params:
            type: Value
            help: |
              Additional parameters to be passed to discover-tempest-config tool.
          deployer_input:
            type: Value
            help: |
              Path to a deployer-input file.
          dest_dir:
            type: Value
            help: |
              Local directory where the files will be     stored.
          download_artifacts:
            type: Bool
            help: |
              Whether artifacts should be downloaded to the host machine or not.
          guideline:
            type: Value
            help: |
              Specific guideline.
          private_key_path:
            type: Value
            help: |
              If defined, results will be uploaded to the corresponding account.
          private_key_path_src:
            type: Value
            help: |
              If defined, the key is copied to the targeted machine to private_key_path location.
          refstack_client_source:
            type: Value
            help: |
              Destination where refstack-client will be cloned.
          server:
            type: Value
            help: |
              Server url where results will be uploaded.
          source_credentials:
            type: Value
            help: |
              File or command to be sourced: keystonerc_admin/openrc admin admin.
          source_admin_credentials:
            type: Value
            help: |
              File or command to be sourced: keystonerc_admin/openrc admin admin.
          tempest_config_path:
            type: Value
            help: |
              Destination of tempest configuration file to be used for running refstack tests.
          tempest_tag:
            type: Value
            help: |
              Tempest will be cloned and checkouted to this specific tag.
          test_list:
            type: Value
            help: |
              A path or an URL to a test list text file containing specific test cases.
          upload_results:
            type: Bool
            help: |
              Whether results should be uploaded to a server or not.
          url_cirros_image:
            type: Value
            help: |
              Path or link to cirros image.
