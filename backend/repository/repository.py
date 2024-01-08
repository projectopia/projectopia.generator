import requests
import json
import logging
from typing import List, Dict


class BaseRepository:
    def __init__(self,
                 token: str,
                 version: str,
                 name: str,
                 description: str = None,
                 homepage: str = "",
                 private: bool = False,
                 is_template: bool = False,
                 auto_init: bool = True):
        # Write a docstring for this class
        """Base class for creating a repository
        :param token: Personal access token
        :param version: API version
        :param name: Repository name
        :param description: Repository description
        :param homepage: Repository homepage
        :param private: Private repository
        :param is_template: Template repository
        :param auto_init: Auto initialize repository
        """

        self._token = token
        self._name = name
        self._description = description
        self._homepage = homepage
        self._private = private
        self._is_template = is_template
        self._auto_init = auto_init

        self._base_url = "https://api.github.com"
        self._headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self._token}",
            "X-GitHub-Api-Version": version
        }

        self._username = self._get_username()
        self._logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def _request(self, method: str, url: str, **kwargs):
        response = requests.request(
            method, url, headers=self._headers, **kwargs)
        return response

    def _get_username(self):
        url = f"{self._base_url}/user"
        response = self._request("GET", url)
        if response.status_code == 200:
            return response.json()["login"]
        else:
            self._logger.error(
                f"Failed to get username. Error: {response.text}")
            return None


class PersonalRepository(BaseRepository):
    def __init__(self,
                 token: str,
                 name: str,
                 description: str = "This is your first repo!",
                 homepage: str = "https://github.com",
                 private: bool = False,
                 is_template: bool = True,
                 auto_init: bool = True,
                 version="2022-11-28"):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        if not isinstance(homepage, str):
            raise TypeError("Homepage must be a string")
        if not isinstance(private, bool):
            raise TypeError("Private must be a boolean")
        if not isinstance(is_template, bool):
            raise TypeError("Is_template must be a boolean")
        if not isinstance(auto_init, bool):
            raise TypeError("Auto_init must be a boolean")
        if not isinstance(token, str):
            raise TypeError("Token must be a string")
        if not isinstance(version, str):
            raise TypeError("Version must be a string")
        super().__init__(token, version, name, description, homepage,
                         private, is_template, auto_init)

    def create(self):
        payload = {
            "name": self._name,
            "description": self._description,
            "homepage": self._homepage,
            "private": self._private,
            "is_template": self._is_template,
            "auto_init": self._auto_init
        }
        url = f"{self._base_url}/user/repos"
        response = self._request(
            "POST", url, data=json.dumps(payload))
        if response.status_code == 201:
            self._logger.info("Repository created successfully!")
        else:
            self._logger.error(
                f"Failed to create repository. Error: {response.text}")
        return response

    def delete(self):
        url = f"{self._base_url}/repos/{self._username}/{self._name}"
        response = self._request("DELETE", url)
        if response.status_code == 204:
            self._logger.info("Repository deleted successfully!")
        else:
            self._logger.error(
                f"Failed to delete repository. Error: {response.text}")

    def add_collaborator(self, username: str):
        url = f"{self._base_url}/repos/{self._username}/{self._name}/collaborators/{username}"
        response = self._request("PUT", url)
        if response.status_code == 201:
            self._logger.info(
                f"Collaborator {username} added successfully!")
        else:
            self._logger.error(
                f"Failed to add collaborator. Error: {response.text}")

    def add_collaborators(self, usernames: List[str]):
        for username in usernames:
            self.add_collaborator(username)

    def add_branch(self, branch_name: str, from_branch: str = "main"):
        url = f"{self._base_url}/repos/{self._username}/{self._name}/git/refs"
        branches = self._request("GET", url).json()
        branch = list(
            filter(lambda x: x["ref"] == f"refs/heads/{from_branch}", branches))
        payload = {
            "ref": f"refs/heads/{branch_name}",
            "sha": branch[0]["object"]["sha"]
        }
        response = self._request("POST", url, data=json.dumps(payload))
        if response.status_code == 201:
            self._logger.info(f"Branch {branch_name} added successfully!")
        else:
            self._logger.error(
                f"Failed to add branch. Error: {response.text}")

    def add_branches(self, branch_components: Dict[str, str]):
        for branch_name, from_branch in branch_components.items():
            self.add_branch(branch_name, from_branch)

    def set_branch_protection_rules(self,
                                    branch_name: str,
                                    required_status_checks: Dict[str, Dict[str, str]],
                                    enforce_admins: bool,
                                    required_pull_request_reviews: Dict[str, Dict[str, str]],
                                    restrictions: Dict[str, Dict[str, str]],
                                    required_linear_history: bool = False,
                                    allow_force_pushes: bool = False,
                                    allow_deletions: bool = False,
                                    block_creations: bool = False,
                                    required_conversation_resolution: bool = False,
                                    lock_branch: bool = False,
                                    allow_fork_syncing: bool = False,):
        url = f"{self._base_url}/repos/{self._username}/{self._name}/branches/{branch_name}/protection"
        payload = {
            "required_status_checks": required_status_checks,
            "enforce_admins": enforce_admins,
            "required_pull_request_reviews": required_pull_request_reviews,
            "restrictions": restrictions,
            "required_linear_history": required_linear_history,
            "allow_force_pushes": allow_force_pushes,
            "allow_deletions": allow_deletions,
            "block_creations": block_creations,
            "required_conversation_resolution": required_conversation_resolution,
            "lock_branch": lock_branch,
            "allow_fork_syncing": allow_fork_syncing
        }
        response = self._request("PUT", url, data=json.dumps(payload))
        if response.status_code == 200:
            self._logger.info(f"Branch protection rules set successfully!")
        else:
            self._logger.error(
                f"Failed to set branch protection rules. Error: {response.text}")

    def configure_github_pages(self, source: str, branch: str = "main"):
        url = f"{self._base_url}/repos/{self._username}/{self._name}/pages"
        payload = {
            "source": {
                "branch": branch,
                "path": source
            }
        }
        response = self._request("POST", url, data=json.dumps(payload))
        if response.status_code == 201:
            self._logger.info(f"GitHub Pages configured successfully!")
        else:
            self._logger.error(
                f"Failed to configure GitHub Pages. Error: {response.text}")

    def update_github_pages(self, source: str, branch: str = "main"):
        url = f"{self._base_url}/repos/{self._username}/{self._name}/pages"
        payload = {
            "cname": None,
            "source": {
                "branch": branch,
                "path": source
            }
        }
        response = self._request("PUT", url, data=json.dumps(payload))
        if response.status_code == 204:
            self._logger.info(f"GitHub Pages updated successfully!")
        else:
            self._logger.error(
                f"Failed to update GitHub Pages. Error: {response.text}")

    def delete_github_pages(self):
        url = f"{self._base_url}/repos/{self._username}/{self._name}/pages"
        response = self._request("DELETE", url)
        if response.status_code == 204:
            self._logger.info(f"GitHub Pages deleted successfully!")
        else:
            self._logger.error(
                f"Failed to delete GitHub Pages. Error: {response.text}")
