from __future__ import annotations

import os
import re
from typing import Sequence

from dotenv import load_dotenv
from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph

load_dotenv()

_DATABASE_BASE_URL = os.getenv(
    'DATABASE_BASE_URL', 'postgresql://postgres:password@host.docker.internal:5432',
)
_DATABASES = [
    'account_store', 'fund_store',
    'assessment_store', 'application_store',
]
_README_FILE = 'README.md'


def main(_: Sequence[str] | None = None) -> int:

    filenames = []
    for database in _DATABASES:
        metadata = MetaData(bind=f'{_DATABASE_BASE_URL}/{database}')
        graph = create_schema_graph(metadata=metadata)
        filename = f'erds/{database}.png'
        filenames.append(filename)
        graph.write_png(filename)

    new_readme_content = ''
    for database, filename in zip(_DATABASES, filenames):
        new_readme_content += f'### {database.capitalize()}:\n'
        new_readme_content += f'![{filename}]({filename})\n\n'

    pattern = r'(<!-- ERD Start -->)[\s\S]*?(<!-- ERD End -->)'
    with open(_README_FILE) as file:
        old_readme_content = file.read()

    modified_content = re.sub(
        pattern, rf'\1\n\n{new_readme_content}\2', old_readme_content,
    )
    with open(_README_FILE, 'w') as file:
        file.write(modified_content)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
