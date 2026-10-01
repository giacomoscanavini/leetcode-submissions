import sys
from pathlib import Path

def make_folders(problem: str):
    number, title = problem.split(".", 1)

    slug = title.strip().lower().replace(" ", "-").replace("/", "-")
    folder_name = f"{number.strip()}-{slug}"

    dsa_dir = Path("Data Structures & Algorithms") / folder_name
    dsa_dir.mkdir(parents=True, exist_ok=True)

    (dsa_dir / "submission-1.py").touch()

    print(f"Created {dsa_dir}/submission-1.py")


if __name__ == "__main__":
    make_folders(sys.argv[1])