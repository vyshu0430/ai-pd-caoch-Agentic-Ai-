import os
from coach.agent import get_resources
from coach.planner import draft_plan
from coach.calendar import create_pd_block

def main():
    print("=== Agentic AI PD Coach ===")
    subject = input("Enter subject: ")
    grade = input("Enter grade/level (e.g., 5-12, College): ")
    goal = input("Enter teaching goal: ")

    # Step 1: Agent fetches resources live from the web
    print("\n🔎 Searching the web for resources...")
    resources = get_resources(subject, grade, goal)
    print("\nRecommended Resources:\n", resources)

    # Step 2: Generate a lesson plan (AI-driven, not JSON-based)
    plan = draft_plan(subject, grade, goal)
    print("\n📘 Lesson Plan:\n", plan)

    # Step 3: Calendar block
    cal = create_pd_block()
    print(f"\n📅 PD block saved to {cal}")

if __name__ == "__main__":
    main()
