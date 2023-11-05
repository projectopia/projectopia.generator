provider "github" {
  token = var.github_token
  owner = var.github_owner
}

locals {
  random_string = var.repo_name != "" ? "" : random_string.repo_suffix.result
}

resource "random_string" "repo_suffix" {
  length  = 8
  special = false
}

resource "github_repository" "init" {
  name          = var.repo_name != "" ? var.repo_name : "projectopia_generated_repo_${local.random_string}"
  description   = var.repo_description
  visibility    = var.repo_visibility

  auto_init     = true
}

resource "github_branch" "develop" {
  depends_on = [ github_repository.init ]
  repository = github_repository.init.name
  branch     = "develop"
}

resource "github_branch_protection" "branch" {
  depends_on       = [ github_repository.init ]
  repository_id    = github_repository.init.name
  pattern          = "[dm][ea][vi]*"
  enforce_admins   = true
  allows_deletions = false

  required_status_checks {
    strict         = true
    contexts       = ["default"]
  }

  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    restrict_dismissals             = true
    required_approving_review_count = 1
  }
}