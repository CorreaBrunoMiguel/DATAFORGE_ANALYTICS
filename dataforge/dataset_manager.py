from pathlib import Path
import shutil

import kagglehub


def _find_project_root(
    start_path: Path,
) -> Path:
    """
    Localiza a raiz de um projeto DATAFORGE.

    Um projeto válido deve conter:
    - data/
    - notebooks/
    - README.md
    """

    current_path = start_path.resolve()

    while current_path != current_path.parent:

        has_data = (
            current_path / 'data'
        ).exists()

        has_notebooks = (
            current_path / 'notebooks'
        ).exists()

        has_readme = (
            current_path / 'README.md'
        ).exists()

        if (
            has_data
            and has_notebooks
            and has_readme
        ):

            return current_path

        current_path = current_path.parent

    raise ValueError(
        'Could not locate a valid DATAFORGE project root.'
    )


def download_dataset(
    kaggle_path: str,
) -> Path:
    """
    Faz download de dataset do Kaggle
    para o projeto DATAFORGE atual.
    """

    current_dir = Path.cwd()

    project_dir = _find_project_root(
        current_dir
    )

    raw_data_dir = (
        project_dir
        / 'data'
        / 'raw'
    )

    print('\n=== STARTING DOWNLOAD ===')

    downloaded_path = Path(
        kagglehub.dataset_download(kaggle_path)
    )

    dataset_name = kaggle_path.split('/')[-1]

    target_dir = raw_data_dir / dataset_name

    target_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    for item in downloaded_path.iterdir():

        destination = target_dir / item.name

        if item.is_dir():

            shutil.copytree(
                item,
                destination,
                dirs_exist_ok=True
            )

        else:

            shutil.copy2(
                item,
                destination
            )

    print('\n=== DOWNLOAD COMPLETED ===')
    print(f'Dataset: {dataset_name}')
    print(f'Saved to: {target_dir}')

    return target_dir