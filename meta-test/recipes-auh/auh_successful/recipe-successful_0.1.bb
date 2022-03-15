SUMMARY = "bitbake-layers recipe"
DESCRIPTION = "Recipe created by bitbake-layers"
LICENSE = "MIT"
LIC_FILES_CHKSUM="file://${THISDIR}/COPYING;md5=3da9cfbcb788c80a0384361b4de20420"

UPSTREAM_CHECK_COMMITS="1"

SRCREV = "d7a09f2f12f17b4a3438e3a3821d9e1f2e428544"
SRCBRANCH = "auh/test_auh"
SRC_URI = "git://git@github.com:ksmanjunath18/auh-test-repo.git;protocol=ssh;branch=${SRCBRANCH}"

S="${WORKDIR}/git"
