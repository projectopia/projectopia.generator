variable "repo_name" {
    type        = string
    description = "The name of the GitHub repository"
}

variable "repo_description" {
    type        = string
    description = "The description of the GitHub repository"
}

variable "repo_visibility" {
    type        = string
    description = "Whether the GitHub repository should be private or public"
}

variable "github_token" {
    type        = string
    description = "The GitHub token to use for authentication"
}

variable "github_owner" {
    type        = string
    description = "The GitHub owner to use for authentication"
}

