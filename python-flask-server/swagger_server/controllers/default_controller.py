import connexion
import six

from swagger_server.models.project import Project  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def assign_mentor(user_proj_id=None):  # noqa: E501
    """assign_mentor

    Assign a project mentor to a project. # noqa: E501

    :param user_proj_id: ID of project and user
    :type user_proj_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user_proj_id = Project.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_project(name=None):  # noqa: E501
    """create_project

    Create a project # noqa: E501

    :param name: Name of project
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = Project.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_mentees(userId):  # noqa: E501
    """get_mentees

    Get the list of IDs of the users being mentored by the queried user. # noqa: E501

    :param userId: ID of the user
    :type userId: int

    :rtype: None
    """
    return 'do some magic!'


def get_mentoring_projects(userId):  # noqa: E501
    """get_mentoring_projects

    Get the list of IDs of the projects being mentored by the queried user. # noqa: E501

    :param userId: ID of the user
    :type userId: int

    :rtype: None
    """
    return 'do some magic!'


def get_users_and_mentors(projectId):  # noqa: E501
    """get_users_and_mentors

    Get the list of IDs of the mentors and users of the project # noqa: E501

    :param projectId: ID of the project
    :type projectId: int

    :rtype: None
    """
    return 'do some magic!'


def user_create(name=None):  # noqa: E501
    """user_create

    Create a new user # noqa: E501

    :param name: The name of the person
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
