gh_clone_with_token() {
    url=$1
    # Extract the organization and repository name from the URL
    org_repo=$(echo $url | sed -E 's/.*github.com\/([^\/]+\/[^\/]+).git/\1/')
    # Authenticate with your second GitHub account
    gh auth login --with-token < ~/.ghtoken2
    # Clone the repository using the extracted organization and repository name
    gh repo clone $org_repo
}
