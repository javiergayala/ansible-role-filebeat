# Ansible Role: Filebeat

[![Build Status](https://travis-ci.org/javiergayala/ansible-role-filebeat.svg?branch=master)](https://travis-ci.org/javiergayala/ansible-role-filebeat) ![Ansible Role](https://img.shields.io/ansible/role/24920)

Installs Filebeat on RedHat/CentOS.

This role installs and configures the latest version of Filebeat (6.x) from the official [Elastic.co](https://www.elastic.co/) [Repo](https://www.elastic.co/guide/en/elasticsearch/reference/current/rpm.html#rpm-repo).

## Requirements

None.

## Role Variables

### Default values (see `defaults/main.yml`):

```yaml
es_major_version: "6.x"
```

The version of Filebeat should always match the verion of Elasticsearch in your ELK stack.  This represents the major version of Elasticsearch.

```yaml
es_use_repository: undefined
```

This value is not defined anywhere in the role.  I have documented it here because it is a value usually defined in the [elastic.elasticsearch](https://github.com/elastic/ansible-elasticsearch) role by [Elastic.co](https://www.elastic.co/).  If you are installing this Filebeat role alongside the `elastic.elasticsearch` role, then that role will typically install the repository for you.  Allowing this Filebeat role to also install the repository will slightly alter the repo file which leads to the role no longer producing an idempotent result.  However, if you tell the `elastic.elasticsearch` role NOT to install the repository, then this Filebeat role *will* install the repository in order to access the software.

```yaml
es_version: "6.2.3"
```

The full version number of Elasticsearch/Filebeat.

```yaml
filebeat_create_config: "true"
```

Whether or not to allow the role to create the Filebeat configuration file.  

```yaml
filebeat_enabled: "yes"
```

This defines whether the filebeat service should be enabled at boot.

```yaml
filebeat_repo_key: 'https://artifacts.elastic.co/GPG-KEY-elasticsearch'
```

The URL to the PGP key used for the [Elastic.co](https://www.elastic.co/) respository.

```yaml
filebeat_run_state: started
```

This defines whether the filebeat service should be started.

```yaml
filebeat_config_content:
  filebeat.prospectors:
    - type: log
      enabled: "true"
      paths:
        - "/var/log/*.log"
  filebeat.config.modules:
    reload.enabled: "false"
    path: "{{ filebeat_modules_dir }}/*.yml"
  setup.template.settings:
    index.number_of_shards: 3
  output.elasticsearch:
    hosts:
      - "localhost:9200"
```

The `filebeat_config_content` variable is a dictionary that contains the basic configuration of Filebeat.  The value of this variable will be used to populate the `filebeat.yml` configuration file.  The typical keys that you will want to define are:

-   `filebeat.prospectors`  
-   `filebeat.config.modules`  
-   `setup.template.settings`   
-   The output (i.e. `output.elasticsearch` or `output.logstash`)  

```yaml
filebeat_module_config: {}
```

The `filebeat_module_config` variable is a dictionary similar to `filebeat_config_content`, however it is used to create the configuration files for the Filebeat modules.  The dictionary key is the name of the module that you want to enable, and the contents of that key are itself a dictionary containing the configuration for the module.

For example:

```yaml
filebeat_module_config:
  system:
    syslog:
      enabled: "true"
    auth:
      enabled: "true"
```

### RedHat specific values (see `vars/filebeat-RedHat.yml`)

```yaml
filebeat_home: /usr/share/filebeat
```

The path where filebeat is installed.

```yaml
filebeat_bin_dir: "{{ filebeat_home }}/bin"
```

The path where the filebeat binary is installed.

```yaml
filebeat_config_dir: "/etc/filebeat"
```

The path to the filebeat configuration directory.

```yaml
filebeat_config_file: "{{ filebeat_config_dir }}/filebeat.yml"
```

The full path to the filebeat configuration file.

```yaml
filebeat_modules_dir: "{{ filebeat_config_dir }}/modules.d"
```

The path where filebeat module configuration is stored.

## Dependencies

None.

## Example Playbook

```yaml
- hosts: servers
  roles:
     - role: javiergayala.filebeat
       filebeat_module_config:
         system:
           syslog:
             enabled: "true"
           auth:
             enabled: "true"
```

## License

BSD

## Author Information

This role was created in 2018 by [Javier Ayala](http://www.javierayala.com/).
