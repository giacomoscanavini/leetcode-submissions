import sys
from pathlib import Path

def make_folders(problem: str):
    number, title = problem.split(".", 1)

    slug = title.strip().lower().replace(" ", "-")
    folder_name = f"{number.strip()}-{slug}"

    sql_dir = Path("SQL") / folder_name
    pandas_dir = Path("pandas") / folder_name

    sql_dir.mkdir(parents=True, exist_ok=True)
    pandas_dir.mkdir(parents=True, exist_ok=True)

    (sql_dir / "submission-1.sql").touch()
    (pandas_dir / "submission-1.py").touch()

    print(f"Created {sql_dir}/submission-1.sql")
    print(f"Created {pandas_dir}/submission-1.py")


if __name__ == "__main__":
    make_folders(sys.argv[1])