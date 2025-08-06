This README file contains information on the contents of the meta-luckfox-pico layer.

Please see the corresponding sections below for details.

Supported Devices
=================

Currently supported devices are:
- Luckfox Pico Max
- Luckfox Pico Mini (A/B)

Dependencies
============

This layer depends on:

    URI: git://git.yoctoproject.org/poky
    branch: scarthgap

    URI: git://git.openembedded.org/meta-openembedded
    layer: meta-oe
    branch: scarthgap

    URI: https://github.com/pengutronix/meta-ptx.git
    branch: scarthgap

Table of Contents
=================

1. Adding the meta-luckfox-pico layer to your build
2. Misc
3. TODO

I. Adding the meta-luckfox-pico layer to your build
=================================================

Run ```bitbake-layers add-layer meta-luckfox-pico```

II. Misc
========

In ```local.conf``` add
```
IMAGE_FSTYPES = "ext4"
IMAGE_ROOTFS_SIZE = "1048576"

IMAGE_INSTALL:append = " \
    btop \
    alsa-utils \
"
```

Run ```bitbake sdcard``` to generate SD card image

Image will be located in ```/path/to/yocto/build/tmp/deploy/images/sdcard-MACHINE.img```

III. TODO
=========

- [ ] Replace genimage with wic
- [ ] Do pre create image task to generate env.img
