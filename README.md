[![Travis (.org) branch](https://img.shields.io/travis/nl2go/ansible-role-hetzner-key/master)](https://travis-ci.org/nl2go/ansible-role-hetzner-key)
[![Codecov](https://img.shields.io/codecov/c/github/nl2go/ansible-role-hetzner-key)](https://codecov.io/gh/nl2go/ansible-role-hetzner-key)
[![Ansible Galaxy](https://img.shields.io/badge/role-nl2go.hetzner_key-blue.svg)](https://galaxy.ansible.com/nl2go/hetzner_key/)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/nl2go/ansible-role-hetzner-key)](https://galaxy.ansible.com/nl2go/hetzner_key)
[![Ansible Galaxy Downloads](https://img.shields.io/ansible/role/d/45353.svg?color=blue)](https://galaxy.ansible.com/nl2go/hetzner_key/)

# Ansible Role: Hetzner Key

An Ansible Role that manages [Hetzner Robot Keys](https://robot.your-server.de/key/index).

## Prerequisites

- Existing [Hetzner Online GmbH Account](https://accounts.hetzner.com).
- Configured [Hetzner Robot Webservice Account](https://robot.your-server.de/preferences).

## Requirements

| Name | Type | Version | Location |
|---|---|---|---|
| [ansible-filter](https://github.com/nl2go/ansible-filter) | Python package | 1.0.1 | Control node |

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    hetzner_key_webservice_base_url: https://robot-ws.your-server.de
 
Base url that is pointing to the [Hetzner Robot API](https://robot.your-server.de/doc/webservice/de.html). The variable is mostly utilized for testing purposes, there
is no need to change the default.

    hetzner_key_webservice_username: robot
    
Webservice login name. May be set/changed as described in the section [Change Access Data (Hetzner Wiki)](https://wiki.hetzner.de/index.php/KonsoleH:Zugangsdaten_aendern/en).

    hetzner_key_webservice_password: secret
    
Webservice password. May be set/changed as described in the section [Change Access Data (Hetzner Wiki)](https://wiki.hetzner.de/index.php/KonsoleH:Zugangsdaten_aendern/en).

    hetzner_key_instances:
      - name: New Key
        data: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDSkT3A1j89RT/540ghIMHXIVwNlAEM3WtmqVG7YN/wYwtsJ8iCszg4/lXQsfLFx\
        YmEVe8L9atgtMGCi5QdYPl4X/c+5YxFfm88Yjfx+2xEgUdOr864eaI22yaNMQ0AlyilmK+PcSyxKP4dzkf6B5Nsw8lhfB5n9F5md6GHLLjOG\
        uBbHYlesKJKnt2cMzzS90BdRk73qW6wJ+MCUWo+cyBFZVGOzrjJGEcHewOCbVs+IJWBFSi6w1enbKGc+RY9KrnzeDKWWqzYnNofiHGVFAuMx\
        rmZOasqlTIKiC2UK3RmLxZicWiQmPnpnjJRo7pL0oYM9r/sIWzD6i2S9szDy6aZ"
        
Keys may be managed by Ansible specifying them within `hetzner_key_instances` variable. Keys are referenced by the `name` attribute.
Existing keys stored in the [Hetzner Robot Key Management](https://robot.your-server.de/key/index) having different names will not be
updated nor removed. All keys from the [Hetzner Robot Key Management](https://robot.your-server.de/key/index) will be 
provisioned on the target hosts.

    hetzner_key_instances:
      - name: New Key
        data: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDSkT3A1j89RT/540ghIMHXIVwNlAEM3WtmqVG7YN/wYwtsJ8iCszg4/lXQsfLFx\
        YmEVe8L9atgtMGCi5QdYPl4X/c+5YxFfm88Yjfx+2xEgUdOr864eaI22yaNMQ0AlyilmK+PcSyxKP4dzkf6B5Nsw8lhfB5n9F5md6GHLLjOG\
        uBbHYlesKJKnt2cMzzS90BdRk73qW6wJ+MCUWo+cyBFZVGOzrjJGEcHewOCbVs+IJWBFSi6w1enbKGc+RY9KrnzeDKWWqzYnNofiHGVFAuMx\
        rmZOasqlTIKiC2UK3RmLxZicWiQmPnpnjJRo7pL0oYM9r/sIWzD6i2S9szDy6aZ"
        state: absent
        
Add `state: absent` to remove the key from [Hetzner Robot Key Management](https://robot.your-server.de/key/index) and
the target hosts.

    hetzner_key_webservice_concurrent_requests: 1
    hetzner_key_webservice_concurrent_poll: 1

To speed up the role execution while handling the configuration for multiple keys, the number of parallel requests made to the Hetzner Robot API
can be controlled by `hetzner_key_webservice_concurrent_requests` variable. The poll interval for asynchronous request
result processing is set using `hetzner_key_webservice_concurrent_poll`. Check official documentation on
[Asynchronous Actions and Polling](https://docs.ansible.com/ansible/latest/user_guide/playbooks_async.html) for more explanation. 

## Tags

Tags can be used to limit the role execution to a particular task module. Following tags are available:

- `hetzner_key`,`config`: Covers the full role lifecycle.
- `hetzner_key_key`: Manages access keys within [Hetzner Robot Key Management](https://robot.your-server.de/key/index).
- `hetzner_key_host`: Configures access keys on the target hosts.

## Dependencies

None.

## Example Playbook

Since the role is managing the communication with the [Hetzner Robot API](https://robot.your-server.de/doc/webservice/de.html)
only, it may be run on localhost.

    - hosts: all
      roles:
         - nl2go.hetzner_key
              
## Development
Use [docker-molecule](https://github.com/nl2go/docker-molecule) following the instructions to run [Molecule](https://molecule.readthedocs.io/en/stable/)
or install [Molecule](https://molecule.readthedocs.io/en/stable/) locally (not recommended, version conflicts might appear).


Use following to run tests:

    molecule test --all
       
This role relies on [hetzner-robot-api-mock](https://github.com/nl2go/hetzner-robot-api-mock) to simulate interactions with
the [Hetzner Robot API](https://robot.your-server.de/doc/webservice/de.html).

## Maintainers

- [build-failure](https://github.com/build-failure)

## License

See the [LICENSE.md](LICENSE.md) file for details.

## Author Information

This role was created by in 2019 by [Newsletter2Go GmbH](https://www.newsletter2go.com/).
