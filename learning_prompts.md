# Prompt 1: Teach Me a Python Concept

I'm learning Python and I don't understand how [TOPIC] works. Please help me understand it without just solving my problem for me.

Specifically, I'd like you to:
1. Explain what [TOPIC] does and why it exists
2. Show me 2–3 short examples that build from simple to slightly more complex
3. Point out a common mistake beginners make with it
4. Give me a small challenge I can try myself — don't give me the answer

Don't write my code for me. Help me understand so I can write it myself.

# Prompt 2: Explore Python Implementation Options

I'm working on a Python project and I want to [DESCRIBE WHAT YOU WANT TO DO].
Before I write this from scratch, can you help me understand my options?

1. Is there a way to do this in the Python standard library? If so, which module and why is it a good fit?
2. If not, are there well-established third-party libraries that handle this? What are the main options and what are the trade-offs between them?
3. When would it make sense to write this myself instead of using a library?
4. What should I search for if I want to learn more — what are the right terms to use?

Don't write the code for me yet. I just want to understand my options first.

# Prompt 3: Match an Existing Codebase Style

I'm working on an existing Python project and I need to understand the style and conventions it uses before I add to it.
Here is some existing code from the project:
[PASTE YOUR CODE HERE]
Please help me understand:

1. What coding style and conventions is this codebase following? (e.g. naming, structure, formatting)
2. Are there any patterns being used that I should know about before I add to it? (e.g. how errors are handled, how functions are structured)
3. What should I be careful not to break or contradict when I write new code?
4. If I wanted to add [DESCRIBE YOUR NEW FEATURE], what would "in the style of this codebase" look like — without writing it for me?

I want to fit in with what's already there, not impose my own style on top of it.

# Prompt 4: Debug Without Giving Me the Fix

My code is not working.
Here is my code and the error I am getting:
[PASTE CODE + ERROR]

Do not fix it for me.
Tell me:

1. What kind of problem this is
2. Where I should be looking first
3. What questions I should ask myself to find the bug
4. One small next debugging step I can try

Help me reason it out instead of giving me the final answer.

# Prompt 5: Review My Code Quality (Without Rewriting)

This code works, but I am not sure if it is well-written:
[PASTE CODE]

Do not rewrite it.
Tell me:

1. What a more experienced developer might notice or question
2. Any readability or maintainability concerns
3. Any risky assumptions or edge cases
4. What topics I should look up to understand the feedback better

I want to improve my judgment, not just get a rewritten version.

# Prompt 6: Explain This Error Message in Plain English

I got this error:
[PASTE ERROR]

Explain:

1. What this error is actually telling me in plain English
2. Where in my code I should look first
3. What this class of error usually means in Python
4. A simple checklist for narrowing it down

Do not write the fix. Help me interpret the error and investigate it.

# Prompt 7: Scope This Feature Before I Build It

I want to add [FEATURE] to my project.

Help me understand:

1. How complex this is (low/medium/high and why)
2. What I would need to learn first
3. Common pitfalls
4. A smaller first version (MVP) I could build first

Do not implement it. Help me decide if I am ready and what to do first.

# Prompt 8: I Read the Docs but Still Do Not Get It

I have read the docs for [LIBRARY/FUNCTION], and I still do not fully understand it.
Here is what I think it does:
[YOUR UNDERSTANDING]

Please tell me:

1. What I got right
2. What I got wrong
3. The gap in my mental model
4. A better way to think about it
5. A tiny practice exercise to confirm I understand it

Do not write production code for me. Help me build understanding.

# Prompt 9: Design Test Cases Before Coding

I am about to write [FUNCTION/FEATURE]. Before coding, help me design test cases.
List normal cases, edge cases, and failure cases I should think through first.
Do not write the implementation.

# Prompt 10: Refactor Safely in Small Steps

I want to refactor this code:
[PASTE CODE]

Do not rewrite it all at once.
Help me plan a sequence of small, safe refactor steps, what to verify after each step, and what could break.

# Prompt 11: Performance Investigation Mindset

This code feels slow:
[PASTE CODE OR DESCRIPTION]

Do not optimize it yet.
Help me figure out what to measure first, where likely bottlenecks are, and how to test whether changes actually improve performance.