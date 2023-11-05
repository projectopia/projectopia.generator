module "github_repo" {
  source = "../modules/github/repo"

  repo_name        = var.repo_name
  repo_description = var.repo_description
  repo_visibility  = var.repo_visibility

  github_token = var.github_token
  github_owner = var.github_owner
}

output "name" {
  value = module.github_repo.created_repo_name
}
