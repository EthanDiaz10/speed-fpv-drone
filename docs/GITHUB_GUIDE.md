# GitHub Guide for This Project (beginner friendly)

## The 30-second version

- **Git** is a tool on your computer that saves *snapshots* of your project folder. Each snapshot is a **commit** with a short message ("printed v0.2 arms, they cracked at the root").
- **GitHub** is a website that stores a copy of those snapshots online, so it's backed up and other people (recruiters!) can see it.
- A **repository (repo)** is the project folder plus its full history.
- **Push** = send your new commits from your computer up to GitHub. **Pull** = bring changes from GitHub down to your computer.

Your commit history becomes a timeline of the build. That's exactly what makes it a good portfolio piece.

## One-time setup

1. **Make a GitHub account** at <https://github.com/signup>. Pick a professional username; it appears in your portfolio links.
2. **Install GitHub Desktop** from <https://desktop.github.com>. It's a point-and-click app, so you don't need the command line yet. Sign in with your GitHub account.
3. **Install Git LFS** from <https://git-lfs.com>, then once in a terminal run `git lfs install`. This lets the repo hold big CAD/STL files properly.
4. **Clone the repo:** in GitHub Desktop, *File → Clone repository*, pick `speed-fpv-drone`, choose a folder like `Documents/speed-fpv-drone`.

## Your everyday loop

1. Work as normal: export STLs from Fusion into `cad/v0.x/`, add photos to `media/`, write in `docs/build-log.md`.
2. Open GitHub Desktop. It lists every changed file.
3. Write a **summary** at bottom left that says what you did, e.g. `v0.2: first printed fuselage, added build photos`.
4. Click **Commit to main**, then **Push origin**.

Commit little and often (every work session), not once a month. Small commits tell the story better.

## Good commit messages

| Weak | Strong |
|---|---|
| `update` | `v0.2: thicken arm root from 3 mm to 5 mm after crack in hover test` |
| `files` | `CFD: first fuselage-only case at 70 m/s, Cd = 0.28` |

## Tracking tasks with Issues and Projects

- **Issues** (the Issues tab) are a to-do list. One issue per task: "Pick motors for v1", "Run CFD on v0.2 fuselage".
- **Projects** (the Projects tab → New project → Board) gives a Kanban board with To do / In progress / Done columns. Add your issues to it.
- When a commit finishes an issue, write `closes #12` in the message and GitHub closes it automatically, linking the work to the task.

## Milestones and releases

When a version is done (say v0.2 flies), create a **Release** (right sidebar → Releases → *Draft a new release*), tag it `v0.2`, attach the STLs and a photo, and write what changed. This gives a clean, clickable history of versions.

## Making it portfolio ready

- Keep the README's top image updated with your latest render or photo
- Pin the repo on your GitHub profile (Profile → *Customize your pins*)
- Fill in the repo's About box (gear icon on the repo page): description, topics like `fpv`, `drone`, `3d-printing`, `cfd`, `openfoam`, `fusion360`

## Glossary

| Word | Meaning |
|---|---|
| commit | a saved snapshot with a message |
| push / pull | upload / download commits to/from GitHub |
| clone | download a full copy of a repo to your computer the first time |
| branch | a parallel line of work; you can ignore these for now and just use `main` |
| LFS | Large File Storage: how Git handles big binary files like STLs |
| `.gitignore` | list of files Git should never save (temp files, huge CFD output) |
