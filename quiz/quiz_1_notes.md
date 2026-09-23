# DATASCI 350 - Quiz 1
## Computing Basics, Command Line, Git, and Github
- 25 tasks
- repository that we have to fork, and answer questions

### Computing Basics
- **Decimal to Binary:** (0 or 1 × 2<sup>0</sup>) + (0 or 1 × 2<sup>1</sup>) + (0 or 1 × 2<sup>2</sup>) + (0 or 1 × 2<sup>3</sup>) + (0 or 1 × 2<sup>4</sup>)... where 0 or 1 correspond to whether that binary position has a 0 or 1
- **Decimal to Hexadecimal:** keep dividing by 16, the remainder corresponds to letters/number in ASCII; read backwards
- **Hexadecimal to Decimal:** multiply first number/letter by 16, add the 2nd number/letter

### Command Line
- **whoami** - which user you are
- **pwd** - prints current working directory
- **mkdir new-folder** - creates a new folder/directory
    - mkdir -p new-folder - creates all missing parent directories
- **rm file-name** - removes a file
- **rm -rf folder/directory** - recursively removes a folder/directory
- **cd folder/directory** - changes/moves directory
- **ls** - lists files in current folder/directory
    - ls -l: long format, with details
    - ls -a: include hidden files (.gitignore)
    - ls -lh: long format, readable sizes
    - ls -R: include subdirectories
- **mv old/file/location new/file/location** - moves a file from one folder/directory to another
- **cp file new/location** - makes a copy of a file to a location
- **touch file-name** - adds a file to the folder/directory
- **cat file-name** - shows what is in a file
- **find file-name** - search for files
- **grep "x" file** - prints lines that contain "x"
    - -n numbers the lines, -i ignores capitals, -v inverts, -r searches a directory, -c counts
- **wc -l file-name** - counts the number of lines 
- **head -n 5 file-name** - first 5 lines of the file
- **tail -n 5 file-name** - first 5 lines of the file
- **sed 's/a/b/g' file-name** - replace a with b
- '*' matches any number of characters
- '?' matches exactly one character
- Use 2 dots to count, commas to list
- '>' sends output to a file and overwrites it
- '>>' sends output to a file and appends it
- '|' feeds 1 command's output into the next

### Git and Github
- **git init** - starts a repository
- **git clone url** - copy a repository from GitHub
- **git status** - shows where everything is/what changed
- **git add .** - stage everything
- **git add file-name** - stage that specific file
- **git commit -m "msg"** - save a snapshot
- **git log --oneline** - the history, one line each
- **git push** - send commits to github
- **git pull** - bring other people's commits back
- **git diff** - shows what you have changed but have not yet staged
- **git diff --staged** - shows what is staged and about to be committed 
- **git commit --ammend -m "The message I meant"** - fixing a wrong commit message
- **git add the-forgotten-file && git commit --amend --no-edit** - if you forgot to include a file
- **git reset --soft HEAD~1** - undo the last commit, keep the work
- **git branch** - lists branches
- **git checkout -b feature-x** - creating a branch (work on something without touching main)
- **git checkout main** - go back to main
- **git merge feature-x** - add the branch to main
- **git branch -d feature-x** - remove the branch
- **git switch -c new-branch hash** - revisit an old commit
- **git cherry-pick commit_id** - allows you to pick specific commits from 1 branch and apply them to another
- **git stash** - puts your uncommitted changes aside, leaving a clean working directory
- **git stash push -m "descriptive message"** - stash with a descriptive message
- **git stash pop** - restore most recent stash and remove from stack; makes it easy to move your uncommitted changes to the correct branch
- **gh pr create --title "My PR" --body "Description of my PR"** - create a pull request
- **gh issue create --title "My Issue" --body "Description of my issue"** - create an issue
- **gh repo create new-project --public --source=. --push** - create a repo and push your local code to it
- **gh repo view --web** - view repo in web browser
- .gitignore lists what Git should never track
- after forking a repository, you will see it on your GitHub account
- clone it with **git clone https://github.com/your-username/repository-name.git**