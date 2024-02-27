import unittest

import mock
from unittest.mock import patch  # For mocking external dependencies
from app.client_utils import create_vimeo_client , get_client
from app.ClientFactory import ClientFactory
from unittest.mock import Mock
from unittest.mock import MagicMock



class TestGetClient(unittest.TestCase):

  resource = {'vimeo': {
      'token': 'a',
      'key': 'a',
      'secret': 'a',
    }}
  
  @patch('app.client_utils.vimeo.VimeoClient')
  def test_CreateFactory(self, mock_vimeo):
    factory = ClientFactory()
    factory.create = MagicMock(return_value=mock_vimeo)
    factory.create('vimeo', self.resource)
  
  @patch('app.client_utils.create_vimeo_client')
  @patch('app.client_utils.vimeo.VimeoClient') 
  def test_get_vimeo_client(self, mock_vimeo, mock_create_client):
    ''' 
      verifies the functionality of the\
      get_client(resource, client_factory, config) function\
      when called with the resource type "vimeo.
    "'''
    # Configure original object creation
    client_factory = ClientFactory()
    client_factory.register("vimeo", create_vimeo_client)

    #storing mocked target object
    client = mock_vimeo(self.resource['vimeo'])
  
    #create create_vimeo_client mock to avoid direct object instantiation
    mocked_client = mock_create_client(self.resource['vimeo']) 
    #holding the creation client mocked function: returned_client == mocked_client for now
    returned_client = mock_create_client.return_value  # Access the returned object

    actual_client = get_client('vimeo', client_factory, self.resource)

  
    self.assertEqual(client, create_vimeo_client(self.resource['vimeo']))
    self.assertEqual(actual_client, client)
    self.assertEqual(returned_client, mocked_client)
    self.assertEqual(create_vimeo_client(self.resource['vimeo']), client)

  def test_invalid_resource(self):
    '''
      verifies the get_client call with None as a factory
      should raise an exception "client_factory cannot be None"
    '''
    with self.assertRaises(ValueError) as e:
      theName = "invalid_resource"
      get_client(theName, None, {})  # No client creation function

    self.assertEqual(str(e.exception), "client_factory cannot be None")