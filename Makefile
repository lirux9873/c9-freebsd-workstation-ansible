SHELL := /bin/sh

REPOSITORY_URL ?= https://github.com/lirux9873/c9-freebsd-workstation-ansible.git
REPOSITORY_BRANCH ?= main
WORK_DIRECTORY ?= /var/db/ansible-pull/c9-freebsd-workstation

.PHONY: bootstrap pull check syntax validate tree

bootstrap:
	su -m root -c "./bootstrap.sh"

pull:
	sudo env REPOSITORY_URL="$(REPOSITORY_URL)" 	    REPOSITORY_BRANCH="$(REPOSITORY_BRANCH)" 	    WORK_DIRECTORY="$(WORK_DIRECTORY)" 	    ./tools/ansible-pull.sh

check syntax:
	./tools/check.sh

validate:
	/usr/local/bin/ansible-playbook -i hosts playbooks/validate.yml

tree:
	find . -not -path './.git/*' | sort
