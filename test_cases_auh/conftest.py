# conftest.py
import os


def pytest_addoption(parser):
    parser.addoption("--script", default="auto-upgrade-helper/upgrade-helper.py",
                     action="store", help="Path to auh tool")
    parser.addoption("--recipe_successful", action="store", default="recipe-successful",
                     help="recipe to test SUCCESSFUL")
    parser.addoption("--recipe_match", action="store", default="recipe-match", help="recipe to test MATCH")
    parser.addoption("--recipe_failed", action="store", default="recipe-failed", help="recipe to test FAILED")
