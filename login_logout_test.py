import pytest
import requests
import json


def test_login():
    url = "http://127.0.0.1:5000/login"