# Title: (Work)Flow States: How are we doing (what we are doing)?

Abstract: Everyone's doing something, almost all of us on computer. But despite this commonality, we often talk more what we are doing than how we are doing it. So I'll start with me:

1. I argue that we should be intentional about how we use a computer for both moral and practical reasons, and claim that generally: relying on AI is bad, relying on corporate or subscription products is bad, not having guaranteed control and access and storage of your own labor is bad; automating tasks is good, reproducibility is good, modularity is good, open source is good.
2. I walk through the particulars of the workflow these arguments have lead _me_ to, including note-taking apps, flash cards, citation managers, local latex, a pipeline mentality, and general coding and modularity principles.

# Addenda

- One thing I forgot to include but should have spent some time on -- use a formatter and a linter for your code! really useful for making things readable, regular, so on. For formatting, I use `ruff` for python, `prettier` for javascript and markdown, and `latexindent` for latex. then I set "editor.formatOnSave": true, in vs code settings JSON. `ruff` also has a linter.
- Have as much of a regular, normalized system for naming variables (including datasets, vars in datasets, and vars in code) as possible.
- Jupyter notebooks are good for quickly altering figures or anything that requires working off a large dataset (eg, pandas dataframe) that you'd like to keep in cached memory. However, they're a HUGE pain for version control, replicable workflows, improvable workflows, all of it. I strongly recommend that you _always_ functionalize and consolidate all valuable code you write in them into a `.py` script BEFORE you get up or walk away from the notebook. If you're doing too much work for that, then you're doing too much work in a notebook.
- Top of the head things that will prevent your version from working:
  - You need to have a local `latex` distribution
  - You need to have a pdf viewer extension for vs code
