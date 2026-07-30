# Architecture

```text
ansible-pull
    |
    v
local.yml
    |
    +-- base
    +-- hardware
    +-- workstation
    +-- desktop
    `-- ansible_pull
```

## FreeBSD boundaries

The implementation uses:

```text
/usr/sbin/pkg
/usr/sbin/sysrc
/usr/sbin/service
/usr/sbin/pw
/usr/bin/lockf
/usr/local/
/etc/rc.conf.local
```

It intentionally does not use:

```text
apt
dnf
pacman
systemctl
systemd
/etc/default
/usr/lib/systemd
Linux input/render groups
```

## Role responsibilities

### Base

- package repository selection;
- package upgrades;
- baseline packages;
- wheel membership;
- sudo policy.

### Hardware

- profile-specific packages;
- rc.d service enablement and startup;
- boot-time kernel module list.

### Workstation

- D-Bus and seatd;
- video group;
- standard user directories.

### Desktop

- Sway or DWM packages;
- desktop configuration;
- session startup files.

### Ansible Pull

- root-owned checkout;
- cron schedule;
- `lockf` protection;
- logging.
