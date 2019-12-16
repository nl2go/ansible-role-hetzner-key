[![Travis (.org) branch](https://img.shields.io/travis/nl2go/ansible-role-hetzner-key/master)](https://travis-ci.org/nl2go/ansible-role-hetzner-key)
[![Ansible Galaxy](https://img.shields.io/badge/role-nl2go.hetzner_key-blue.svg)](https://galaxy.ansible.com/nl2go/hetzner_key/)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/nl2go/ansible-role-hetzner-key)](https://galaxy.ansible.com/nl2go/hetzner_key)
[![Ansible Galaxy Downloads](https://img.shields.io/ansible/role/d/44723.svg?color=blue)](https://galaxy.ansible.com/nl2go/hetzner_key/)

# Ansible Role: Hetzner Key

An Ansible Role that manages [Hetzner Robot Keys](https://robot.your-server.de/key/index).

## Requirements

- Existing [Hetzner Online GmbH Account](https://accounts.hetzner.com).
- Configured [Hetzner Robot Webservice Account](https://robot.your-server.de/preferences).

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    hetzner_key_webservice_base_url: https://robot-ws.your-server.de
 
Base url that is pointing to the [Hetzner Robot API](https://robot.your-server.de/doc/webservice/de.html). The variable is mostly utilized for testing purposes, there
is no need to change the default.

    hetzner_key_webservice_username: robot
    
Webservice login name. May be set/changed as described in the section [Change Access Data (Hetzner Wiki)](https://wiki.hetzner.de/index.php/KonsoleH:Zugangsdaten_aendern/en).

    hetzner_key_webservice_password: secret
    
Webservice password. May be set/changed as described in the section [Change Access Data (Hetzner Wiki)](https://wiki.hetzner.de/index.php/KonsoleH:Zugangsdaten_aendern/en).

## Dependencies

None.

## Example Playbook

Since the role is managing the communication with the [Hetzner Robot API](https://robot.your-server.de/doc/webservice/de.html)
only, it may be run on localhost.

    - hosts: all
      roles:
         - nl2go.hetzner-key
              
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
