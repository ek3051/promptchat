import unittest
from github_handler import get_user_repos

class TestGitHubHandler(unittest.TestCase):

    def test_get_user_repos(self):
        repos = get_user_repos('octocat')
        self.assertIsNotNone(repos)
        self.assertIsInstance(repos, list)

if __name__ == '__main__':
    unittest.main()
