import requests
from datetime import date, timedelta


def get_trending_repositories(top_size):
    repos_url = 'https://api.github.com/search/repositories'
    datetime_week_ago = (date.today() - timedelta(days=7)).strftime('%Y-%m-%d')
    created_last_week = 'created:>={}'.format(datetime_week_ago)
    params = {
        'q': created_last_week,
        'sort': 'stars',
        'per_page': top_size
    }
    trending_repos = requests.get(repos_url, params=params)
    top_github_repos = trending_repos.json()['items']
    return top_github_repos


def get_open_issues_amount(repo_owner, repo_name):
    repo_url = 'https://api.github.com/repos/{}/{}/issues'.format(
        repo_owner,
        repo_name
    )
    issues = requests.get(repo_url)
    return len(issues.json())


def show_top_repo_info(top_number, repo_name, repo_issues, repo_url, repo_stars):
    print('#{}\nName: {}\nStars: {}\nIssues: {}\nUrl: {}\n'.format(
        top_number,
        repo_name,
        repo_stars,
        repo_issues,
        repo_url
    ))


if __name__ == '__main__':
    print('Top 20 of Github repositories by stars for the last week:\n')
    top_size = 2
    top_github_repos = get_trending_repositories(top_size)
    for top_number, repo in list(enumerate(top_github_repos, start=1)):
        repo_name = repo['name']
        repo_owner = repo['owner']['login']
        repo_url = repo['url']
        repo_stars = repo['stargazers_count']
        repo_issues = get_open_issues_amount(
            repo_owner,
            repo_name
        )
        show_top_repo_info(
            top_number,
            repo_name,
            repo_issues,
            repo_url,
            repo_stars,
        )