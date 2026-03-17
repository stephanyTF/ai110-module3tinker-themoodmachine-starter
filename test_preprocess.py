"""
Quick visual check for MoodAnalyzer.preprocess().
Run with: python test_preprocess.py
"""

from dataset import SAMPLE_POSTS
from mood_analyzer import MoodAnalyzer

analyzer = MoodAnalyzer()

print("=== Preprocess check on SAMPLE_POSTS ===\n")
for post in SAMPLE_POSTS:
    tokens = analyzer.preprocess(post)
    print(f"Input:  {post}")
    print(f"Output: {tokens}")
    print()

# Targeted punctuation edge cases
print("=== Edge case checks ===\n")
edge_cases = [
    "Hello!",
    "It's fine.",
    "Why? Because!",
    "bruh 💀",
]
for text in edge_cases:
    print(f"Input:  {text}")
    print(f"Output: {analyzer.preprocess(text)}")
    print()
