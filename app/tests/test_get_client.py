import unittest
import mock
import os
from unittest.mock import patch  # For mocking external dependencies
from app.client_utils import get_client
from unittest.mock import MagicMock


class TestGetClient(unittest.TestCase):


  @patch('app.client_utils.create_vimeo_client') 
  def test_get_vimeo_client(self, mock_create_client):
    # Configure the mock to return a fake client object
    # mock_create_client.return_value = mock_create_client(ClientFactory, 'vimeo', {"vimeo": {
    #     "token": os.environ.get("VIMEO_ACCESS"),
    #     "key": os.environ.get("VIMEO_CLIENT_ID"),
    #     "secret": os.environ.get("VIMEO_CLIENT_SECRET")
    # }})

    mock_create_client.return_value = MagicMock(name='vimeo.VimeoClient')
    # Call the function with "vimeo" resource
    client = get_client("vimeo", mock_create_client, {"vimeo": {1: "fef"}})
    # Assert that the correct client was created and returned
    self.assertEqual(client, mock_create_client)

  def test_invalid_resource(self):
    with self.assertRaises(ValueError) as e:
      theName = "invalid_resource"
      get_client(theName, None, {})  # No client creation function

    self.assertEqual(str(e.exception), "client_factory cannot be None")