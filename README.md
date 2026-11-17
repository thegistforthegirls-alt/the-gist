# The Gist — prototype

A lightweight, mobile-friendly daily news discovery website using the approved baby-pink and black logo. No backend server or API key required.

## What works
- Seven selectable topics and search within the current edition
- Fresh sourced article headlines and publication dates from public Google News RSS
- Original source links, quick source excerpts, saved stories in the same browser
- A scheduled GitHub Actions update targeting **4 AM America/Chicago** (CST/CDT)

## Publish (recommended: GitHub + Netlify)
1. Create a free GitHub account, if needed, and a **new public or private repository** named `the-gist`.
2. Upload **all files and folders from this project**, including `.github/workflows/morning-edition.yml`. To preserve the hidden `.github` folder, uploading through GitHub Desktop or Git is easiest; you can also create the workflow file manually on GitHub.
3. On GitHub, open **Actions → Refresh The Gist morning edition → Run workflow**. Allow a minute or two for the first news edition. Check `data/news.json` for new stories.
4. Sign in to Netlify. Select **Add new project → Import an existing project → GitHub**, select `the-gist`, and deploy. Publish directory: repository root (`.`). No build command needed.
5. Open the Netlify site URL on your phone and use **Add to Home Screen**.

## Daily updates
GitHub Actions checks hourly, but runs the refresh only during the **4 AM America/Chicago hour**. Scheduled jobs can be delayed by GitHub and Netlify deployments take additional time, so **4:00 AM sharp is not guaranteed**. You can also run the workflow manually any time. GitHub may disable scheduled workflows in inactive public repositories; monitor Actions occasionally.

## Limitations
This prototype currently indexes **news articles**, not native podcast or TikTok feeds. Search is within the downloaded edition; it does not query the internet. Source snippets are **not AI summaries**. Google News RSS may occasionally fail or provide redirect links. Social media content, especially private Facebook groups, is not copied or scraped. No account syncing: bookmarks are stored in your current browser only. Google News search may include weak or misleading sources, so read original reporting before sharing.

## Edit
Colors and homepage: `index.html`. Topics: `TOPICS` in `index.html` and `QUERIES` in `scripts/update_news.py`. Logo: styled text in `index.html`. Any commit to GitHub triggers a Netlify redeploy.

## Take the Pink Pill (coming soon)
The homepage includes a preview of a future members-only editorial section. This is **not** a paywall or secure private page. Do not publish exclusive content in this static repository. Before charging subscribers, integrate a membership/authentication provider with server-side access control, configure payments, and test the entire signup and cancellation flow.

## Donations
Deferred until a real donation URL is supplied.
