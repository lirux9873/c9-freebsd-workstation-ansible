# Host Changes

## Package repository

Managed file:

```text
/usr/local/etc/pkg/repos/FreeBSD.conf
```

The selected branch is `quarterly` or `latest`.

## Package state

Managed through `ansible.builtin.package`, which uses FreeBSD `pkg`.

A full package upgrade is optional and uses:

```sh
/usr/sbin/pkg upgrade -y
```

## rc.conf

Managed blocks are written to:

```text
/etc/rc.conf.local
```

Blocks:

```text
c9-base
c9-hardware
c9-kernel-modules
c9-workstation
```

Content outside these markers is preserved.

## Account databases

The FreeBSD-aware Ansible user and group modules may update:

```text
/etc/group
/etc/master.passwd
/etc/passwd
```

The files are not edited directly.

## Services

Possible services:

```text
dbus
seatd
vboxguest
vboxservice
```

Persistent enablement is stored in `/etc/rc.conf.local`, then the rc.d service
is started.

## Desktop files

Sway:

```text
~/.config/sway/config
~/.config/waybar/config
~/.config/foot/foot.ini
~/.config/mako/config
~/.local/bin/start-sway
```

DWM:

```text
~/.xinitrc
~/.config/picom/picom.conf
~/.config/dunst/dunstrc
```

## Scheduled Ansible Pull

Optional files:

```text
/usr/local/sbin/c9-ansible-pull
/var/db/ansible-pull/c9-freebsd-workstation
/var/log/ansible-pull.log
```

A root cron entry runs the wrapper. FreeBSD `lockf` prevents concurrent runs.


## Hardware loader settings

Each hardware profile owns a separate file under `/boot/loader.conf.d/`.

VirtualBox creates `/boot/loader.conf.d/virtualbox.conf` containing:

```conf
hw.efi.poweroff="0"
```

Profiles with no loader settings do not keep an empty profile file.
