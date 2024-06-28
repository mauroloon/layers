from googleapiclient.discovery import build


def make_build(
    service_name: str,
    version: str,
    credentials: dict
):
    """
    Build a Google API service object.

    Args:
        service_name (str): The name of the service to build.
        version (str): The version of the service to build.
        credentials (dict): The credentials to use to build the service.

    Returns:
        googleapiclient.discovery.Resource: The built service object

    """
    return build(service_name, version, credentials=credentials)