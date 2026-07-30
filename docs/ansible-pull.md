# Ansible Pull

Manual example:

```sh
ansible-pull \
  -U https://github.com/lirux9873/c9-freebsd-workstation-ansible.git \
  -i hosts \
  local.yml
```

`ansible-pull` clones or updates the repository locally and runs the selected
playbook on the same host.

The future scheduled implementation should:

1. use a fixed repository URL and branch;
2. log output;
3. prevent concurrent runs;
4. use a predictable checkout directory;
5. validate syntax before applying changes;
6. document exactly when it runs;
7. avoid storing credentials in the repository.
