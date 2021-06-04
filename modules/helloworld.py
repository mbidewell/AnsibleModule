#!/usr/bin/python

from ansible.module_utils.basic import *

def main():
	module_args = dict(
		phrase=dict(type='str', required=True)
	)

	module = AnsibleModule(argument_spec=module_args)

	response = {"msg": module.params['phrase'].upper(), "changed": False}
	module.exit_json(**response)


if __name__ == '__main__':
    main()
