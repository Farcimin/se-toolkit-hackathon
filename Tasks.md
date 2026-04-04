# Lab 9 - Quiz and Hackathon

The lab opens with a quiz and then kicks off the hackathon.

To get the full point for the lab, you need to:

- Pass Tasks 1, 2, 3 during the lab AND
- Finish Tasks 4 and 5 by the usual deadline of Thursday 23:59.

Each student builds their own project:

- Go from an idea to a deployed product.
- Use agents and LLMs throughout.

----

## Task 1 (graded by TA after the lab)

Pen and paper quiz:

- 20 mins;
- closed book, no devices;
- you get 3 random questions from the question bank;
- answer at least 2.

## Task 2 (approved by TA during the lab)

Ideate and plan your project.

### Project idea

The project idea must be:

- something simple to build;
- clearly useful;
- easy to explain.

Define and show to your TA:

- End-user of the product
- What problem your product solves for the end-user?
- The product idea in one short sentence.
- What is the product's core feature?

### Implementation plan

When the idea is approved, produce a plan for two product versions.

Version 1 does one core thing well:

- Pick the one feature most valuable to the end-user and relatively easy to implement;
- It is a functioning product, not a prototype;
- Must be shown to the TA upon completion for feedback.

Version 2 builds upon Version 1:

- Improves the initial feature or adds another one on top;
- Address TA feedback from the lab;
- Deploy and make it available for use.

The product must have the following components, each fulfilling a useful function:

- backend;
- database;
- end-user-facing client: web app, mobile app, or LLM-powered agent, e.g. `nanobot`.

Note:

- You can use the setup from Lab 8 or start from scratch.
- `Telegram` bots are blocked on university VMs.

## Task 3 (approved by TA during the lab)

Implement Version 1 outlined in the plan:

- Build one core feature;
- Follow best practices and git workflow;
- Test it yourself and fix bugs;
- Have the TA try it as a user;
- Take note of the TA feedback;
- Get TA's approval for the task to be marked as DONE.

## Task 4

Implement and deploy Version 2 outlined in the plan:

- Build and polish functionality;
- Take TA feedback into account;
- Push all code to the GitHub repo (see the detailed instructions below);
- Follow best practices and git workflow;
- Document your solution;
- Dockerize all services;
- Deploy it to be accessible to use.

Version 2 can be completed during the lab or after it, before the usual deadline.

## Task 5 (demo and PDF submitted through Moodle)

Submit a presentation with five slides:

1. Title:

   - Product title
   - Your name
   - Your university email
   - Your group

2. Context:

   - End-user of the product
   - What problem your product solves
   - The product idea in one short sentence

3. Implementation:

   - How you built the product
   - What went into Version 1 and Version 2
   - What TA feedback points you addressed

4. Demo:

   - Pre-recorded video demonstration of Version 2 with voice-over (no longer than 2 minutes).
   - _Note:_ **This is the most important part of the presentation**.

5. Links:

   - Link and QR code for each of these:
     - The GitHub repo with the product code
     - Deployed product (latest version)

----

## Publishing the product code on GitHub

- Publish the product code in a repository on `GitHub`.

  The repository must be called `se-toolkit-hackathon`.

- Add the MIT license file to make your product open-source.

- Add `README.md` in the product repository.

  `README.md` structure:

  - Product name (as title)

  - One-line description

  - Demo:
    - A couple of relevant screenshots of the product

  - Product context:

    - End users
    - Problem that your product solves for end users
    - Your solution

  - Features:

    - Implemented and not yet implemented features

  - Usage:

    - Explain how to use your product

  - Deployment:

    - Which OS the VM should run on (you may assume `Ubuntu 24.04` like on your university VMs)
    - What should be installed on the VM
    - Step-by-step deployment instructions
