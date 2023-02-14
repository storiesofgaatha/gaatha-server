from apps.project.factories import ProjectFactory
from gaatha.tests import TestCase


class ProjectQueryTestCase(TestCase):
    def test_project_query(self):
        project_query = """
            query MyQuery {
              projects(pagination: {limit: 10}) {
                id
                title
                location
                image {
                    name
                    url
                }
            }
        }
    """

        projects = ProjectFactory.create_batch(3)
        resp = self.query_check(project_query)
        self.assertIsNotNone([project.title] for project in projects)
        self.assertIsNotNone([project.location] for project in projects)
        self.assertIsNotNone(res['image'] for res in resp['data']['projects'])
        self.assertEqual(len(resp['data']['projects']), 3)
        self.assertEqual(
            [project.title for project in projects],
            [res['title'] for res in resp['data']['projects']]
        )
        self.assertEqual(
            [project.location for project in projects],
            [res['location'] for res in resp['data']['projects']]
        )
