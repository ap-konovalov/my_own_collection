#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This module create .txt file with content

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This module create .txt file on host with content passed with args

options:
    path:
        description: This is the path where .txt file created
        required: true
        type: str
    content:
        description: This is the file content
        required: true
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Aleksandr Konovalov (@ap-konovalov)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.my_test:
    path: example.txt
    content: hello world
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample:
         "changed": false,
         "content": "lets learn netology ansible",
         "gid": 20,
         "group": "staff",
         "mode": "0644",
         "owner": "aleksandr",
         "path": "example.txt",
         "size": 27,
         "state": "file",
         "uid": 501
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str'),
            content=dict(type='str')
        ),
        supports_check_mode=True
    )

    f = open(module.params['path'], "w")
    f.write(module.params['content'])
    f.close()

    result = dict(
        path=module.params['path'],
        content=module.params['content']
    )

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()