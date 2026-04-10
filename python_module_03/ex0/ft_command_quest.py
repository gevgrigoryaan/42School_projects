import sys

print("=== Command Quest ===")
argc = len(sys.argv)
print(f"Program name: {sys.argv[0]}")
if argc == 1:
    print("No arguments provided!")
else:
    print(f"Arguments received: {argc - 1}")
    for arg in range(1, argc):
        print(f"Argument {arg}: {sys.argv[arg]}")
print(f"Total arguments: {argc}\n")
