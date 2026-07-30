# c9-freebsd-workstation-ansible

A FreeBSD 15.x workstation configuration managed locally with
`ansible-pull`.

This repository is FreeBSD-specific. It does not contain Linux package
managers, systemd units, Linux service names, or Linux filesystem paths.

## Supported hardware profiles

```text
virtualbox
dell_latitude_5591
```

## Supported desktops

```text
sway
dwm
```

The default selection is:

```yaml
hardware_profile: virtualbox
desktop_environment: dwm
```

Change it in:

```text
host_vars/localhost.yml
```

## Bootstrap

On a fresh FreeBSD installation, clone the repository and run:

```sh
su -
cd /path/to/c9-freebsd-workstation-ansible
./bootstrap.sh
```

The bootstrap uses FreeBSD commands only:

```text
pkg
install
uname
id
```

It installs:

```text
ca_root_nss
git
sysutils/py-ansible-core
sudo
```

and then runs `ansible-pull`.

## Manual pull

```sh
sudo ./tools/ansible-pull.sh
```

or:

```sh
make pull
```

## Validate

```sh
make check
make validate
```

## Start the desktop

For Sway:

```sh
start-sway
```

For DWM:

```sh
startx
```

Log out and back in, or reboot, after the first run so new group membership
and boot-time kernel modules take effect.

## Scheduled pull

Scheduled pulling is disabled by default:

```yaml
ansible_pull_enabled: false
```

Enable it in `group_vars/all.yml`.

The role installs:

```text
/usr/local/sbin/c9-ansible-pull
```

and a root cron job. It uses FreeBSD `lockf` to prevent overlapping runs.

## Host changes

The project may change:

```text
/usr/local/etc/pkg/repos/FreeBSD.conf
/usr/local/etc/sudoers.d/c9-workstation
/etc/rc.conf.local
/usr/local/sbin/c9-ansible-pull
/var/db/ansible-pull/c9-freebsd-workstation
/var/log/ansible-pull.log
/home/daniel/.config/
/home/daniel/.local/bin/
/home/daniel/.xinitrc
```

It may also:

- install or upgrade FreeBSD packages;
- add the workstation user to `wheel` and `video`;
- start FreeBSD rc.d services;
- configure boot-time `kld_list`;
- add a root cron entry.

Shared configuration uses explicit `BEGIN/END ANSIBLE MANAGED BLOCK` markers.
Complete generated files contain `BEGIN/END ANSIBLE MANAGED FILE` comments.


## Hardware-owned loader configuration

Each hardware profile owns its own file under:

```text
/boot/loader.conf.d/<hardware_profile>.conf
```

The VirtualBox profile creates:

```text
/boot/loader.conf.d/virtualbox.conf
```

with:

```conf
hw.efi.poweroff="0"
```

Profiles without loader settings do not keep an empty file.
