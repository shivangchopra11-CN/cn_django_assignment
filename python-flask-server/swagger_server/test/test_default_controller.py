# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.project import Project  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_assign_mentor(self):
        """Test case for assign_mentor

        
        """
        user_proj_id = Project()
        response = self.client.open(
            '//project/assignMentor/',
            method='POST',
            data=json.dumps(user_proj_id),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_project(self):
        """Test case for create_project

        
        """
        name = Project()
        response = self.client.open(
            '//project/createProject/',
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mentees(self):
        """Test case for get_mentees

        
        """
        response = self.client.open(
            '//users/{userId}/getMentees/'.format(userId=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mentoring_projects(self):
        """Test case for get_mentoring_projects

        
        """
        response = self.client.open(
            '//users/{userId}/getProjects/'.format(userId=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users_and_mentors(self):
        """Test case for get_users_and_mentors

        
        """
        response = self.client.open(
            '//project/{projectId}/getUserMentor/'.format(projectId=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_create(self):
        """Test case for user_create

        
        """
        name = User()
        response = self.client.open(
            '//users/createUser/',
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
