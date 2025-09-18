def draft_plan(subject, grade, goal, tool=None, pedagogy=None):
    return f"""
Lesson Plan ({subject}, {grade})
Goal: {goal}

1. Warm-up (5 min): Quick discussion or activity.
2. Pedagogical Strategy: {pedagogy or "Choose an active method"}.
3. Main Activity (20–30 min): Use {tool or "a relevant online tool"}.
4. Wrap-up (5 min): Reflection or exit ticket.

Why this works:
- {pedagogy or "Active pedagogy"} fosters engagement.
- {tool or "Interactive tools"} support practice and deeper learning.
"""
