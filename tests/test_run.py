from kg_emerging_viruses import download, transform


def test_run():
    """Tests the run.py script."""

    download('download.yaml', 'data/raw')
    transform('data/raw', 'data/transformed')

    return None
