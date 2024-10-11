# Contributing
Welcome to the **Smart API Code Samples** contribution guide! 

If you're reading this, you're either interested in consuming the information provided here and/or helping out with developing more samples. Either way, we're glad you're here. Take the time to read this document, and thank you in advance for your contributions!

## Purpose
Smart has a small development team for the scope of our software. We work on many projects and issues and items of feedback at once and unfortunately, we don't have the resources to develop a full SDK (Software Development Kit) for every programming language, or connector for every piece of third party software out there. Smart relies on open-sourced software itself. Without community contributions and the open-sourced software movement, MOST software out there today wouldn't exist, or at least work as well as it does. It's core to the industry, can foster innovation, and (usually) improve security.

We don't expect you to release all your intellectual property to us and other (sometimes competing) aviation organisations - you may get a taste for how expensive software development really is - but we strongly believe that if organisations using Smart can at least get started using the API, and are able to access the incredibly rich volume of data that Smart collects, it will end up benefitting the industry as a whole. We know how important and powerful networking is in business - if one Smart organisation likes what you produce, you never know what sort of beautiful relationships might come out of that!

We don't have a Smart "App Store" for applications developed with the API - we are not *quite* be at that scale yet. But we are excited to see what you create. At a minimum, we would like to have code samples for the following API endpoints:
- `/tokens` -  Create, Read and Delete Personal Access Tokens for a Smart user.
- `/tokens/refresh` -  Refresh a PAT for a Smart User.
- `/roles` -  List the roles in an organisation.
- `/organisations` -  List the organisations the PAT holder belongs to.
- `/waypoints` -  Get a filtered list of waypoints as a CORE request.
- `/resources/#resource_id?include[]=type&include=resourceable` -  Get a single resource, including it's Type and Resourceable object.
- `/events` -  Get a filtered list of events between two dates. 

That should cover many of the caveats that might arise while accessing the Smart API, including:
- Core vs tenant requests
- Publishable key vs Personal Access Token requests
- Token abilities/permissions
- Filtering and request parameters
- Accessing relationships

## Beta
Remember the Smart API is technically in **BETA**. That means there may be (are...) some underlying issues with the API platform itself. If you run into issues, please submit a ticket via the [Smart Support Portal](https://smartaviation.net/support?category=Technical+Support).

## Getting Started
### First steps

#### 1 - Fork it

Fork the [repository](https://github.com/SmartManagementSystems/smart-api-code-samples) into your own Github account.

#### 2 - Clone it 

Clone the repo onto your development machine. This can be done using many [Git GUI's](https://git-scm.com/downloads/guis) or using the command line, e.g.
    `git clone https://<path to your FORKED repo>`

#### 3 - Branch it 

Create a new branch off `main`. See [Branch Naming](#branch-naming) for acceptable branch names.

#### 4 - Code it 

Make your magic. See [Pull Requests](#pull-requests) for code style and requirements.

#### 5 - PR it 

Back in the [Smart repository](https://github.com/SmartManagementSystems/smart-api-code-samples), submit a new pull request. You'll need to 'compare across forks' to see your branch. See [Pull Requests](#pull-requests) for requirements.

### Repo structure
We want to keep this as simple as possible. 

- `/`
  - `.gitignore`: 

    The primary `.gitignore` file. Each folder can (and should) also have its own, customised specifically for the language being developed.

  - `CONTRIBUTING.md`: 

    This document.

  - `README.md`: 

    The document seen when visiting the [repo on Github.com](https://github.com/SmartManagementSystems/smart-api-code-samples).

  - `language-version/` (folder): 

    A folder for the language the code samples contained within are written. Version is optional, but should be mentioned in the `README.md` against each code sample description.

    - `README.md`: 

        Language-specific readme file containing pertinent information about the code samples, and basic requirements to use them. This should include the version of the language if applicable. Every code sample **MUST** be recorded in this file. 

    - `operation-endpoint.specifics.py`: 
  
        Each code sample should be contained in its own file with the format `operation`-`endpoint-path`.`specifics`.`file_extension`. 
  
        For example, `post-tokens-refresh.py` would contain an example of how to refresh a Personal Access Token for a user. 

        `specifics` is an OPTIONAL string to help any ambiguity that may arise with some endpoints. 

        If certain characters are forbidden in the filename, or the language strongly enforces a file naming convention (for namespacing/autodiscover etc), then please make that clear in the `README.md` file, and the pull request.

### Branch Naming
To avoid large PR's, **every branch must only contain code for a SINGLE development task/issue**. This helps keep things focussed, and enables quicker processing, testing and merging. It avoids having large branches go stale from frustration if they don't get accepted. 

To make it clear from a glance what is being developed, the branch names **MUST** be in the following format:
- Tackling an Issue: `issue/language-#issuenumber`
- Creating a snippet: `feature/language-filename-without-extension`
- Modifications, improvements and maintenance: `maintenance/language-brief-description`

## Issues
If you come across issues with any of the code in this repository, submit an issue using the provided template. The more detail you can provide of the specifics when running into the issue, the better. This is NOT a place to submit issues to do with the API itself, or Smart Developer Portal (API documentation). Use the [Smart support desk](https://smartaviation.net/support?category=Technical+Support) for that. 

## Pull requests
In the interests of keeping things moving forward and encouraging contribution, we are going to take the approach of continuous improvement when it comes to submissions. Small things we can correct ourselves, like incorrect naming of the PR or files, language/spelling, we may fix, and include as a feedback item in the PR closing statement. We are not going to hold back contributions unless it's something that either plainly doesn't work, is not possible to comprehend, is a security issue, or is too large in scope. 

### Secrets
**DO NOT include secrets in your submitted source code!**

We suggest wherever possible, to enable your code to read from a `.env` file. You can document the required variables in the language's `README.md`.

### Closing issues
If you worked on an issue, you must include a closing keyword as the first line of the PR description. E.g. `Closes #19`

### Description
Under the closing keyword, you should divide your PR description into the following sections:
- What
  Brief explanation of what this PR provides.
- How
  Brief example of how to use the code sample, or test the fix/maintenance.
- Limitations/other
  Any other pertinent information or limitations.

Keep it short and sweet.

### Code style
Since there may be many different languages being considered, and we are not proficient in every programming language on the planet, we are going to defer code styling to the 'best practices' of each language itself. Saying that, we are not going to be able to strictly test against code style. In the future, we may be able to run an automatic linter/code formatter over submitted code. But for now, we trust our contributors to write friendly looking, standardised code. 

### Code comments
All code should be well documented, and well formatted. These are starter samples, so think about someone who has never used the Smart API before, and comment so that nothing is left in doubt about what each line of code does. Over-commenting is a "thing", but with 'getting started's and code samples, this is less of a concern.

### Tests
Tests are not required for contributing, but if you want to write unit tests for your code samples, you are welcome to. If you do, please provide instructions in the `README.md` file in the root folder for the language you are writing a sample for.