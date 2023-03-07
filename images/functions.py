#Functions

def path_to_upload_img(instance, filename):
    """Creates path for uploaded image.

    Args:
        instance (class object): uploaded image instance
        filename (str): name of uploaded file

    Returns:
        str: path for saving uploaded file
    """
    return f"{instance.user.id}/images/{instance.id}/{filename}"
