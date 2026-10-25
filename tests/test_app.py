"""Smoke tests for the Flask backend"""
from unittest import mock

import pytest
import requests

from myapp import app


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv('RECAPTCHA_PRIVATE_KEY', 'test-key')
    monkeypatch.setenv('MY_EMAIL', 'me@example.com')
    return app.test_client()


def recaptcha(success):
    res = mock.Mock()
    res.json.return_value = {'success': success}
    return mock.patch('myapp.routes.requests.post', return_value=res)


@pytest.mark.parametrize('url', ['/', '/projects/', '/css/bootstrap.min.css'])
def test_static_pages(client, url):
    assert client.get(url).status_code == 200


@pytest.mark.parametrize('url', ['/../../etc/passwd',
                                 '/css/%2e%2e/%2e%2e/routes.py',
                                 '/nonexistent'])
def test_missing_or_escaping_paths(client, url):
    assert client.get(url).status_code == 404


def test_show_email_valid_captcha(client):
    with recaptcha(True):
        res = client.post('/show_email', data={'g-recaptcha-response': 'x'})
    assert res.status_code == 200
    assert res.json == {'email': 'me@example.com'}


def test_show_email_invalid_captcha(client):
    with recaptcha(False):
        res = client.post('/show_email', data={'g-recaptcha-response': 'x'})
    assert res.status_code == 400
    assert 'email' not in res.json


def test_show_email_recaptcha_unreachable(client):
    with mock.patch('myapp.routes.requests.post',
                    side_effect=requests.ConnectionError):
        res = client.post('/show_email', data={'g-recaptcha-response': 'x'})
    assert res.status_code == 400
