import os

from django.core.exceptions import ValidationError


def get_default_user_img_path() -> str:
    """
    return a default user image path
    :return: (media)/default/avatar/user-avatar.jpg
    """
    return f"default/avatar/user-avatar.jpg"


def get_custom_user_img_path(instance, file) -> str:
    """
    return a custom user image path
    :return: (media)/avatar/user_id/photo.jpg
    """
    return f'avatar/user_{instance.id}/{file}'


def validate_size_image(file_obj):
    """
    Check the image file size
    """
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Max image file size {megabyte_limit}MB")


def delete_old_file(path_file):
    """ 
    Delete the old file
    """
    if os.path.exists(path_file):
        os.remove(path_file)


def get_redirect_name(request):
	"""
    Function to return a redirect url name
    """
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect