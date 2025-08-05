SUMMARY = "SD card image generator"
COMPATIBLE_MACHINE = "(luckfox-pico-max|luckfox-pico-mini)"

inherit genimage

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/files/common-licenses/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI += " \
    file://luckfox-pico-max.config \
    file://luckfox-pico-mini.config \
"

DEPENDS += "genext2fs-native"

GENIMAGE_VARIABLES[MACHINE] = "${MACHINE}"

do_genimage[depends] += " \
    virtual/bootloader:do_deploy \
    core-image-minimal:do_image_complete \
"

do_configure:prepend() {
    # TODO: generate genimage.config from env.txt or use other tool
    cp "${WORKDIR}/${MACHINE}.config" "${WORKDIR}/genimage.config"
}