from pathlib import Path
import shutil

import kagglehub


def download_dataset(
    kaggle_path: str,
) -> Path:
    """
    Faz download de dataset do Kaggle
    para o projeto atual.

    Requer notebook dentro de:
    PROJECTS/<PROJECT_NAME>/NOTEBOOKS/
    """

    current_dir = Path.cwd()

    if current_dir.name != 'NOTEBOOKS':

        raise ValueError(
            'Notebook must be executed inside '
            'PROJECTS/<PROJECT_NAME>/NOTEBOOKS'
        )

    project_dir = current_dir.parent

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