# DATASCI 350 - Quiz 1
## Computing Basics, Command Line, Git, and Github

### Quiz Day Setup
- **Fork** the quiz repository on the GitHub website
- Open the terminal and clone the fork
    - cd ~/Desktop
    - git clone https://github.com/mollym425/datasci350-quiz01.git
- In VS Code: File --> Add Folder to Workspace --> select quiz folder
- In the terminal, move to the quiz folder and check:
    - cd ~/Desktop/datasci350-quiz01
    - pwd
    - git status
- Open **commands.txt** in VS Code or create it with:
    - touch commands.txt
- Commit and push all required files, including commands.txt, then submit the fork’s URL on Canvas

### Computing Basics
- **Binary to Decimal:** (0 or 1 × 2<sup>0</sup>) + (0 or 1 × 2<sup>1</sup>) + (0 or 1 × 2<sup>2</sup>) + (0 or 1 × 2<sup>3</sup>) + (0 or 1 × 2<sup>4</sup>)... where 0 or 1 correspond to whether that binary position has a 0 or 1
- **Decimal to Hexadecimal:** keep dividing by 16, the remainder corresponds to letters/number in Hexa (A-F for 10-15); read backwards
- **Hexadecimal to Decimal:** ...+ (3rd to last digit * 256) + (second to last digit * 16) + (last digit * 1) where digits 0–9 keep their values and A–F represent 10–15.

### Command Line
- **whoami** - which user you are
- **pwd** - prints current working directory
- **mkdir new-folder** - creates a new folder/directory
    - **mkdir -p new-folder** - creates all missing parent directories
    - **mkdir -p new-folder/{folder1,folder2,folder3}** - create multiple subdirectories
- **rm file-name** - removes a file
- **rm -rf folder/directory** - recursively removes a folder/directory
- **cd folder/directory** - changes/moves directory
- **ls** - lists files in current folder/directory
    - ls -l: long format, with details
    - ls -a: include hidden files (.gitignore)
    - ls -lh: long format, readable sizes
    - ls -R: include subdirectories
- **mv old/file/location new/file/location** - moves a file from one folder/directory to another (renames too)
- **cp file new/location** - makes a copy of a file to a location
- **touch file-name** - adds a file to the folder/directory
- **cat file-name** - shows what is in a file
- **find . -name "file-name"** - search for files in current directory
- **grep "x" file** - prints lines that contain "x"
    - -n numbers the lines, -i ignores capitals, -v inverts, -r searches a directory, -c counts
- **wc -lw file-name** - counts the number of lines and words
- **head -n 5 file-name** - first 5 lines of the file
- **tail -n 5 file-name** - last 5 lines of the file
- **sed 's/a/b/g' file-name** - replace a with b (just prints)
- **echo "text" > file.txt** - write text to a file (also creates that file)
- **echo "text" >> file** - append text to a file
- '*' matches any number of characters
- '?' matches exactly one character
- Use 2 dots to count, commas to list
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
- **git commit --amend -m "The message I meant"** - fixing a wrong commit message
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
- **git log branch --oneline** - view another branch's commits
- **gh pr create --title "My PR" --body "Description of my PR"** - create a pull request
- **gh issue create --title "My Issue" --body "Description of my issue"** - create an issue
- **gh repo create new-project --public --source=. --push** - create a repo and push your local code to it
- **gh repo view --web** - view repo in web browser
- .gitignore lists what Git should never track
- after forking a repository, you will see it on your GitHub account
- clone it with **git clone https://github.com/your-username/repository-name.git**

### Resources Acknowledgement
I used the lecture notes from DATASCI 350 Lectures 2-8 to complete this quiz. I used OpenAI Codex only to review commands and answers I wrote myself, not to generate solutions.