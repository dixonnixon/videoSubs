import vimeo

def get_client(resource, client_factory, config):
  """Returns an API client or raises a ValueError with a detailed message."""
  if client_factory is None:
      raise ValueError("client_factory cannot be None")
  try:
    if client_factory.has(resource):
      client_factory.create(resource, config)
      return client_factory.get(resource)
    
    raise ValueError("Client creator not registered for resource: {}".format(resource))
    
  except KeyError as e:
    raise ValueError(f"Resource '{resource}' not found in configuration") from e
  except ValueError as e:
    raise ValueError(f"Error creating client for resource '{resource}': {e}") from e
 

def create_vimeo_client(resource):

  # print("create_vimeo_client", resource)
  return vimeo.VimeoClient(
      token=resource['token'],
      key=resource['key'],
      secret=resource['secret']
  )