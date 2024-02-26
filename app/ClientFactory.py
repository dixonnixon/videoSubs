class ClientFactory:
  """
  A registry for creating API clients for different resources.
  """

  def __init__(self):
    self._clients = {}

  def register(self, resource, creator):
    """
    Registers a function for creating a client for a specific resource.
    """
    self._clients[resource] = creator

  def get(self, resource):
        
        if resource in self._clients:
          return self._clients[resource]  # Return the actual client object
        else:
          # Handle the case where the client doesn't exist yet (optional)
          raise ValueError("Client not found for resource: {}".format(resource))
  
  def create(self, resource, config):
      # Create a new client based on resource and config
      client = self.create_client(resource, config) 
      self._clients[resource] = client
      return client

  def create_client(self, resource, config):
    """
    Returns an API client for the given resource using the registered creator.
    """
    creator = self._clients.get(resource)
    if creator is None:
      raise ValueError(f"Resource '{resource}' not implemented")
    return creator(config[resource])
  
  def has(self, resource):
        return resource in self._clients