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
                images {
                    id
                    image {
                        name
                        url
                    }
                }
            }
        }
    """

        projects = ProjectFactory.create_batch(3)
        resp = self.query_check(project_query)
        self.assertEqual(
            [
                dict(
                    id=str(project.id),
                    location=project.location,
                    title=project.title
                ) for project in projects
            ], resp['data']['projects']
        )
        self.assertIsNotNone([project.title] for project in projects)
        self.assertIsNotNone([project.location] for project in projects)
        self.assertIsNotNone([image['image']] for image in resp['data']['image'])
