import os

import docker.errors
from dotenv import load_dotenv

try:
    import docker
    import docker.errors
except ImportError as exc:
    raise ImportError(
        """Couldn't import Docker. Are you sure it's installed and /
        available on your PYTHONPATH environment variable? Did you
        forget to activate a virtual environment?"""
    ) from exc


def start_docker_container():
    _ = load_dotenv()

    """starts a docker image with SQL database"""
    client = docker.from_env()

    CONTAINER_NAME = 'laws'
    IMAGE_NAME = 'laws_POSTESQL'
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    DOCKERFILE_PATH = 'docker/'

    try:
        _ = client.images.build(
            path=DOCKERFILE_PATH,
            tag=IMAGE_NAME,
            rm=True,
        )
    except Exception as e:
        print(f'\uea87 Build image error: {e}')
        raise

    try:
        container = client.containers.get(CONTAINER_NAME)

        if container.status != 'running':
            print(f'\ueb7b Starting Container, Already exists: {CONTAINER_NAME}...')

            container.start()

        else:
            print(f'\uf058 Container is already running: {CONTAINER_NAME}.')

    except docker.errors.NotFound:
        print(f'\uf058 Container is running: {CONTAINER_NAME}.')
        try:
            _ = client.containers.run(
                image=IMAGE_NAME,
                name=CONTAINER_NAME,
                auto_remove=True,
                detach=True,
                ports={'5432/tcp': 5432},
                environment=[f'POSTGRES_PASSWORD={POSTGRES_PASSWORD}'],
            )

            print('\uf058 Container criado e iniciado com sucesso.')

        except Exception as e:
            print(f'\uea87 Star/Creating container error: {e}')
            return
