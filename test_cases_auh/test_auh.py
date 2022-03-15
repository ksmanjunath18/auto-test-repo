# test_param.py 

import os
import subprocess

import pytest


def test_oe_env():
    """For verifying Bitbake build environment"""
    build_dir = os.getenv('BUILDDIR', False)
    assert build_dir, "You must source oe-init-build-env before running this script!"


def test_script_path(pytestconfig):
    """For verifying script existence"""
    assert os.path.exists(pytestconfig.getoption('script'))


def test_auh_upgrade_SUCCESS(pytestconfig):
    """For verifying Successfull upgrade test case"""
    head_commit_old = subprocess.check_output('git rev-parse HEAD', stderr=subprocess.STDOUT)
    op = subprocess.check_output([pytestconfig.getoption('script'), '-s', pytestconfig.getoption('recipe_successful')],
                                 stderr=subprocess.STDOUT)
    head_commit_new = subprocess.check_output('git rev-parse HEAD', stderr=subprocess.STDOUT)

    assert "SUCCESSFUL" in op.decode('utf-8'), "AUH recipe:%s upgrade Failed" % pytestconfig.getoption(
        'recipe_successful')

    assert head_commit_old != head_commit_new, "AUH Git commit Failed"


def test_auh_upgrade_MATCH(pytestconfig):
    """For verifying recipe already upgraded"""
    op = subprocess.check_output([pytestconfig.getoption('script'), '-s', pytestconfig.getoption('recipe_match')],
                                 stderr=subprocess.STDOUT)

    assert "MATCH" in op.decode('utf-8'), "AUH recipe:%s needs Upgrade" % pytestconfig.getoption('recipe_match')


def test_auh_upgrade_FAILURE(pytestconfig):
    """For verifying recipe upgrade failing if SRCREV is not proper"""
    op = subprocess.check_output([pytestconfig.getoption('script'), '-s', pytestconfig.getoption('recipe_failed')],
                                 stderr=subprocess.STDOUT)

    assert "Failed" in op.decode('utf-8'), "AUH recipe:%s has no issues" % pytestconfig.getoption('recipe_failed')
