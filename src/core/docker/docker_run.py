import os
import sys

from docker.client import DockerClient
from docker.errors import DockerException, NotFound
from docker.models.containers import Container
from dotenv import load_dotenv

try:
    import docker
except ImportError as exc:
    raise ImportError(
        """Couldn't import Docker. Are you sure it's installed and /
        available on your PYTHONPATH environment variable? Did you
        forget to activate a virtual environment?"""
    ) from exc


def start_docker_container() -> Container:
    _ = load_dotenv()

    """starts a docker image with SQL database"""
    try:
        client: DockerClient = docker.from_env()

    except DockerException as exc:
        print(f'Something wrong was ocurred {exc}')
        sys.exit(1)

    CONTAINER_NAME = 'laws'
    IMAGE_NAME = 'laws-postegresql:latest'
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    DOCKERFILE_PATH = os.path.dirname(os.path.abspath(__file__))

    try:
        _ = client.images.build(
            path=DOCKERFILE_PATH,
            tag=IMAGE_NAME,
            rm=True,
        )
    except Exception as e:
        print(f'\uea87 Build image error: {e}')
        sys.exit(1)

    try:
        container: Container = client.containers.get(CONTAINER_NAME)
        container.reload()

        if container.status != 'running':
            print(f'\ueb7b Starting Container, Already exists: {CONTAINER_NAME}...')
            container.start()
        else:
            print(f'\uf058 Container is already running: {CONTAINER_NAME}.')

            # return container

    except NotFound:
        try:
            running_container = client.containers.run(
                image=IMAGE_NAME,
                name=CONTAINER_NAME,
                auto_remove=True,
                detach=True,
                ports={'5432/tcp': 5432},
                environment=[
                    f'POSTGRES_USER={POSTGRES_USER}',
                    f'POSTGRES_PASSWORD={POSTGRES_PASSWORD}',
                    'POSTGRES_DB=default',
                ],
            )

            print('\uf058 Container successfull started.')

        except Exception as e:
            print(f'\uea87 Start/Creating container error: {e}')
            sys.exit(1)

        return running_container


def stop_docker_container(container: Container):
    try:
        container.stop()
        print('Container stoped')

    except NotFound:
        print('Container already stoped')
        sys.exit(1)


if __name__ == '__main__':
    container = start_docker_container()
    # stop_docker_container(container)
